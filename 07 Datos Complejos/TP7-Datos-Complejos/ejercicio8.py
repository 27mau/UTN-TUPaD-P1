# 8
"""Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
Permití al usuario: 
• Consultar el stock de un producto ingresado. 
• Agregar unidades al stock si el producto ya existe. 
• Agregar un nuevo producto si no existe."""

# Diccionario inicial
stock_productos = {
    "manzanas": 10,
    "peras": 5,
    "naranjas": 8
}

# Pedimos al usuario el nombre del producto
producto = input("Ingresá el nombre del producto: ").lower()

# Verifica si el producto ya existe en el diccionario
if producto in stock_productos:
    print(f"Stock actual de {producto}: {stock_productos[producto]} unidades")

    # Pregunta si quiere agregar más unidades al stock
    agregar = input("Querés agregar unidades? (si/no): ").lower()
    if agregar == "si":
        cantidad = int(input("Cuántas unidades querés agregar?: "))
        stock_productos[producto] += cantidad
        print(f"Nuevo stock de {producto}: {stock_productos[producto]} unidades")

else:
    # Si el producto no existe, se agrega como nuevo
    print(f"{producto} no está en el stock.")
    nuevo = input("¿Querés agregarlo al inventario? (si/no): ").lower()
    if nuevo == "si":
        cantidad = int(input("Cuántas unidades querés agregar?: "))
        stock_productos[producto] = cantidad
        print(f"{producto} agregado con {cantidad} unidades.")

# Mostramos el stock actualizado completo
print("\nStock actual de todos los productos:")
for prod, unidades in stock_productos.items():
    print(f"{prod}: {unidades} unidades")
