# 4
""" Escribí un programa que permita almacenar y consultar números telefónicos. 
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
• Luego, pedí un nombre y mostrale el número asociado, si existe."""

# Diccionario vacío
contactos = {}
# Carga no más de 5 contactos
for i in range(5):

    nombre = input("Ingrese el nombre del contacto: ")

    numero = input(f"Ingrese nº de teléfono: ")
    contactos[nombre] = numero      # Se guarda en el diccionario

nombre_consulta = input("Ingrese el nombre que desea buscar: ")

# Si existe el nombre en el diccionario, muestra el número y si no, muestra contacto no encontrado.
if nombre_consulta in contactos:
    print("Número: ", contactos[nombre_consulta])
else:
    print("Contacto no encontrado.")
