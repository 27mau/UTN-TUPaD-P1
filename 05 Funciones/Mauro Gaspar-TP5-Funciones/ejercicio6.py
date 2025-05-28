# 6
"""Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la fun
ción."""
# Definimos la función de multiplicar.
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):  # El bucle for recorre los valores del 1 al 10 y mostrar el producto.
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Ingresa el número y llama a la función
numero = int(input("Ingrese un número para ver su tabla de multiplicación: "))
tabla_multiplicar(numero)