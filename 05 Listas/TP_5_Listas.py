# NOTA: Siempre que se pida mostrar una lista o sus elementos, utilizar estructuras repetitivas.

# 1) Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.

# Creamos la lista.
#lista = [3, 4, 5, 2, 8, 6, 10, 9, 7, 8]

# Mostramos la lista por pantalla.
#print("Las notas son: ")
#for notas in lista:
#    print("#", notas)

# Calculamos y mostramos el promedio.
#suma = 0
#banderita = 0

#for numero in lista:
#    suma += numero
#    banderita += 1

#promedio = suma / banderita
#print("El promedio es: ", promedio)

# Calculamos y mostramos las notas.
#nota_mayor = lista[0]
#nota_menor = lista[0]

#for nota in lista:
#    if nota > nota_mayor:
#        nota_mayor = nota
#    if nota < nota_menor:
#        nota_menor = nota
    
#print(f"La nota mas alta es: {nota_mayor}\nLa nota mas baja es: {nota_menor}")


#2) Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

#Pedimos los valores
listaProductos = []
for i in range(5):
    producto = input(f"Ingrese el producto {i+1}: ")
    listaProductos.append(producto)

# Ordenamos y mostramos la lista alfabeticamente.
listaProductos = sorted(listaProductos)

print("\nLista de productos: ")

for prod in listaProductos:
    print(prod)

# Preguntamos que producto quiere eliminar.
borrar_producto = input("\nIngrese el producto que desea eleminiar: ")

if borrar_producto in listaProductos:
    listaProductos.remove(borrar_producto)
    print("\nLista actualizada:")
    for prod in listaProductos:
        print(prod)
else:
    print("El producto ingresado no esta en la lista")