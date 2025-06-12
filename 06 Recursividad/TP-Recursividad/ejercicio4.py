# 4
"""Crear una función recursiva en Python que reciba un número entero positivo en base 
decimal y devuelva su representación en binario como una cadena de texto."""
# Función que convierte un número decimal entero a binario
def decimal_binario(numero):
    if numero == 0:     # Caso base: si el num es 0 o 1, devuelve como cadena
        return "0"
    elif numero == 1:
        return "1"
    else:
        # Paso recursivo: dividimos el número por 2 y concatenamos el resto
        return decimal_binario(numero // 2) + str(numero % 2)

# Se pide al usuario un número entero positivo en decimal    
numero = int(input("Ingrese un número entero positivo en decimal: "))

# Llamamos al función
binario = decimal_binario(numero)
print(f"El número {numero} en binario es: {binario}")