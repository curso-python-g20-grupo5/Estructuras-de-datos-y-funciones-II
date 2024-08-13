# Estructuras de datos y funciones II
En este repositorio se presenta el desarrollo para la actividad Estructuras de datos y funciones II.

## Descripción del proyecto

Este repositorio está compuesto por cuatro archivos: 
  - ```filtro.py```: este archivo corresponde a la solución de la actividad 'Filtro'
  - ```velocidad.py```: este es un texto generado para ser importado a Python 'velocidad'
  - ```ong.py```: este es un texto generado para ser importado a Python 'ong'

## Actividad 1: Filtrado relevante.

En esta actividad se nos pide filtrar productos de una tienda de tecnología según su precio, comparándolos con un umbral especificado. Se crea el archivo llamado ´´´filtro.py´´´ contiene una función que procesa un diccionario de productos y sus precios. La función permite mostrar:

- Un diccionario con los productos cuyos precios son mayores que un umbral dado.
- Un diccionario con los productos cuyos precios son menores que un umbral, si se especifica.

Funcionalidad

- Filtrar productos que cumplan con una condición de precio basada en un umbral.
- Mostrar productos con precios estrictamente mayores al umbral por defecto.
- Opción de mostrar productos con precios estrictamente menores al umbral si se especifica con el argumento "menor".
- Gestión de entradas mediante sys.argv para recibir los argumentos desde la línea de comandos.

Uso

Para ejecutar el script, utiliza el siguiente comando en la terminal:

Productos con precios mayores al umbral:
´´´
python filtro.py 30000
´´´
Salida:
´´´
Los productos mayores a umbral son: Notebook, Monitor, Escritorio, Tarjeta de Video
´´´

Productos con precios menores al umbral:
´´´
python filtro.py 30000 menor
´´´
Salida:
´´´
Los productos menores a umbral son: Teclado, Mouse
´´´

Operación no válida:
´´´
python filtro.py 30000 otro
´´´
Salida:
´´´
Lo sentimos, no es una operación válida
´´´
## Actividad 2: Alertas telemáticas.

En esta actividad se nos pide analizar y monitorear la eficiencia energética de correas transportadoras mediante el cálculo y filtrado de sus velocidades. La aplicación identifica qué correas transportadoras están operando por encima del promedio de velocidad, lo que podría indicar un consumo excesivo de energía. Se crea el archivo velocidad.py para calcular el promedio de velocidades de una lista de correas transportadoras y para identificar cuáles de estas están operando por encima de dicho promedio.

Funcionalidad

- Cálculo del Promedio: Calcula el promedio de una lista de velocidades proporcionadas.
- Filtrado de Velocidades: Identifica las posiciones en la lista de aquellas correas transportadoras que tienen una velocidad superior al promedio calculado.

Uso
Para ejecutar el programa, utiliza el siguiente comando en la terminal:

python velocidad.py

Al ejecutarlo, se calculará el promedio de las velocidades y se listarán las posiciones de las correas que están por encima de este promedio:

#Lista de velocidades
velocidad = [25, 12, 19, 16, 11, 11, 24, 1,
14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

Calcular el promedio y filtrar las velocidades
print(filtrar(velocidad, promedio(velocidad)))

Salida:

[0, 2, 3, 6, 13, 15, 17, 19, 29, 30, 31, 34, 36, 37, 40, 47, 49, 55, 56, 58, 59]
Esto indica que las correas en las posiciones listadas están operando por encima del promedio de velocidad.

## Actividad 3: Apoyo Matemático.





## Autores y Autoras

- [Rosa Rubio](https://github.com/PaulinaRubioP)
- [Valery Maragaño](https://github.com/Valyxp)
- [Marco Alvarado](https://github.com/7pixel-cl)
- [Esteban Hernández](https://github.com/stivhc)
- [Claudia Aguayo](https://github.com/aguayo40)

⌨️ con ❤️ por el Grupo 5 - G20 😊
