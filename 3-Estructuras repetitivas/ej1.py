#Ejercicio 1



#4. Al final mostrar:
#o Total sin descuentos
#o Total con descuentos
#o Ahorro total
#o Promedio por producto (usar float y formatear con :.2f, ejem:
#x = 3.14159
#print(f"{x:.2f}"))

#1. Pedir nombre del cliente (solo letras, validar con .isalpha() en while).
while True:
    nombre_cliente = input("Nombre cliente: ")
    if nombre_cliente.isalpha():
        break
    print("Error: El nombre debe contener solo letras. Intente nuevamente.")

#2. Pedir cantidad de productos a comprar (número entero positivo, validar con
#.isdigit() en while).
while True:
    cantidad_productos = input("Ingrese la cantidad de productos: ")
    if cantidad_productos.isdigit() and int(cantidad_productos) > 0:
        cantidad_productos = int(cantidad_productos)
        break
    print("Error: La cantidad debe ser un número entero positivo. Intente nuevamente.")

#inicializamos vables
total_sin_descuentos = 0
total_con_descuentos = 0

#3. Por cada producto (usar for):
#o Pedir precio (entero, validar .isdigit()).
#o Pedir si tiene descuento S/N (validar con while, aceptar s o n en
#cualquier mayuscula/minuscula).
#o Si tiene descuento: aplicar 10% al precio de ese producto.

for productos in range(int(cantidad_productos)):
    while True:
        precio_producto = input(f"Ingrese el precio del producto {productos + 1}: ")
        if precio_producto.isdigit():
            precio_producto = int(precio_producto)
            break
        print("Error: El precio debe ser un número entero. Intente nuevamente.")

    while True:
        descuento = input(f"¿El producto {productos + 1} tiene descuento? (S/N): ").strip().lower()
        if descuento in ['s', 'n']:
            break
        print("Error: Debe ingresar 'S' para sí o 'N' para no. Intente nuevamente.")
        
    total_sin_descuentos += precio_producto

    if descuento == 's':
        precio_producto *= 0.9  # Aplicar 10% de descuento
    total_con_descuentos += precio_producto

ahorro_total = total_sin_descuentos - total_con_descuentos
promedio_por_producto = total_con_descuentos / cantidad_productos

print("------------------------------------------------")
print(f"Total sin descuentos: {total_sin_descuentos}")
print(f"Total con descuentos: {total_con_descuentos}")
print(f"Ahorro total: {ahorro_total}")
print(f"Promedio por producto: {promedio_por_producto:.2f}")

    

