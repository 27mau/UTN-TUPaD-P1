#7
"""Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos."""

while True:

    numero = int(input("Ingrese un número entero distinto de 0: "))
    
    if numero == 0:
        break

    numero1 = int(input("Ingrese un número entero distinto de 0: "))

    if numero1 == 0:
        break

    suma = numero + numero1
    resta = numero - numero1
    multiplicacion = numero * numero1
    division = numero / numero1

    print(f"Los números enteros {numero} + {numero1} es: {suma}")
    print(f"Los números enteros {numero} / {numero1} es: {division:.2f}")
    print(f"Los números enteros {numero} x {numero1} es: {multiplicacion}")
    print(f"Los números enteros {numero} - {numero1} es: {resta}")