# *********************************************************************
# HACER UNA COPIA DE ESTE ARCHIVO A LA CARPETA
# CODIGO_ESTUDIANTES
# NO SOBRESCRIBIR ESTE ARCHIVO PARA EVITAR CONFLICTOS DE SINCRONIZACION
# *********************************************************************


# ---------------------------------------------------------------------
#  Ejercicio 1 - Convertir temperaturas
# ---------------------------------------------------------------------
"""
Dada la lista de temperaturas en °C, obtené una nueva lista
con las temperaturas en °F, redondeadas a 1 decimal.

Clue: fórmula → F = C * 9/5 + 32 y usá round(valor, 1).
"""

temperaturas = [1, 9.2, 5.5, 2.3, 6.5]
temperaturasDos = list(map(lambda num: round(num*9/5+32, 1), temperaturas))
print (temperaturasDos)

# ---------------------------------------------------------------------
#  Ejercicio 2 - Promedio ponderado de notas
# ---------------------------------------------------------------------
"""
Dados dos listados paralelos con notas de parcial y final, 
calculá el promedio ponderado 0.4*parcial + 0.6*final para cada alumno. 
Redondeá a 1 decimal.
"""
parcial = [7, 8.5, 6, 9.5, 4]
final = [6, 7.5, 8, 9, 5]
promedios = list(map(lambda x, y: round(x*0.4 + y*0.6, 1), parcial, final))
print(promedios)

# ---------------------------------------------------------------------
#  Ejercicio 3 - Normalizar los nombres y apellidos de los estudiantes
# ---------------------------------------------------------------------
"""
Se solicita normalizar los nombre y apellidos de los estudiantes, de manera
que todos sus caracteres sean en minúscula, salvo la primer letra.
"""

estudiantes = ["maria gomez", "JUAN PEREZ", "luis MARTINEZ", "Ana lopez"]
estudiantesNormalizados = list(map(lambda nombre: nombre.title(), estudiantes))
print(estudiantesNormalizados)