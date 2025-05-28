# 9
"""Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función."""
# Definimos la función que pasa de fahrenheit a celsius.
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

# Ingresa valor en Cº.
temperatura = int(input("Ingrese una temperatura en ºC: "))

# Llama a la función y guarda en una variable.
resultado = celsius_a_fahrenheit(temperatura)
print(f"La temperatura {temperatura}ºC en Fahrenheit es: {resultado:.2f}ºF")

