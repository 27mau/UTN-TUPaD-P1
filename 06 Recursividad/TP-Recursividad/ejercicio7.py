# 7
"""Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
último nivel con un solo bloque. 
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
pirámide."""
# Esta funcion implementa la suma de los primeros n números naturales
def contar_bloques(n):
    if n == 1:      # Caso base: si n es 1, solo se cuenta 1
        return 1
    return n + contar_bloques(n -1)     # Caso recursivo: se suma n con la cantidad de bloques del siguiente nivel

bloques = int(input("Ingrese número natural: "))
contar = contar_bloques(bloques)

print(f"Total de bloques: {contar}")
