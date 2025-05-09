#6
"""Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
multiplicar de dicho número."""

while True:
    
    numero = int(input("Ingrese un número para ver su tabla: "))

    if numero == 0:
        break

    print(f"La tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    print("\n")
