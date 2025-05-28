# 10
""" Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos: 
● Posición lista_anidada[0]: 15 
● Posición lista_anidada[1]: True 
● Posición lista_anidada[2][0]: 25.5 
● Posición lista_anidada[2][1]: 57.9 
● Posición lista_anidada[2][2]: 30.6 
● Posición lista_anidada[3]: False 
Imprimir la lista resultante por pantalla."""

lista_anidad = []

lista_anidad.append(15)

# Agregamos los elementos en un lugar específico con .insert(). 
# El primero elemento es el índice
lista_anidad.insert(1, True)
lista_anidad.insert(2, [25.5, 57.9, 30.6])
lista_anidad.insert(3, False)

print(lista_anidad)