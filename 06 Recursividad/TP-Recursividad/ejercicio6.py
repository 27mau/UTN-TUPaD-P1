# 6
"""
Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
número entero positivo y devuelva la suma de todos sus dígitos. 
Restricciones: 
No se puede convertir el número a string. 
Usá operaciones matemáticas (%, //) y recursión. 
Ejemplos: 
suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
suma_digitos(9)      → 9 
suma_digitos(305)    → 8   (3 + 0 + 5) 
"""

def suma_digitos(n):
    if n < 10:      # Caso base: si el número es menor a 10, reotrna el propio número
        return n
    return (n % 10) + suma_digitos(n // 10)  # Caso recursivo, sumar el útlimo dígito
                                            #  al resultado de la llamada recursiva con el resto del número

numero = int(input("Ingrese un número natural: "))

resultado = suma_digitos(numero)

print(f"Suma de los dígitos ingresados: {resultado}")