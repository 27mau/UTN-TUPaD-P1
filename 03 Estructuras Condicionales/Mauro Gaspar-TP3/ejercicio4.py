# 4
"""Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
siguientes categorías pertenece: 
● Niño/a: menor de 12 años. 
● Adolescente: mayor o igual que 12 años y menor que 18 años. 
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
● Adulto/a: mayor o igual que 30 años."""

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Eres niño/a.")

elif 12 <= edad < 18:
    print("Eres un adolescente.")
elif 18 <= edad < 30:
    print("Eres un adulto/a joven.")
else:
    print("Eres un adulto/a mayor.")