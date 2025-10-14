# 1) Dado el diccionario precios_frutas

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melon': 3000, 'Uva': 1450}

# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300


# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melon = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800



# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.

lista_precios_frutas = [precios_frutas.keys()] #Usamos "nombre_diccionario".keys() para recuperar las frutas.
print(lista_precios_frutas)


# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

#Creamos el diccionario vacio.
contactos = {}

# Pedimos y cargamos los 5 contactos con bucle for.
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese le numero telefonico de {nombre}: ")
    contactos[nombre] = numero

print("\nContactos agregados correctamente\n")

#Consultar contactos.
nombre_buscar = input("Ingrese el nombre del contacto que desea consultar: ")

if nombre_buscar in contactos:
    print(f"El numero de {nombre_buscar} es: {contactos[nombre_buscar]}")
else:
    print("Ese nombre no esta agendado.")

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ")

# Separamos las palabras por espacios
palabras = frase.split()

# Creamos un conjunto con las palabras unicas
palabras_unicas = set(palabras)

# Creamos un diccionario para contar cuantas veces aparece cada palabra
contador = {}

for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1

print("\nPalabras unicas:", palabras_unicas)
print("Recuento:", contador)

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

alumnos = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno nro {i+1}: ")
    
    notas = input(f"Ingrese las 3 notas de {nombre} separadas por espacios: ")
#Aca se traba un poco pero convertimos a una tupla de enteros.
    notas = tuple(map(int, notas.split()))
#Y guardamos en el diccionario.
    alumnos[nombre] = notas

#Calculamos y mostramos el promedio.
print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")


#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial_1 = {1, 2, 3, 4, 5}
parcial_2 = {4, 5, 6, 7, 8}

#Usamos interseccion.
ambos = parcial_1 & parcial_2
#Usamos diferencia simetrica.
solo_uno = parcial_1 ^ parcial_2
#Usamos union.
al_menos_uno = parcial_1 | parcial_2

#Mostramos.
print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)


# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

productos = {
    "manzanas": 10,
    "peras": 5,
    "bananas": 8
}

producto = input("Ingrese el nombre del producto que desea consultar: ").lower()

if producto in productos:
    print(f"Stock actual de {producto}: {productos[producto]}")
    agregar = input("¿Desea agregar unidades a este producto? (s/n): ").lower()
    
    if agregar == "s":
        cantidad = int(input("Ingrese cuantas unidades desea agregar: "))
        productos[producto] += cantidad
        print(f"Nuevo stock de {producto}: {productos[producto]}")
    else:
        print("No se modifico el stock.")
else:
    print("El producto no existe. Se agregara uno nuevo.")
    cantidad = int(input("Ingrese el stock inicial del nuevo producto: "))
    productos[producto] = cantidad
    print(f"Producto agregado: {producto} con stock de {cantidad} unidades.")

print("\nStock actualizado:", productos)


# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.

agenda = {
    ("lunes", "10:00"): "Comprar facturas",
    ("martes", "15:00"): "Llamar al mecanico",
    ("miercoles", "09:30"): "Ir al gym"
}

dia = input("Ingrese el dia: ").lower()
hora = input("Ingrese la hora (formato hh:mm): ")

# Buscar la clave (tupla)
clave = (dia, hora)

if clave in agenda:
    print(f"Actividad programada: {agenda[clave]}")
else:
    print("No hay ninguna actividad programada en ese dia y hora.")


# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asuncion"
}

# Creamos el nuevo diccionario invertido.
invertido = {capital: pais for pais, capital in original.items()}

# Mostramos ambos diccionarios.
print("Diccionario original:", original)
print("Diccionario invertido:", invertido)