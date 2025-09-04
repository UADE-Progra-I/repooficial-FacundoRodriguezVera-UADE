# *********************************************************************
# HACER UNA COPIA DE ESTE ARCHIVO A LA CARPETA
# CODIGO_ESTUDIANTES
# NO SOBRESCRIBIR ESTE ARCHIVO PARA EVITAR CONFLICTOS DE SINCRONIZACION
# *********************************************************************

# ---------------------------------------------------------------------
#  Ejercicio 1 - Ordenar una lista de listas
# ---------------------------------------------------------------------
"""
Declarar una lista de listas con una matriz de tu proyecto.
Luego generar una función que retorne la lista ordenada por alguna variable numérica.

Clue: usar función sorted combinada con lambda para ordenar ese arreglo
"""

matriz = [
    ["producto A", 30, 200.5],
    ["producto B", 20, 150.0],
    ["producto C", 50, 300.7],
    ["producto D", 10, 100.2],
]
matriz_ordenada = sorted(matriz, key=lambda x: x[1])
print(matriz_ordenada) ## ¿Sorted y sort ordenan numero y letra?

# ---------------------------------------------------------------------
#  Ejercicio 2 - Invertir el orden
# ---------------------------------------------------------------------
"""
Generar una función complementaria, que además de ordenar, 
lo haga de forma ascendente o descendente, según indique el usuario 
"""
desicion = input("1 o 2: -> ")
if desicion == "1":
    matriz_ordenada = sorted(matriz, key=lambda x: x[1], reverse=False)
else:
    matriz_ordenada = sorted(matriz, key=lambda x: x[1], reverse=True)
print(matriz_ordenada)

