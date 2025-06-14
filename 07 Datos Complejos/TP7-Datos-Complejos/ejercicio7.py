# 7
"""Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
y Parcial 2: 
• Mostrá los que aprobaron ambos parciales. 
• Mostrá los que aprobaron solo uno de los dos. 
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
"""

parcial_1 = {"Roberto", "Luis", "Matias", "Rosa", "Camila", "Emanuel"}

parcial_2 = {"Camila", "Mauro", "Pablo", "Luis", "Pedro", "Gisel"}
# Se usa el operador & para obtener solo los nombres de ambos sets
aprobado_ambos = parcial_1 & parcial_2
print("Aprobaron ambos parciales:", aprobado_ambos)

# El operador ^ devuelve los elementos que estan en uno u otro.
solo_uno = parcial_1 ^ parcial_2
print("Aprobaron solo en un parcial:", solo_uno)

# El operador | combina todos los elementos, sin repetir
todos = parcial_1 | parcial_2
print("Aprbaron al menos un parcial:", todos)