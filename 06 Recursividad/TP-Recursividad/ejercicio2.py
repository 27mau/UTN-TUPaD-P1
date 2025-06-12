# 2
"""Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
especifique."""
# Función recursiva de fibonacci
def fibonacci_recursivo(posicion):
    if posicion == 0:   # Caso base: 0 es 0
        return 0
    elif posicion == 1:
        return 1        # Caso base: 1 es 1
    else: 
        return fibonacci_recursivo(posicion - 1) + fibonacci_recursivo(posicion - 2)

# Usuario ingresa una posición hasta dónde mostrar la serie Fibo
posicion = int(input("Ingresa la posición (número entero positivo): "))

# Muesta la serie de Fibo hasta la posición ingresada
print(f"Serie de Fibonacci hasta la posición {posicion}: ")

for i in range(posicion):
    print(fibonacci_recursivo(i), end=" ")  # Muestra cada número en una sola línea separada