# 6
"""escribir un programa que tome la lista 
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla."""

import statistics
import random
from statistics import mode, median, mean

num_aleatorios = [random.randint(1,100) for i in range(50)]

moda = statistics.mode(num_aleatorios)
mediana = statistics.median(num_aleatorios)
media = statistics.mean(num_aleatorios)


#print(f"Los números son: {num_aleatorios}")
print(f"La moda es: {moda}")
print(f"La mediana es: {mediana}")
print(f"La media es: {media}")

if media > mediana > moda:
    print("Sesgo positivo o a la derecha.")
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda.")
elif media == mediana == moda:
    print("Sin sesgo.")
else:
    print("Irregular.")