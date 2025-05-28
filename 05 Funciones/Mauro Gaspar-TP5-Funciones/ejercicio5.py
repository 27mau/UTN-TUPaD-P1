# 5
"""Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mos
trar el resultado usando esta función."""
# Definimos la función segundos a horas.
def segundos_a_horas(segundos):
    hora = 3600 # 1 hora es igual a 3600 segundos.
    return segundos / hora

# Usuario ingresa los segundos.
ingresar_segundos = float(input("Ingrese candidad de segundos: "))

# Llamamos a la función y mostramos el resultado.
horas = segundos_a_horas(ingresar_segundos)
print(f"Los segundos ingresados equivalen a {horas:.2f} horas.")