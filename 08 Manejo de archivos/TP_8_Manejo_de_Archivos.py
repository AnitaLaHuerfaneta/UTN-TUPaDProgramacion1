# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
# formato: Producto: Lapicera | Precio: $120.5 | Cantidad: 30

# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente.

# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
# una lista llamada productos, donde cada elemento sea un diccionario con claves:
# nombre, precio, cantidad.
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        #Eliminamos espacios y saltos de lineas con strip()
        linea = linea.strip()

        #Separamos los datos por "," (Y hacemos el punto 4)
        nombre, precio, cantidad = linea.split(",")
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)

        #Imprimimos en el formato pedido
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

# Paso 3
print("\nAhora agreguemos uno nuevo.")
nombre = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio: "))
cantidad = int(input("Ingrese la cantidad: "))

# Y lo agregamos al archivo sin borrar lo existente.
with open("productos.txt", "a") as archivo:
    archivo.write(f"\n{nombre},{precio},{cantidad}")

print("Producto agregado.")

#Tambien a la lista.
productos.append({
    "nombre": nombre,
    "precio": precio,
    "cantidad": cantidad
})

# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error.

buscar = input("Ingrese el nombre del producto a buscar: ")

producto_existe = False
for p in productos:
    if p["nombre"].lower() == buscar.lower():
        print(f"Nombre: {p['nombre']}")
        print(f"Precio: ${p['precio']}")
        print(f"Cantidad: {p['cantidad']}")
        producto_existe = True
        break

if not producto_existe:
    print("El producto no existe en la lista.")

# 6. Guardar los productos actualizados:

with open("productos.txt", "w") as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
print("Archivo actualizaco correctamente.")