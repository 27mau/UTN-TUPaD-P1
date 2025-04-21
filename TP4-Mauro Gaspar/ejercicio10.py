# 10
"""Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""

# Ingresar número entero y convertir a texto
num = int(input("Ingrese un número: "))

numero = str(abs(num))
# Guardar número invertido
num_invertido = ""

# Itera sobre cada caracter del número pasado a texto
for i in numero:
    # Agrega cada caracter al principio del texto invertido
    num_invertido = i + num_invertido

if num < 0:
    print(f"Número invertido: -{num_invertido}")
else:
    print(f"Número invertido: {num_invertido}")
