# 2
"""Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
dígitos que contiene."""

num = int(input("Ingrese un número entero: "))

# abs() obtiene el valor absoluto del número, eliminando signno negativo.
# str() conviert el valor absoluto a una cadena.
# len() calcula la longitud de la cadena
longitud = len(str(abs(num)))

print(f"El número {num} tiene {longitud} cifra/s.")