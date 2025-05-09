#5
"""Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
cuántas horas equivale."""
while True:

    segundos = int(input("Ingrese una cantidad de segundos('0' para terminar): "))
    hora = segundos / 60 / 60

    if segundos == 0:
        break

    print(f"La cantidad de segundos equivale a {hora:.1f} hora/s.")