# 5
"""Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""
import random

# Genera un número aleatorio entre 0 y 9
numero_aleatorio = random.randint(0, 9)
intentos = 0

print("Adivina el número entre 0 y 9.")

# Creo un bulce infinito hasta que se adivine el número
while True:
    ingreso = int(input("Ingrese número: "))
    # Contamos los intentos realizados
    intentos += 1

    # Una vez adivinado el número cortamos con un break
    if ingreso == numero_aleatorio:
        print(f"Felicidades!! Adivinaste el número en {intentos} intento/s.")
        break

