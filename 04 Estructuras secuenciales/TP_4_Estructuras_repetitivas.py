#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

cont = 0
for cont in range(0, 101):
    print(cont)
    cont += 1


#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

num1 = int(input("Ingrese un numero entero: "))
cantDigit = len(str(abs(num1)))
print(f"El numero ingresado tiene {cantDigit} digitos")


#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Por favor ingrese el 1er nro: "))
num2 = int(input("Por favor ingrese el 2do nro: "))

if num1 > num2:
    num1, num2 = num2, num1

suma = 0
for i in range(num1 + 1, num2):
    suma += i #Suma = suma + i

print(f"La suma de los numeros entre {num1} y {num2} es: {suma}")


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

suma = 0
numeroIngresado = int(input("Ingrese numeros para ir sumandolos, 0 para terminar: "))
while numeroIngresado != 0:
    suma += numeroIngresado
    numeroIngresado = int(input(": "))
else:
    print(f"El total acumulado es: {suma}")


#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
print("Hora de intentar adivinar el nro")
num1 = 10 
contador = 0
numAzar = random.randint(0, 9)
while num1 != numAzar:
    num1 = int(input(": "))
    contador += 1
print(f"Felicitaciones, te tomo solo {contador} intentos")


#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100, -1, -2):
    print(i)


#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

num1 = int(input("Ingrese un nro: "))
suma = 0

for i in range(0, num1): #No agrego el numero ingresado por el usuario en la suma porque leyendo al consigna entiendo que "Solo los comprendidos entre"
    suma += i
print(f"La suma de todos los nros entre 0 y {num1} es {suma}")


#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

ponerCien = 10
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(ponerCien):
    num = int(input(f"{i}: ")) #Entiendo que podria usar "int(input(f"{i+1}: "))" para que el contador arranque 1 sea mas prolijo, pero creo que vscode no lo esta tomando bien.
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")


#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

ponerCien = 10
suma = 0

print(f"Ingrese {ponerCien} numeros enteros: ")

for i in range(ponerCien):
    num = int(input(f"Numero {i+1}: "))
    suma += num

media = suma / ponerCien
print(f"La media de los {ponerCien} numeros es: {media}")


#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num1 = input("Ingrese un numero entero: ")

invertido = num1[::-1]
print(f"El nuemero ingresado invertido es {invertido}")
