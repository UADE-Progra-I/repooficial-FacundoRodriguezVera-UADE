# CREAR MATRICES
"""
#UNO
matriz3x4 = []  # Creamos una lista vacía
for fil in range(3):
    matriz3x4.append([])  # Agregamos una nueva fila
    for col in range(4):
        matriz3x4[fil].append(0)  # Agregamos un nuevo elemento a la fila
print("\nMetodo 1:")
print(matriz3x4)

matriz = []
matrizUno = []
for i in range(2):
    matriz.append([])
    matrizUno.append([])
    for j in range(3):
        matrizUno[i].append(0)
        matriz[i].append(j)
print(matriz)
print(matrizUno)

#DOS
matriz3x4 = []  # Creamos una lista vacía
for fil in range(3):
    matriz3x4.append([0] * 4)  # Agregamos una nueva fila
print("\nMetodo 2:")
print(matriz3x4)

matriz = []
for i in range(3):
    matriz.append([0]*4)
print(matriz)

#TRES
matriz3x4porComp = [[0] * 4 for i in range(3)]
print("\nMetodo 3:")
print(matriz3x4porComp)

matriz = [[i]*4 for i in range(3)]
print(matriz)

import random
matriz3x4porComp = [[random.randint(1, 10)] * 4 for fil in range(3)]
print("\nMetodo 4:")
print(matriz3x4porComp)
"""

# CREAR MATRICES # SUMA # MULTIPLICACION
"""
def sumar_matrices(matrizA, matrizB):
    # Para sumar matrices deben tener la misma longitud
    if len(matrizA) != len(matrizB) or len(matrizA[0]) != len(matrizB[0]):
        print("Imposible sumar matrices de diferente dimensión")
        return
    nFilas = len(matrizA)
    nColumnas = len(matrizA[0])
    resultado = [[0]*nColumnas for i in range(nFilas)]
    for i in range(nFilas):
        for j in range(nColumnas):
            resultado[i][j] = matrizA[i][j] + matrizB[i][j]
    return resultado
print(sumar_matrices([[0]*4 for i in range(3)], [[1]*4 for i in range(3)]))

def suma(mUno,mDos):
    if len(mUno) != len(mDos) or len(mUno[0]) != len(mDos[0]):
        print("No se puede")
        return False
    f = len(mUno)
    c = len(mUno[0])
    resultado = [[0]*len(mUno[0]) for i in range(len(mUno))]
    for i in range(len(mUno)):
        for j in range(len(mUno[0])):
            resultado[i][j] = mUno[i][j] + mDos[i][j]
    return resultado 

print(suma([[0]*4 for i in range(3)], [[1]*4 for i in range(3)]))

def matriz_por_escalar(matriz, escalar):
    nFilas = len(matriz)
    nColumnas = len(matriz[0])
    resultado = [[0]*nColumnas for i in range(nFilas)]
    for i in range(nFilas):
        for j in range(nColumnas):
            resultado[i][j] = matriz[i][j] * escalar
    return resultado

def matrixXescalar(mUno, escalar):
    resultado = [[0]*len(mUno[0]) for i in range(len(mUno))]
    for i in range(len(mUno)):
        for j in range(len(mUno[0])):
            resultado[i][j] = mUno[i][j] * escalar
    return resultado 
print(matrixXescalar([[3]*4 for i in range(3)], 2))
"""
def matriz_por_matriz(matrizA, matrizB):
    # matriz 3x3 multiplica a matriz de 3x2 => resultado matriz 3x2
    # Condición: nColumnasA == nFilasB # Si las columnas de B son iguales a las filas de A??? Osea al revez?
    nFilasA = len(matrizA)
    nColumnasA = len(matrizA[0])
    nFilasB = len(matrizB)
    nColumnasB = len(matrizB[0])

    if nColumnasA != nFilasB:
        print("Solo se pueden multiplicar matrices cuando nColumnasA es igual a nFilasB")
        return None

    matriz_resultado = [[0]*nColumnasB for i in range(nFilasA)]

    for i in range(nFilasA):
        for j in range(nColumnasB):
            suma = 0
            for k in range(nFilasB):
                suma += matrizA[i][k] * matrizB[k][j]
            matriz_resultado[i][j] = suma

    return matriz_resultado

def multiplicar(mUno, mDos):
    if len(mUno[0]) != len(mDos):
        print("No se puede hacer esto che")
        return False
    resultado = [[0]*len(mDos[0]) for i in range(len(mUno))]
    for i in range(len(mUno)):
        for j in range(len(mDos[0])):
            suma = 0 
            for k in range(len(mDos)):
                suma += mUno[i][k] * mDos[k][j]
            resultado[i][j] = suma
    return resultado
print([[6]*3 for i in range(3)])
print([[1]*4 for i in range(3)])
print(multiplicar([[6]*2 for i in range(4)], [[1]*4 for i in range(2)]))
print(matriz_por_matriz([[6]*2 for i in range(4)], [[1]*4 for i in range(2)]))