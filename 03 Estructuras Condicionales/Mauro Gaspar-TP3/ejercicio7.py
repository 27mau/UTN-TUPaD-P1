# 7
"""Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
pantalla."""

frase = input("Ingrese una palabra o frase: ").lower() # Uso lower() para convertir la cadena a minúscula.

ultima_letra = frase[-1]

if ultima_letra in 'aeiouáéíóú':
    print(f"{frase}!")
else:
    print(f"{frase}")

