# ******************************************
# Actividad 1
# Listas y Metodos
# ******************************************

import random

"""
Sugerencia:
dentro de la carpeta "codigo_estudiantes" crear un archivo python,
copiar y pegar alli estas consignas y trabajar en ese archivo
"""

# Datos para comenzar
estudiantes_header = ["id_estudiante", "nombre", "apellido", "email"]

estudiantes_datos = [
    ["Thiago", "Almada"],
    ["Agostina", "Hein"],
    ["Leandro", "Bolmaro"],
    ["Valentina", "Raposo"],
]


estudianteIds = [i for i in range(1, len(estudiantes_datos) +1) ]
estudiantesNumbres = [estudiantes_datos[i][0] for i in range(len(estudiantes_datos))]
estudiantesApellidos = [estudiantes_datos[i][1] for i in range(len(estudiantes_datos))]
estudiantesMail = [f"{estudiantes_datos[i][0].lower()}.{estudiantes_datos[i][1].lower()}@gmail.com" for i in range(len(estudiantes_datos))]
print ("Ids de estudiantes:", estudianteIds)  
print ("Nombres de estudiantes:", estudiantesNumbres) 
print ("Apellidos de estudiantes:", estudiantesApellidos) 
print ("Emails de estudiantes:", estudiantesMail) 


# 1
for i in range(len(estudiantes_datos)):
    estudiantes_datos[i].append(f"{estudiantes_datos[i][0].lower()}.{estudiantes_datos[i][1].lower()}@gmail.com")
# Agregar emails ficticios usando append()
# Ejemplo: para Thiago Almada → [1, "Thiago", "Almada", "talmada@mail.com"].

# 2
for i in range(len(estudiantes_datos)):
    estudiantes_datos[i].insert(0, estudianteIds[i])
# Agregar los ids faltantes usando insert()

# 3
estudiantes_datos.append([estudiantes_datos[-1][0]+1, "Roberto", estudiantes_datos[-1][2], f"roberto.{estudiantes_datos[-1][2].lower()}@gmail.com"])
# Agregar un nuevo estudiante al final con append()
# Hacer que el apellido de este estudiante se repita
# Ejemplo: [5, "Diego", "Almada", "dalmada@gmail.com"]

# 4
for estudiante in estudiantes_datos:
    if estudiante[2] == "Almada":
        estudiantes_datos.remove(estudiante)
# Eliminar un estudiante por apellido usando remove()

# 5
estudianteEliminado = estudiantes_datos[-1]
for estudiante in estudiantes_datos:
    estudiantes_datos[-1].pop()  # Quitar el último estudiante
print(estudiantes_datos)
print("Estudiante eliminado:", estudianteEliminado) # Me queda el [.., []]
# Quitar el último estudiante usando pop() y mostrar qué estudiante fue eliminado.

# 6
"""
print("Estudiantes:", estudiantes_datos)
estudiantesApellidos = [estudiantes_datos[i][2] for i in range(len(estudiantes_datos))]
print("Apellidos de estudiantes:", estudiantesApellidos)
print(estudiantesApellidos.index("Bolmaro"))
"""
# Buscar la posición (índice) de un apellido con index().
# 7
# Contar cuántos estudiantes tienen el mismo apellido con count() (simular apellidos repetidos agregando uno igual).
# Clue 1: generar una lista solo con apellidos
# Clue 2: investigar como implementarlo con listas por comprension
lista = ["a", "b", "b", "a", "c", "d"]
lista_sin_repeticiones = [ (i, lista.count(i)) for i in lista]
print(lista_sin_repeticiones)

lista = ["a", "b", "b", "a", "c", "d"]
lista_sin_repeticiones = []
[lista_sin_repeticiones.append(i) for i in lista if i not in lista_sin_repeticiones]
print(lista_sin_repeticiones)  
# 8
# Ordenar alfabéticamente los estudiantes por nombre
# Clue 1: Pueden usar sort pero deben combinarlo con funcion lambda
# Clue 2: Pueden usar el método "Bubble Sort"

# NOTA:
# Si usan IA, debe ser con "pensamiento crítico"


#estudiantes_datos[0][1]  
#for i in estudiantes_datos:
#    print(i[1][0])