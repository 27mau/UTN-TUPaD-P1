# 10
""" Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
diccionario donde: 
• Las capitales sean las claves. 
• Los países sean los valores."""

# Diccionario: país -> capital
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Alemania": "Berlín",
    "Inglaterra": "Londres",
    "Perú": "Lima",
    "Uruguay": "Montevideo"
}

# Crea diccionario vacío para invertir los datos
capitales_paises = {}

# Recorre cada diccionario original
for pais, capital in paises_capitales.items():
    # Guarda la capital como clave y el país como valor
    capitales_paises[capital] = pais

# Muestra el nuevo diccionario invertido
print("Diccionario invertido (capital -> país):")
print(capitales_paises)
