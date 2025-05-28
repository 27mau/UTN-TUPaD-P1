# 7 
"""Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resulta
do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
sultados de forma clara."""
# La función toma dos parámetros y realiza las siguientes operaciones.
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    # Usamos un if para evitar la división por cero.
    division = a / b if b != 0 else "Error de división por cero."
    return (suma, resta, multiplicacion, division) # Los resultados se almacenan en una tupla

# Ingreas los dos parámetros.
a = int(input("Ingrese 1re número entero: "))
b = int(input("Ingrese 2do número entero: "))

# Llama a la función y se guarda en una variable.
resultado = operaciones_basicas(a, b)
print(resultado)
print(f"Suma: {resultado[0]}")
print(f"Resta: {resultado[1]}")
print(f"Multiplicación: {resultado[2]}")
print(f"División: {resultado[3]}")