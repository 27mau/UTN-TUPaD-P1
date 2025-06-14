# 5
"""Solicita al usuario una frase e imprime: 
• Las palabras únicas (usando un set). 
• Un diccionario con la cantidad de veces que aparece cada palabra."""

frase = input("Ingrese una frase: ")

palabras = frase.split()    # split() para separar las palabras.

palabra_unicas = set(palabras)  # set() para obtener palabras únicas.

diccionario = {}    # Guardamos las palabras contadas

# Condicional para contar las palabras
for palabra in palabras:
    if palabra in diccionario:
        diccionario[palabra] += 1
    else: 
        diccionario[palabra] = 1

print("Palabras:",palabras)
print("Palabras únicas:",palabra_unicas)
print("Cantidad de veces que aparece:", diccionario)