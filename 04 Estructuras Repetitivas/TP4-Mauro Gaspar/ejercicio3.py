# 3
""" Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
dados por el usuario, excluyendo esos dos valores."""

num1 = int(input("Ingrese primer número: "))
num2 = int(input("Ingrese segundo número: "))

suma = 0

# Ordenar los números ingresados de menor a mayor
if num1 > num2:
    primero = num2
    segundo = num1
else:
    primero = num1
    segundo = num2

# Genera una secuencia del "primer" número y termina en "segundo" y sumamos cada número que hay dentro del rango 
for i in range(primero + 1, segundo):
    suma += i

print(f"La suma de los números entre {primero} y {segundo} es: {suma}")