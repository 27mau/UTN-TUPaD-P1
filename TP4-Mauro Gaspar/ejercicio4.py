# 4
"""Elabora un programa que permita al usuario ingresar números enteros y los sume en 
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
un 0."""

num = 0
suma = 0

# Creo un bucle infinito hasta que ingresamos "0", y sumamaos los números ingresados
while True:
    num = int(input("Ingrese un número entero (0 para finalizar): "))
    suma += num 

# Si se ingresa 0 se detiene el bucle
    if num == 0:
        break

print(f"La suma de los números ingresados es: {suma}")

