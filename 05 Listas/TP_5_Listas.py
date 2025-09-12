#1) Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.

notas = [7, 5, 8, 10, 6, 9, 4, 7, 8, 6]  #Agrego notas inventadas ya que no se especifica nada.

print("Notas:", notas)
promedio = sum(notas) / len(notas)

print(f"Promedio: {promedio:.2f}")
print(f"Nota mas alta: {max(notas)}")
print(f"Nota mas baja: {min(notas)}")


#2) Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos = []

for i in range(5):
    p = input(f"Ingrese el producto {i+1}: ")
    productos.append(p)

print("\nLista de productos:", productos)

productos_ordenados = sorted(productos)
print("Productos ordenados:", productos_ordenados)

eliminar = input("\n¿Que producto desea eliminar?: ")
if eliminar in productos_ordenados:
    productos_ordenados.remove(eliminar)
    print("Lista actualizada:", productos_ordenados)
else:
    print("Ese producto no esta en la lista.")


#3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.

import random

numeros = [random.randint(1, 100) for _ in range(15)]
print("Numeros generados:", numeros)

pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

print(f"\nLista de pares ({len(pares)}): {pares}")
print(f"Lista de impares ({len(impares)}): {impares}")


#4) Dada una lista con valores repetidos:
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.

# Lista de valores repetidos
valores = [1, 2, 2, 3, 4, 4, 5, 1, 6]

sin_repetidos = list(set(valores))

print("Lista original:", valores)
print("Lista sin repetidos:", sin_repetidos)


#5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.

estudiantes = ["Anita", "Luisito", "Martita", "Pedrito", "Carlita", "Juancito", "Raulito", "Jorgita"]

print("Lista actual:", estudiantes)

accion = input("¿Desea agregar o eliminar un estudiante? (a/e): ")

if accion == "a":
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
elif accion == "e":
    borrar = input("Ingrese el nombre del estudiante a eliminar: ")
    if borrar in estudiantes:
        estudiantes.remove(borrar)
    else:
        print("Ese estudiante no esta en la lista.")

print("Lista final:", estudiantes)


#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
# ltimo pasa a ser el primero).

numeros = [1, 2, 3, 4, 5, 6, 7]
print("Lista original:", numeros)

rotada = [numeros[-1]] + numeros[:-1]

print("Lista rotada:", rotada)


#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.

temperaturas = [
    [12, 20],
    [10, 18],
    [14, 22],
    [11, 19],
    [13, 25],
    [9,  17],
    [15, 24] 
]

minimas = [fila[0] for fila in temperaturas]
maximas = [fila[1] for fila in temperaturas]

prom_min = sum(minimas) / len(minimas)
prom_max = sum(maximas) / len(maximas)

print(f"Promedio minimas: {prom_min:.2f}")
print(f"Promedio maximas: {prom_max:.2f}")

amplitudes = [maxi - mini for mini, maxi in temperaturas]
dia_max = amplitudes.index(max(amplitudes)) + 1

print(f"El dia con mayor amplitud termica fue el dia {dia_max}")


#8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.

notas = [
    [7, 8, 6],
    [5, 9, 7],
    [10, 6, 8],
    [4, 7, 5],
    [8, 9, 10]
]

print("\nPromedio por estudiante:")
for i, fila in enumerate(notas):
    prom = sum(fila) / len(fila)
    print(f"Estudiante {i+1}: {prom:.2f}")

print("\nPromedio por materia:")
for j in range(len(notas[0])):
    columna = [notas[i][j] for i in range(len(notas))]
    prom = sum(columna) / len(columna)
    print(f"Materia {j+1}: {prom:.2f}")


#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.

tablero = [["-" for _ in range(3)] for _ in range(3)]

def mostrar_tablero():
    for fila in tablero:
        print(" ".join(fila))
    print()

mostrar_tablero()

for turno in range(4):
    jugador = "X" if turno % 2 == 0 else "O"
    print(f"Turno del jugador {jugador}")
    fila = int(input("Fila (0-2): "))
    col = int(input("Columna (0-2): "))
    if tablero[fila][col] == "-":
        tablero[fila][col] = jugador
    else:
        print("Casilla ocupada, pierde turno.")
    mostrar_tablero()

#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.

ventas = [
    [5, 8, 6, 4, 7, 3, 9],   # Producto 1
    [3, 6, 4, 8, 5, 7, 6],   # Producto 2
    [10, 12, 9, 11, 8, 7, 13], # Producto 3
    [2, 4, 3, 5, 6, 2, 4]    # Producto 4
]

print("Total por producto:")
totales_productos = []
for i, fila in enumerate(ventas):
    total = sum(fila)
    totales_productos.append(total)
    print(f"Producto {i+1}: {total}")

totales_dias = [sum(col) for col in zip(*ventas)]
dia_max = totales_dias.index(max(totales_dias)) + 1
print(f"\nEl dia con mayores ventas fue el dia {dia_max}")

producto_max = totales_productos.index(max(totales_productos)) + 1
print(f"El producto mas vendido en la semana fue el producto {producto_max}")
