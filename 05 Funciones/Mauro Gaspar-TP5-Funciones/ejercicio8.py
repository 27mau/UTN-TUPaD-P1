# 8
"""Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
ción para mostrar el resultado con dos decimales."""
# Definimos la función para calcular el peso.
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Ingresa el peso y la altura.
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en m: "))

# Llama a la función y guarda en la variable para luego imprimir.
imc = calcular_imc(peso, altura)
print(f"Su índice de masa corporta(IMC) es: {imc:.2f}")