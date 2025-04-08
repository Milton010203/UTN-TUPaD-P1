import random
from statistics import mean

# Actividad 1
contador1 = 0
for a in range(0,101):
    print(contador1)
    contador1 += 1

# Actividad 2
num1 = int(input("Ingrese un numero entero"))
digitos2= 0
for b in str(num1):
    digitos2 += 1
print(f"El numero contiene {digitos2} digitos")


# Actividad 3
valor1_1 = int(input("Ingrese el primer valor: "))
valor1_2 = int(input("Ingrese el segundo valor: "))
acumulador3 = 0
for c in range((valor1_1 + 1), valor1_2):
    acumulador3 += c
print(f"La suma de todos los numeros da {acumulador3}")

# Actividad 4
acumulador4 = 0
num4 = -1
while num4 != 0:
    num4 = int(input("Ingrese un numero para sumar" \
    "Ingrese 0 para terminar la suma y mostrar el resultado"))
    acumulador4 += num4
print(f"La suma da {acumulador4}")

# Actividad 5
contador5 = 0
numero_5 = random.randint(0, 9)
eleccion5 = -1
while eleccion5 != numero_5:
    contador5 += 1
    eleccion5 = int(input("Adivine el numero del 0 al 9!: "))
    if eleccion5 != numero_5:
        print("Numero equivocado, intente de nuevo!")
print(f"Fueron necesarios {contador5} intentos para adivinar el numero")

# Actividad 6
for d in range(100, 0, -1):
    if d % 2 == 0:
        print(d)

# Actividad 7
numero_7 = int(input("Ingrese un numero: "))
acumulado_7 = 0
for e in range(0, numero_7):
    acumulado_7 += e
print(f"La suma de todos los numeros comprendidos entre el 0 y el {numero_7} da {acumulado_7}")

# Actividad 8
ct_pares8 = 0
ct_impares8 = 0
ct_positivos8 = 0
ct_negativos8 = 0
for f in range(0, 100):
    numero_8 = int(input("Ingrese un numero: "))
    if numero_8 % 2 == 0:
        ct_pares8 += 1
    else:
        ct_impares8 += 1
    if numero_8 >= 0:
        ct_positivos8 += 1
    else:
        ct_negativos8 += 1
print(f"Hubieron {ct_pares8} numeros pares y {ct_impares8} impares")
print(f"Hubieron {ct_positivos8} numeros positivos y {ct_negativos8} negativos")

# Actividad 9
lista09 = []
for g in range(0, 100):
    numero_9 = int(input("Ingrese un numero: "))
    lista09.append(numero_9)
media09 = mean(lista09)
print(f"La media de los numeros ingresados es de {media09}")

# Actividad 10
rango = 0
inversion_09 = []
cadena = str(input("Ingrese un numero: "))
for h in cadena:
    rango -= 1
    inversion_09.append(cadena[rango])
print(inversion_09)

