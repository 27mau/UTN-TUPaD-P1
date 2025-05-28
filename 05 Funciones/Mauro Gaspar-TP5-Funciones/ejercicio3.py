# 3
"""Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”.Pe
dir los datos al usuario y llamar a esta función con los valores in
gresados."""
# Definimos la función que recibe 4 parámetros.
def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"

# Pedimos al usuario los 4 datos.
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")
# Llamamos a la función con los datos ingresados.
informacion = informacion_personal(nombre, apellido, edad, residencia)
print(informacion)