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