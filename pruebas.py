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
"""
# OPERAR CON LISTAS
"""
import math
lst = []
numeros = []
indices = list(range(4))
print(indices)
lst.append(4) ## Agrega el valor a lo ultimo
lst.extend([3, 4]) ## Extiende la lista sumandole otra
lst.insert(1, 1.5)  ## Inserta 1.5 en la posicion 1
lst.remove(2) ## Elimina el primer 2 que encuentra
lst.pop() ## Elimina el ultimo elemento
lst.index(2) ## Busca el 2 y devuelve la posicion en donde aparecio por primera vez
lst.count(2) ## Devuelve la cantidad de veces que aparecio el 2
lst.sort() ## Ordena numericamente la lista de menor a mayor
lst.reverse() ## Invierte el orden de la lista 
longitud = len([1, 2, 3])
suma = sum([1, 2, 3])
minimo = min([1, 2, 3])
maximo = max([1, 2, 3])
lista = list((1, 2, 3)) ## Forma una lista con los parametros
print(f"lst[1:3]: {lst[1:3]}") ## Desde el idice 1 hasta el 3 (sin incluir al ultimo)
print(f"lst1 + lst2: {lst1 + lst2}") 
a, b, c = [1, 2, 3] 
print(f"Desempaquetado: a = {a}, b = {b}, c = {c}") ## Desempaquetado
cuadrados = [num**2 for num in numeros]
listaCuadradosParesPorComp = [num**2 for num in lista if num % 2 == 0] 
listaPorComp = [num**2 if num % 2 == 0 else num for num in lista] ## A los pareces los elevo al cuadrado
raices = [math.sqrt(x) for x in numeros] ## Raices
dobles = [(lambda x: x * 2)(x) for x in numeros]
"""
# OPERAR CON CARACTERES
"""
s = "hello"
lst = []
print(f"str.upper(): {s.upper()}")  # Resultado: 'HELLO'
print(f"str.strip(): '{s.strip()}'")  # Resultado: 'hello'
print(f"str.replace('e', 'a'): {s.replace('e', 'a')}")  # Resultado: 'hallo'
print(f"str.find('e'): {s.find('e')}")  # Resultado: 1
print(f"str.split(): {s.split()}")  # Resultado: ['hello', 'world']
print(f"str.join(lst): {' '.join(lst)}")  # Resultado: 'hello world' ## Los une en una cadena con un espacio de separacion+
print(f"cadena.lstrip(): '{' hola '.lstrip()}'")  # Resultado: 'hola '
print(f"cadena.rstrip(): '{' hola '.rstrip()}'")  # Resultado: ' hola'
print(f"cadena.center(10, '-'): '{'hola'.center(10, '-')}'")  # Resultado: '---hola----'
print(f"cadena.ljust(10, '-'): '{'hola'.ljust(10, '-')}'")  # Resultado: 'hola------'
print(f"cadena.rjust(10, '-'): '{'hola'.rjust(10, '-')}'")  # Resultado: '------hola'
print(f"cadena.zfill(5): '{'42'.zfill(5)}'")  # Resultado: '00042' ## Rellena con ceros
print(f"cadena.isalnum(): {('hola123'.isalnum())}")  # Resultado: True
print(f"cadena.isalpha(): {('hola'.isalpha())}")  # Resultado: True ##
print(f"cadena.isnumeric(): {('123'.isnumeric())}")  # Resultado: True ##
print(f"cadena.isspace(): {(' '.isspace())}")  # Resultado: True
print(f"cadena.isdigit(): {('123'.isdigit())}")  # Resultado: True
print(f"cadena.isdecimal(): {('123'.isdecimal())}")  # Resultado: True
print(f"separador.join(iterable): {', '.join(['manzana', 'banana', 'cereza'])}")  # Resultado: 'manzana, banana, cereza'
print("\nMétodo istitle() - ¿Cada palabra empieza con mayúscula?")
cadena = "Python Es Interesante"
print(cadena, "→", cadena.istitle())
cadena = "Python es interesante"
print(cadena, "→", cadena.istitle())
print("\nMétodos find() y rfind() - Posición de la subcadena dentro de la cadena") ## rfind() -> Devuelve el primer indice y el segundo -1
print("\nMétodos startswith() y endswith() - Verifica si comienza o termina con una subcadena")
## Metodos de mayus o min
texto = "hOLA, mUnDo. eSTO eS uN eJeMpLo."
texto_capitalize = texto.capitalize()
print("capitalize:", texto_capitalize)  # capitalize: Hola, mundo. esto es un ejemplo.
texto_title = texto.title()
print("title:", texto_title)  # title: Hola, Mundo. Esto Es Un Ejemplo.
texto_lower = texto.lower()
print("lower:", texto_lower)  # lower: hola, mundo. esto es un ejemplo.
texto_upper = texto.upper()
print("upper:", texto_upper)  # upper: HOLA, MUNDO. ESTO ES UN EJEMPLO.
texto_swapcase = texto.swapcase()
print("swapcase:", texto_swapcase)  # swapcase: Hola, MuNdO. Esto Es Un EjEmPlO.
cadena = "uno,dos,tres,cuatro,cinco"
lista_split = cadena.split(",")
print("split:", lista_split)  # ['uno', 'dos', 'tres', 'cuatro', 'cinco']
cadena_multilinea = "Hola mundo\nEsto es una prueba\nCon varias líneas"
lista_splitlines = cadena_multilinea.splitlines()
print("splitlines:", lista_splitlines)  # ['Hola mundo', 'Esto es una prueba', 'Con varias líneas']
cadena_multilinea = "Hola mundo\nEsto es una prueba\nCon varias líneas"
lista_splitlines = cadena_multilinea.splitlines()
print("splitlines:", lista_splitlines)  # ['Hola mundo', 'Esto es una prueba', 'Con varias líneas']
legajo, nombre, nota = 11212, "Maria", 10
print("Legajo: %d, Nombre: %s, Nota: %d" % (legajo, nombre, nota))  # Legajo: 11212 Nombre: María Nota: 10
"""
# LAMBDA 
"""
lambdaSumar = lambda num1, num2: num1 + num2
mayor = lambda x, y: x if x > y else y
menor = lambda x, y: x if x < y else y
estudiantes_datos = [["Thiago", "Almada", 19], ["Agostina", "Hein", 25], ["Leandro", "Bolmaro", 22], ["Valentina", "Raposo", 24],]
estudiantes_datos_ordenados = sorted(estudiantes_datos, key=lambda x: x[2], reverse=False)
calificaciones, calificaciones_rounded = [8, 8.5, 9, 9.75], []
calificaciones_rounded = list(map(lambda x:round(x), calificaciones)) # map (funcion, iterable)
calificaciones = [8, 7, 6.5, 8.5, 5, 9, 9.75]
calificaciones_filtradas = list(filter(lambda x: x>=7 , calificaciones)) ## Solo los valores que pasen el filtro
calificaciones = [8, 8.5, 5, 9.75]
calificaciones_int = list(map( lambda calificacion : (round(calificacion), "Aprobo" if calificacion > 7 else "Desaprobo") , calificaciones  ))
"""
# DICCIONARIOS
"""
estudiante = {
    'nombre': 'Carlos',
    'edad': 19,
    'materias': ['Programación I', 'Sistemas de información I']
}
print(estudiante['nombre']) # Carlos
print(list(estudiante.keys()))
print(list(estudiante.values()))
print(list(estudiante.items()))
del estudiante['nombre']
dic = dict(nombre='Juan', apellido='Pérez', edad=38)
dic_zip = zip('abcd',[1,2,3,4])
dic = dict(zip('abcd',[1,2,3,4]))
print(dict(zip(['num1', 'num2', 'num3', 'num4'],[1,2,3,4])))
print(dic.get('f', 'No existe.')) # No existe.
valor = dic.setdefault('e',5) ## AGREGAR OTRO VALOR
print(dic)

dic1 = {'a' : 1, 'b' : 2, 'c' : 3 , 'd' : 4}
dic2 = {'c' : 6, 'b' : 5, 'e' : 9 , 'f' : 10}
dic1.update(dic2) ## Pisa los repetidos
valor = dic.pop('b')
dic = dict.fromkeys(['a','b','c','d'],1)
matriz, encabezados = [], []
productos = [dict(zip(encabezados, fila)) for fila in matriz] ## DE LISTA A DICCIONARIO
"""