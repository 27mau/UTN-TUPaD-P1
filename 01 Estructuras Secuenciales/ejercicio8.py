#8
"""Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente 
modo:"""

while True:

    altura = float(input("Ingrese su altura: "))

    if altura == 0:
        print("Programa terminado.")
        break

    peso = float(input("Ingrese su peso: "))

    if peso == 0:
        print("Programa terminado.")
        break

    imc = peso / (altura ** 2)

    print(f"Su masa índice de masa corporal(IMC) es: {imc:.2f}")

