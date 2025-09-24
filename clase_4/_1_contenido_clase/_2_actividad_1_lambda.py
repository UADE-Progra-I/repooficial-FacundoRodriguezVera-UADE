# *********************************************************************
# HACER UNA COPIA DE ESTE ARCHIVO A LA CARPETA
# CODIGO_ESTUDIANTES
# NO SOBRESCRIBIR ESTE ARCHIVO PARA EVITAR CONFLICTOS DE SINCRONIZACION
# *********************************************************************


# ---------------------------------------------------------------------
#  Ejercicio 1 - Elevar al cuadrado
# ---------------------------------------------------------------------
"""
Declara una función lambda llamada cuadrado que reciba un número y devuelva ese número al cuadrado.
Prueba tu función con los valores 2, 5 y 10.
"""
cuadrado = lambda x: x ** 2
print(cuadrado(2))  # Output: 4
print(cuadrado(5))  # Output: 25
print(cuadrado(10))  # Output: 100

# ---------------------------------------------------------------------
# Ejercicio 2 – Obtener el mayor de dos números
# ---------------------------------------------------------------------
"""
Declara una función lambda llamada mayor que reciba dos números y devuelva el mayor de los dos.
Prueba con los pares: (7, 3), (10, 15) y (20, 20).

Clue: usar el operador ternario 
val1 if condicion else val2
"""

mayor = lambda x, y: x if x > y else y
print(mayor(7, 3))    # Output: 7

menor = lambda x, y: x if x < y else y
print(menor(1,2))

