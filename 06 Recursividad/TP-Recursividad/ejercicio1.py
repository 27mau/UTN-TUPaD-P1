# 1
"""Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
función para calcular y mostrar en pantalla el factorial de todos los números enteros 
entre 1 y el número que indique el usuario"""
# Define una función recursiva
def factorial(numero):
    if numero == 0 or numero == 1:  # Caso base, si el factorial de 0 o 1 es 1
        return 1    
    else:
        return numero * factorial(numero - 1) # Llamada recursiva

# Solicita numero al usuario
numero_final = int(input("Ingrese un número entero positivo: "))

# Se usa un bucle para calcular y mostrar el factorial
# Mostrar factorial desde 1 hasta el número ingresado
for i in range(1, numero_final + 1):
    resultado = factorial(i)    # Calculamos el factorial del número actual usando la función
    print(f"El factorial de {i} es {resultado}")
