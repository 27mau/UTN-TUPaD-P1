# 1
"""Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función 
range."""

# Creo una lista vacía, para guardar todos los números que cumplan con la siguiente condición.
mi_lista = []

for i in list(range(1, 101)): # Crea un bucle que va a recorrer los números del 1 al 100 inclusive, 
                # y convierto eso en una lista, en cada vuelta, el número actual se guarda en la variable i
    if i % 4 == 0: # Verifica si i es divisible de 4
        mi_lista.append(i)  # Si i es múltiplo de 4, se agrega a la lista usando .append()

print(mi_lista)