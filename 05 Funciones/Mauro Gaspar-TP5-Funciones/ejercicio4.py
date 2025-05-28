# 4 
"""Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
dio como parámetro y devuelva el área del círculo. calcular_peri
metro_circulo(radio) que reciba el radio como parámetro y devuel
va el perímetro del círculo. Solicitar el radio al usuario y llamar am
bas funciones para mostrar los resultados."""
import math # Importamos la librería para usar pi.

# Definimos la función para el área el círculo.
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

# Definimos la función para calcular el perímetro del círculo.
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# El usuario ingresa el valor del radio.
radio = float(input("Ingrese el número del radio del círculo: "))
# Llamamos a las funciones y mostramos los resultados
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
# Imprime los resultados con solo dos decimales
print(f"Área del círculo es: {area:.2f}")
print(f"Perímetro del círculo es: {perimetro:.2f}")