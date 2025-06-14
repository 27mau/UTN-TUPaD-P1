# 9
"""Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos."""

# Agenda vacía
agenda = {}

# Agregar eventos a la agenda
agenda[("Lunes", "10:00")] = "Ir de compras"
agenda[("Martes", "13:00")] = "Reunión laboral"
agenda[("Miércoles", "14:30")] = "Clase de Informática"
agenda[("Viernes", "18:00")] = "Natación"


print("Agenda completa:")
# Con el bucle recorre cada entrada del diccionario
for clave, evento in agenda.items():    # Devuelve una lista de pares (clave, valor) del diccionario
    dia, hora = clave # se desempaqueta la tupla en sus dos partes, dia y hora.
    print(f"{dia} a las {hora}: {evento}")

def consultar_evento():
    print("CONSULTAR EVENTO EN LA AGENDA")
    dia = input("Ingresá el día: ")
    hora = input("Ingresá la hora (ej: 09:00): ")

    consulta = (dia, hora)
    # Verifica si esa clave existe en el diccionario
    if consulta in agenda:      # si no existe, muestra un mensaje diciendo que no hay nada agendado 
        print(f"\nEvento agendado el {consulta[0]} a las {consulta[1]}: {agenda[consulta]}")
    else:
        print("\nNo hay eventos agendados en ese horario.")

consultar_evento()
