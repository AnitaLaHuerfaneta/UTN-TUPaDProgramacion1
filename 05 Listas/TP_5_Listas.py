# NOTA: Siempre que se pida mostrar una lista o sus elementos, utilizar estructuras repetitivas.

# 1) Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.

# Creamos la lista.
lista = [3, 4, 5, 2, 8, 6, 10, 9, 7, 8]

# Mostramos la lista por pantalla.
print("Las notas son: ")
for notas in lista:
    print("#", notas)

# Calculamos y mostramos el promedio.
suma = 0
banderita = 0

for numero in lista:
    suma += numero
    banderita += 1

promedio = suma / banderita
print("El promedio es: ", promedio)

# Calculamos y mostramos las notas.
nota_mayor = lista[0]
nota_menor = lista[0]

for nota in lista:
    if nota > nota_mayor:
        nota_mayor = nota
    if nota < nota_menor:
        nota_menor = nota
    
print(f"La nota mas alta es: {nota_mayor}\nLa nota mas baja es: {nota_menor}")


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


# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.

#Improtamos los numeros y creamos las variables.
import random
lista = [random.randint(1, 100) for _ in range(15)]
pares = []
impares = []

for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
    else:
       impares.append(numero)

print("Los numeros pares son: ")
for n in pares:
    print(f":{n}")

print("\nLos numeros impares son: ")
for n in impares:
    print(f":{n}")


# 4) Dada una lista con valores repetidos:
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

datos_sin_duplicados = list(set(datos))
print("La lista sin duplicados es: ")
for contador in datos_sin_duplicados:
    print(f":{contador}")


# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.

estudiantes = ["Max", "Raul", "Nicholas", "Rulo", "Aleto", "Marian", "Dante", "Keke"]

opcion = input("¿Desea agregar (A) o eliminar (E) un estudiante? ").upper()

if opcion == "A":
    nuevo = input("Ingrese el nombre del estudiante a agregar: ")
    estudiantes.append(nuevo)

elif opcion == "E":
    eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
    else:
        print("Ese estudiante no está en la lista.")

else:
    print("Opción no válida.")

# Mostrar la lista final con estructura repetitiva
print("\nLista final de estudiantes:")
for est in estudiantes:
    print(est)


# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
# último pasa a ser el primero).

numeros = [10, 20, 30, 40, 50, 60, 70]

ultimo = numeros[-1]   
for i in range(len(numeros)-1, 0, -1): 
    numeros[i] = numeros[i-1]
numeros[0] = ultimo

print("Lista rotada:")
for num in numeros:
    print(num, end=" ")

#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana. 
# • Calcular el promedio de las mínimas y el de las máximas. 
# • Mostrar en qué día se registró la mayor amplitud térmica. 

# [min, max] por cada día
temperaturas = [
    [12, 20], [14, 25], [11, 23],
    [15, 27], [13, 24], [10, 22], [16, 28]
]

# Promedio mínimas y máximas
suma_min = 0
suma_max = 0
for t in temperaturas:
    suma_min += t[0]
    suma_max += t[1]

prom_min = suma_min / len(temperaturas)
prom_max = suma_max / len(temperaturas)

print("Promedio mínimas:", prom_min)
print("Promedio máximas:", prom_max)

# Mayor amplitud térmica (max - min)
mayor_amp = 0
dia_mayor_amp = 0
for i in range(len(temperaturas)):
    amplitud = temperaturas[i][1] - temperaturas[i][0]
    if amplitud > mayor_amp:
        mayor_amp = amplitud
        dia_mayor_amp = i + 1

print("Día con mayor amplitud térmica:", dia_mayor_amp, "(", mayor_amp, "°C )")

#8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 
# • Mostrar el promedio de cada estudiante. 
# • Mostrar el promedio de cada materia.

notas = [
    [7, 8, 6],
    [5, 6, 7],
    [9, 8, 10],
    [4, 5, 6],
    [8, 7, 9]
]

# Promedio por estudiante
for i in range(len(notas)):
    suma = 0
    for j in range(len(notas[i])):
        suma += notas[i][j]
    print(f"Promedio estudiante {i+1}: {suma/len(notas[i]):.2f}")

# Promedio por materia
for j in range(len(notas[0])):
    suma = 0
    for i in range(len(notas)):
        suma += notas[i][j]
    print(f"Promedio materia {j+1}: {suma/len(notas):.2f}")

#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
# • Inicializarlo con guiones "-" representando casillas vacías. 
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.

tablero = [["-" for _ in range(3)] for _ in range(3)]

def mostrar_tablero():
    for fila in tablero:
        for casilla in fila:
            print(casilla, end=" ")
        print()

# Juego simple de 2 turnos de ejemplo
for turno in range(2):
    jugador = "X" if turno % 2 == 0 else "O"
    print(f"Turno del jugador {jugador}")
    fila = int(input("Ingrese fila (0-2): "))
    col = int(input("Ingrese columna (0-2): "))
    if tablero[fila][col] == "-":
        tablero[fila][col] = jugador
    else:
        print("Casilla ocupada, pierde el turno.")
    mostrar_tablero()

#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
# • Mostrar el total vendido por cada producto. 
# • Mostrar el día con mayores ventas totales. 
# • Indicar cuál fue el producto más vendido en la semana.

ventas = [
    [5, 6, 7, 8, 4, 6, 7],   # Producto 1
    [3, 4, 2, 5, 3, 2, 4],   # Producto 2
    [8, 7, 9, 10, 6, 8, 9],  # Producto 3
    [2, 3, 4, 2, 3, 2, 3]    # Producto 4
]

# Total vendido por producto
for i in range(len(ventas)):
    total = 0
    for j in range(len(ventas[i])):
        total += ventas[i][j]
    print(f"Total producto {i+1}: {total}")

# Día con mayores ventas totales
mayor_dia = 0
suma_mayor = 0
for j in range(len(ventas[0])):  # días
    suma = 0
    for i in range(len(ventas)):  # productos
        suma += ventas[i][j]
    if suma > suma_mayor:
        suma_mayor = suma
        mayor_dia = j + 1
print("Día con mayores ventas:", mayor_dia, "(Total:", suma_mayor, ")")

# Producto más vendido en la semana
mas_vendido = 0
producto_max = 0
for i in range(len(ventas)):
    total = sum(ventas[i])
    if total > mas_vendido:
        mas_vendido = total
        producto_max = i + 1
print("Producto más vendido en la semana:", producto_max, "(Total:", mas_vendido, ")")