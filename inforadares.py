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

#función para el ejercicio 3
def ejercicio3(doc, ruta1):
    lista_provincias=datos(doc, ruta1)
    lista_grande=[]
    lista_pequeña=[]
    for i in lista_provincias:
        #lista_pequeña.append(i)
        lista_pequeña.append(datos(doc,"/RAIZ/PROVINCIA[NOMBRE='%s']/CARRETERA/DENOMINACION/text()" %(i)))
        #lista_grande.append(lista_pequeña)
        #lista_pequeña=[]
    return zip(lista_provincias,lista_pequeña)

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
        tecla= input("PRESIONA UNA INTRO PARA CONTINUAR")

    elif opcion=="2":
        print("Tenemos constancia de",len(datos(doc, "//CARRETERA/RADAR/PUNTO_INICIAL/PK/text()")), "radares")
        print(" ")
        tecla= input("PRESIONA UNA INTRO PARA CONTINUAR")

    elif opcion=="3":
        #for i in ejercicio3(doc, "/RAIZ/PROVINCIA/NOMBRE/text()"):
        #    for x in i:
        #        print("Carreteras de", x)
        for prov, total in ejercicio3(doc, "/RAIZ/PROVINCIA/NOMBRE/text()"):
            print(prov,"- Cantidad de radares:", len(total))
            for i in total:
                print("     -",i)
            print("")
        tecla= input("PRESIONA UNA INTRO PARA CONTINUAR")

    elif opcion=="4":

        print("")
        tecla= input("PRESIONA UNA INTRO PARA CONTINUAR")

    elif opcion=="5":

        print("")
        tecla= input("PRESIONA UNA INTRO PARA CONTINUAR")

    elif opcion=="0":
        print("Adios")
        break
    else:
        print("Lo siento, no hay ninguna opción disponible")
        print(" ")
             



