# 8
"""Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
aparece ese dígito dentro del número. 
Ejemplos: 
contar_digito(12233421, 2)   → 3   
contar_digito(5555, 5)       → 4   
contar_digito(123456, 7)     → 0   """

def contar_digito(numero, digito):
    if numero < 10:     # Caso base: Si el num tiene un solo digito
        return 1 if numero == digito else 0
    
    # Caso recursivo: si el útlimo digito es igual, contar y continuar con el resto
    ultima_digito = numero % 10     # Extrae el útlimo digito
    return (
        1 if ultima_digito == digito
        else 0
    ) + contar_digito(numero // 10, digito)     # Elimina el último dígito

contar = int(input("Ingrese número: "))
veces = int(input("Ingrese el dígito a contar (0 a 9): "))

resultado = contar_digito(contar, veces)

print(f"El dígito {veces} aparece {resultado} vez/veces")