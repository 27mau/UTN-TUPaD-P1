# 10
"""Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
si el usuario se encuentra en otoño, invierno, primavera o verano."""

hemisferio = input("En cuál hemisferio se encuentra ('N' para Norte y 'S' para Sur)?: ").lower()

mes = input("Qué mes del año es?: ").lower()

dia = int(input("Qué día del mes es?: "))

# Convertimos los meses a año
if mes == "enero":
    mes_num = 1
elif mes == "febrero":
    mes_num = 2
elif mes == "marzo":
    mes_num = 3
elif mes == "abril":
    mes_num = 4
elif mes == "mayo":
    mes_num = 5
elif mes == "junio":
    mes_num = 6
elif mes == "julio":
    mes_num = 7
elif mes == "agosto":
    mes_num = 8
elif mes == "septiembre":
    mes_num = 9
elif mes == "octubre":
    mes_num = 10
elif mes == "noviembre":
    mes_num = 11
elif mes == "diciembre":
    mes_num = 12
else:
    print("Dato ingresado incorrecto.")
    

# Determinamos la estación
if hemisferio == "n":
    if (mes_num == 3 and dia >= 21) or (mes_num == 4) or (mes_num == 5) or (mes_num == 6 and dia <= 20):
        print("Estás en Primavera.")
    elif (mes_num == 6 and dia >= 21) or (mes_num == 7) or (mes_num == 8) or (mes_num == 9 and dia <= 22):
        print("Estás en Verano.")
    elif (mes_num == 9 and dia >= 23) or (mes_num == 10) or (mes_num == 11) or (mes_num == 12 and dia <= 20):
        print("Estás en Otoño.")
    else:
        print("Estás en Invierno.")
elif hemisferio == "s":
    if (mes_num == 3 and dia >= 21) or (mes_num == 4) or (mes_num == 5) or (mes_num == 6 and dia <= 20):
        print("Estás en Otoño.")
    elif (mes_num == 6 and dia >= 21) or (mes_num == 7) or (mes_num == 8) or (mes_num == 9 and dia <= 22):
        print("Estás en Invierno.")
    elif (mes_num == 9 and dia >= 23) or (mes_num == 10) or (mes_num == 11) or (mes_num == 12 and dia <= 20):
        print("Estás en Primavera.")
    else:
        print("Estás en Verano.")
else:
    print("Dato ingresado incorrecto.")