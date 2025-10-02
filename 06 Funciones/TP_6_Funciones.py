#Aclaracion: como no se piden validaciones en ningun momento, no gaste lineas en validar.

# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

def imprimir_hola_mundo():
    print("Hola mundo!")

# 2. Crear una función llamada saludar_usuario(nombre) 
# que reciba como parámetro un nombre y devuelva un saludo personalizado.

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

#3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: 
# “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

import math
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio


#5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. 
# Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    return segundos / 3600


#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.
import time
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}: ")
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")
        time.sleep(0.5)


# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y 
# devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por 0 kpo."
    return (suma, resta, multiplicacion, division)


# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). 
# Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    return peso / (altura ** 2)


#9. Crear una función llamada celsius_a_fahrenheit(celsius) que recibauna temperatura en grados Celsius 
# y devuelva su equivalente en Fahrenheit. 
# Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius):
        return (celsius * 9/5) + 32

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y 
# devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    return(a + b + c) / 3


#Llamada 1ra funcion:
#imprimir_hola_mundo()

#Llamada 2da funcionP:
#nombre_usuario = input("Ingrese su nombre: ")
#print(saludar_usuario(nombre_usuario))

#Llamada 3ra funcion:
#nombre = input("Ingrese su nombre: ")
#apellido = input("Ingrese su apellido: ")
#edad = input("Ingrese su edad: ")
#residencia = input("Ingrese su lugar de residencia: ")
#informacion_personal(nombre, apellido, edad, residencia)

#Llamada a la 4ta funcion:
#radio = float(input("Ingrese el radio para calcular area y perimetro: "))
#print(f"Area del circulo: {calcular_area_circulo(radio):.2f}")
#print(f"Perimetro del circulo: {calcular_perimetro_circulo(radio):.2f}")

#Llamada  al 5ta funcion:
#segundos = int(input("Ingrese la cantidad de segundos: "))
#print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos).2f} horas.")

#Llamada a las 6ta funcion:
#numero = int(input("Ingrese el nro para ver su tabla de multiplicar: "))
#tabla_multiplicar(numero)

#Llamamda a la 7ma funcion:
#a = float(input("Ingrese el primero numero: "))
#b = float(input("Ingrese el segundo numero: "))
#resultados = operaciones_basicas(a, b)
#print("╔═════════════════════╗")
#print("║ Operaciones basicas ║") #Bueno, bonito y claro.
#print("╚═════════════════════╝")
#print(f"Suma: {resultados[0]}")
#print(f"Resta: {resultados[1]}")
#print(f"Multiplicacion: {resultados[2]}")
#print(f"Division: {resultados[3]}")


#Llamada a la 8va funcion:
#peso = 0.0
#altura = 0.0
#peso = float(input("Ingrese el peso en kg: "))
#altura = float(input("Ingrese la altura en metros: "))
#print(f"El IMC es {calcular_imc:.2f}")

#Llamada a la 9na funcion:
#celsius = float(input("Ingrese la temperatura en numeros: "))
#print(f"{celsius}°c equivalen a {celsius_a_fahrenheit(celsius):.2f}°f")

#Llamada a la 10ma funcion:
a = float(input("Ingrese el 1er numero: "))
b = float(input("Ingrese el 2do numero: "))
c = float(input("Ingrese el 3er numero: "))
print(f"El promedio es: {calcular_promedio(a, b, c):.2f}")