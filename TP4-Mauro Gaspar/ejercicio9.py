# 9
"""Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
poder procesar 100 números cambiando solo un valor)."""

# Sumar los números enteros ingresados
suma = 0

cantidad = 10

# Iterar los 100 números
for i in range(10):
    num = int(input("Ingrese números enteros: "))
    suma += num

media = suma / cantidad

print(f"La media de los {cantidad} números es: {media}")