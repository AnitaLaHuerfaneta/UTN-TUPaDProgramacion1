#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Por favor, ingrese su edad: "))
if edad >= 18 :
    print("Es mayor de edad")
else :
    print("Es menor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

notaExamen = int(input("Por favor, ingrese su nota de examen: "))
if notaExamen >= 6 :
    print("Aprobado")
else :
    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

numero = int(input("Por favor ingrese un numero par: "))
if numero % 2 == 0 :
    print("Ha ingresado un número par.")
else :
    print("Por favor, ingrese un número par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad = int(input("Por favor, ingrese su edad: "))
if edad < 12 and edad >= 0 :
    print("Niño/a")
elif edad >= 12 and edad < 0 :
    print("Adolescent")
elif edad >= 18 and edad < 30 :
    print("Adulto/a joven")
elif edad >= 30 :
    print("Adulto/a joven")
else :
    print("Ingrese una edad valida")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string

password = str(input("Por favor, ingrese una contraseñas entre 8 y 14 caracteres: "))
if len(password) >= 8 and len(password) <= 14 :
    print("Ha ingresado una contraseña correcta") 
else :
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6)Escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range (50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda :
     print("Hay sesgo positivo")
elif media < mediana and mediana < moda :
     print("Hay sesgo negativo")
elif media == mediana and mediana == moda :
     print("No hay sesgo")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

frase = str(input("Ingrese una frase o palabra: "))
termina_Vocal = False
if len(frase) > 0 :
    ultima_Letra = frase[-1]
    if ultima_Letra in "aeiouAEIOU" :
        print(frase + "!")
    else :
        print(frase)
else :
    print("Frase invalida")

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Ingrese su nombre: ")
print("Elige una opcion para transformar tu nombre:")
print("1. Mayusculas")
print("2. Minusculas")
print("3. Primera letra en mayusculas")

opcion = input("Opcion: ")

#Aqui tambien podria poner (int(input) para recibir un entero 1,2 o 3 y facilitar abajo, pero nose que seria mejor)

if opcion == "1" :
    nombreFinal = nombre.upper()
elif opcion == "2" :
    nombreFinal = nombre.lower()
elif opcion == "3" :
    nombreFinal = nombre.title()
else :
    nombreFinal = "Opcion no valida"

print(nombreFinal)

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = float(input("Ingrese la magnitud del terremoto del 1 al 10: "))

if magnitud >= 0 and magnitud <= 10:
    if magnitud < 3 :
        print("Muy leve (imperceptible)")
    elif magnitud >= 3 and magnitud < 4:
        print("Leve (ligeramente perceptible)")
    elif magnitud >= 4 and magnitud < 5:
        print("Moderado(sentido por personas, pero generalmente no causa daños.)")
    elif magnitud >= 5 and magnitud < 6:
        print("Fuerte (puede causar daños en estructuras debiles)")
    elif magnitud >=6 and magnitud < 7:
        print("Muy fuerte (puede causar daños significativos)")
    elif magnitud >=7:
        print("Extremo (puede causar graves daños a gran escala)")
else:
    print("magnitud no valida")


#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("En que hemisferio se encuentra? N para norte y S para sur: ").upper()
mes = int(input("En que mes del 1 al 12 se encuentra?: "))
dia = int(input("En que dia del año se encuentra?: "))

#Tambien podria pedir el mes por nombre y pasarlo a numeros con condicionales pero se haria muy extenso.

if mes == 0 or mes > 12:
    print("Mes invalido")
elif dia == 0 or dia > 31:
    print("Dia invalido")
else:
    pass

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or mes in [1, 2] or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or mes in [4, 5] or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or mes in [7, 8] or (mes == 9 and dia <= 20):
        estacion = "Verano"
    else:
        estacion = "Otoño"

elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or mes in [1, 2] or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or mes in [4, 5] or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or mes in [7, 8] or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    else:
        estacion = "Primavera"
else:
    print("Hemisferio no válido")
    exit()

print("Usted se encuentra en", estacion)