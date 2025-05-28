# 2
"""Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
volver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario."""
# Definimos la función
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Se le pide al usuario ingresar un nombre
ingresar_nombre = input("Cuál es tu nombre? ")
# Llamamos a la función con ese nombre, que se guarda el resultado en la variable saludo.
saludo = saludar_usuario(ingresar_nombre)
print(saludo)