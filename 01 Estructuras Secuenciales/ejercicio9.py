#9
"""Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: """

while True:

    entrada = input("Ingrese valor de temperatura Celsius('s' para salir): ")

    if entrada.lower() == "s":
        print("Programa termindo.")
        break

    celsius = float(entrada)
    fahrenheit = float(celsius * 1.8) + 32

    print(f"La temperatura ingresada, en Fahrenheit es: {fahrenheit:.1f}")

