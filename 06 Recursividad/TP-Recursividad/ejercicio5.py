# 5
"""Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
lo es. 
Requisitos: 
La solución debe ser recursiva. 
No se debe usar [::-1] ni la función reversed()."""

def es_palindromo(palabra):
    if len(palabra) <= 1:       # Caso base: si la palabra tiene 0 o 1 letra, es palíndromo
        return True
    
    if palabra[0] != palabra[-1]:   # Comparar primera y última letra
        return False
    return es_palindromo(palabra[1:-1])  # Llama recusiva con la palabra sin la primera y última letra

print(es_palindromo(input("Ingrese una palabra: ")))