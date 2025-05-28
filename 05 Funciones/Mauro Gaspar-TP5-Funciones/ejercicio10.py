# 10
"""Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función."""
# Definimos la función promedio, con 3 parámetros.
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

# Ingresa los númerso a promediar.
a = float(input("Ingrese 1er número: "))
b = float(input("Ingrese 2do número: "))
c = float(input("Ingrese 3er número: "))

# Llamamos a la función y mostramos en pantalla.
resultado = calcular_promedio(a, b, c)
print(f"El promedio de los números ingresados es: {resultado:.2f}")