# 7 
"""Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
número entero positivo indicado por el usuario."""

# Un bucle infinito hasta que se ingrese un número entero positivo
while True:
    num = int(input("Ingrese un número entero positivo: "))
    
    # Verifica si el número ingresado es positivo, si no es rompe el bucle.
    if num > 0:
        break
    else:
        print("Por favor, ingrese un número entero positivo.")

suma = 0

# Itera sobre los números ingresados desde 0 hasta el número ingresado
for i in range(0, num):
    # Acumula la suma de los números de la variable suma.
    suma += i

print(f"La suma de los números entre 0 y {num} es: {suma}")
