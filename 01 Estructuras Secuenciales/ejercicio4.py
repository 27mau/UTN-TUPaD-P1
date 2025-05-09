#4
""" Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
su perímetro."""

radio = float(input("Ingrese el radio de un círculo: "))
pi = 3.1415

# calculamos el área
area = pi * (radio ** 2)
perimetro = 2 * pi * radio

print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")