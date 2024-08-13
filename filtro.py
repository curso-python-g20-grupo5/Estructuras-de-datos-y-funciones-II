import sys #importación de librería sys
'''
Se solicita implementar una función que permita entregar lo
siguiente:
● Un diccionario con los productos que cumplen una cierta condición dado un umbral
● La función debe permitir mostrar los valores mayor que o menor que un umbral
(siempre estrictos).
● Por defecto la función debe siempre mostrar los valores mayor que el umbral a
menos que se indique lo contrario.

'''
#ingreso de datos mediante sys.argv, alojadas en variable 'umbral'
def filtrar_precios():
    datos = sys.argv
    umbral = int(datos[1])

    #Diccionario
    precios = {'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000}

#Se crean diccionarios vacíos
    mayores = {}
    menores = {}

#Filtrar productos por umbral 
    for producto, valor in precios.items():
        if valor > umbral:
            mayores[producto] = valor
        elif valor < umbral:
            menores[producto] = valor

#Se convierten los resultados a cadenas de texto
    may = ", ".join(mayores)
    men = ", ".join(menores)

# se Verifica la longitud de los datos para determinar la salida
    if len(datos) == 2:
        print("Los productos mayores a umbral son: ", may)
    elif len(datos) == 3 and datos[2]== "menor" :
        print("Los productos menores a umbral son: ", men)
    else:
        print("Lo sentimos, no es una operación válida")

# Llamada a la función
filtrar_precios()







