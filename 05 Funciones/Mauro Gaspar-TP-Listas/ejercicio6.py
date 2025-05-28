# 6
"""Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por 
pantalla los dos primeros."""

# Se crea una lista vacía
mi_lista = []

# Se usa un for que genera números desde el 10 hasta el 30, de 5 en 5.
for i in list(range(10, 31, 5)):
    mi_lista.append(i) # Cada número generado se va guardando a mi_lista

print(mi_lista[:2]) # [:2] significa, desde el inicio hasta el índice 2 (sin incluir)