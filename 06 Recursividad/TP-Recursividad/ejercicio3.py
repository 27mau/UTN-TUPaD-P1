# 3
"""Crea una función recursiva que calcule la potencia de un número base elevado a un 
exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
algoritmo general."""
# Función recusiva para calcular la potencia
def potencia(base, exponente):
    if exponente == 0:      # Caso base: cualquier numero elevado a 0 es 1
        return 1
    else: 
        return base * potencia(base, exponente - 1) # Paso recursivo

# Pedir base y exponente al usuario
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

# Llamada a la función
resultado = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es: {resultado}")