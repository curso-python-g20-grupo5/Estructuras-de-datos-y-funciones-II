def calcular_factorial(n):
    """Calcula el factorial de un número."""
    if n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

def calcular_productoria(lista):
    """Calcula la productoria de una lista de números."""
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado

def calcular(**kwargs):
    """Controla el cálculo de factoriales y productorias."""
    for clave, valor in kwargs.items():
        if 'fact' in clave:
            resultado = calcular_factorial(valor)
            print(f"El factorial de {valor} es {resultado}")
        elif 'prod' in clave:
            resultado = calcular_productoria(valor)
            print(f"La productoria de {valor} es {resultado}")
        else:
            print(f"Operación no reconocida: {clave}")

# Ejemplo de uso:
calcular(fact_1=5, prod_1=[4, 6, 7, 4, 3], fact_2=6, fact_3=0, frod_1=[1, 2, 3])
