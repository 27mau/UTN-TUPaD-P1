# 6
"""Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
Luego, mostrá el promedio de cada alumno."""

# Se crea diccionario vacío
alumnos = {}

# Bucle para cargar los datos de los 3 alumnos
for i in range(3):
    nombre = input(f"Ingresa el nombre del alumno {i+1}: ")

    notas = input(f"Ingresa 3 notas de {nombre}, separadas por espacio: ")

    notas = tuple(map(int, notas.split())) # Convierte la cadena ingresada a una lista de enteros y luego a tupla

    alumnos[nombre] = notas     # Se guarda en el diccionario el nombte como clave y la tupla como valor

for nombre, notas in alumnos.items():
    # Calcula el promedio de las notas
    promedio = sum(notas) / len(notas)

    print(f"{nombre}: promedio = {promedio:.2f}")