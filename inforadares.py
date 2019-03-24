#importar xml
from lxml import etree
doc=etree.parse('radares.xml')

#función para el ejercicio 1
def ejercicio1(doc, ruta):
    lista_repetida=datos(doc, ruta)
    lista_sin_repetir=datosSinRepetir(lista_repetida)
    return lista_sin_repetir

#función que crea una lista a partir de una ruta
def datos(doc, ruta):
    lista=[]
    dato=doc.xpath(ruta)
    for i in dato:
        lista.append(i)
    return lista

#función que recibe una lista y elimina los valores repetidos
def datosSinRepetir(lista):
    lista_sin_repetir=[]
    for i in lista:
        existe=False
        for x in lista_sin_repetir:
            if i==x:
                existe=True
        if existe==False:
            lista_sin_repetir.append(i)
    return lista_sin_repetir

#función para el ejercicio 4
def ejercicio4(doc, ruta):
    lista_carreteras_repetidas=datos(doc, ruta)
    lista_carreteras_sin_repetir=datosSinRepetir(lista_carreteras_repetidas)
    return lista_carreteras_sin_repetir

#menu principal
while True:
    print('''
1.- Listar las provincias de las que tenemos información sobre radares
2.- Contar los radares de los que tenemos información
3.- Nombre de las carreteras y cantidad de radares según provincia
4.- Mostrar provincias y radares según carretera
5.- Mostrar radares y coordenadas de estos según carretera
0.- Salir''')
    opcion=input("Opción: ")
    print("")
    if opcion=="1":
        for i in range(len(ejercicio1(doc,"/RAIZ/PROVINCIA/NOMBRE/text()"))):
            print(i, "-", ejercicio1(doc,"/RAIZ/PROVINCIA/NOMBRE/text()")[i])
        print("")
        tecla= input("PRESIONA INTRO PARA CONTINUAR")

    elif opcion=="2":
        print("Tenemos constancia de",len(datos(doc, "//CARRETERA/RADAR/PUNTO_INICIAL/PK/text()")), "radares")
        print(" ")
        tecla= input("PRESIONA INTRO PARA CONTINUAR")

    elif opcion=="3":
        prov=input("Introduce la provincia: ")
        print("")
        while prov not in ejercicio1(doc,"/RAIZ/PROVINCIA/NOMBRE/text()"):
            print("Ha ocurrido un error. La provincia que has introducir no se encuentra")
            print("Prueba escribiendo la primera letra en mayúscula")
            print("")
            prov=input("Introduce la provincia: ")
        print("Los radares en", prov, "son", len(datos(doc,"/RAIZ/PROVINCIA[NOMBRE='%s']/CARRETERA/DENOMINACION/text()" %(prov))))
        print("Las carreteras son:")
        for i in datosSinRepetir(datos(doc,"/RAIZ/PROVINCIA[NOMBRE='%s']/CARRETERA/DENOMINACION/text()" %(prov))):
            print(" -", i)
        print("")
        tecla= input("PRESIONA INTRO PARA CONTINUAR")

    elif opcion=="4":
        print("Las carreteras con radares son:")
        for i in datosSinRepetir(datos(doc, "/RAIZ/PROVINCIA/CARRETERA/DENOMINACION/text()")):
            print("     -",i)
        car=input("Introduce la carretera: ")
        print("")
        print("Las carreteras son:")              
        while car not in datos(doc,"/RAIZ/PROVINCIA/CARRETERA/DENOMINACION/text()"):
            print("Ha ocurrido un error. La carretera que has introducir no se encuentra")
            print("")
            car=input("Introduce la carretera: ")
        carretera=datos(doc, "/RAIZ/PROVINCIA[CARRETERA/DENOMINACION='%s']/NOMBRE/text()" %(car))
        print("La carretera", car,"tiene",len(carretera), "radar/es")
        print("y pasa por:")
        for i in carretera:
            print("     -",i)
        print("")
        tecla= input("PRESIONA INTRO PARA CONTINUAR")

    elif opcion=="5":
        print("Las carreteras con radares son:")
        for i in datosSinRepetir(datos(doc, "/RAIZ/PROVINCIA/CARRETERA/DENOMINACION/text()")):
            print("     -",i)
        car=input("Introduce la carretera: ")
        lat=datos(doc, "/RAIZ/PROVINCIA/CARRETERA[DENOMINACION='%s']/RADAR/PUNTO_INICIAL/LATITUD/text()" %(car))
        lon=datos(doc, "/RAIZ/PROVINCIA/CARRETERA[DENOMINACION='%s']/RADAR/PUNTO_INICIAL/LONGITUD/text()" %(car))
        for i in range(len(lat)):
            print('https://www.openstreetmap.org/#map=15/%s/%s' %(lat[i], lon[i]))

        print("")
        tecla= input("PRESIONA INTRO PARA CONTINUAR")

    elif opcion=="0":
        print("Adios")
        break
    else:
        print("Lo siento, no hay ninguna opción disponible")
        print(" ")
             

#https://www.openstreetmap.org/#map=6/40.007/-2.488
#https://www.openstreetmap.org/#map=6/latitud/longitud

