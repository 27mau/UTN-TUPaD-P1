#10
"""Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
dichos números."""

while True:
    try:
        
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        num3 = float(input("Ingrese el tercer número: "))

        promedio = float((num1 + num2 + num3) / 3)

        print(f"El promedio de los 3 números es: {promedio:.2f}\n")

        continuar = input("Continuar? (s/n): ").strip().lower()
        if continuar != "s":
            print("Programa terminado.")
            break

    except ValueError:
        print("Ingrese un número válido.")
