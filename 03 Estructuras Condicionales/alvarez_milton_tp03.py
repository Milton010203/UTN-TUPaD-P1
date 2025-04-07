import random
from statistics import mode, median, mean
#Actividad 1
print("- " * 50)
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Usted es mayor de edad")
else:
    print("Usted no es mayor de edad")

#Actividad 2
print("- " * 50)
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("APROBADO")
else:
    print("DESAPROBADO")

#Actividad 3
print("- " * 50)
num = int(input("Ingrese un numero par: "))
if num % 2 == 1:
    print("Ingrese un numero par!")
else:
    print("Perfecto!")

#Actividad 4
print("- " * 50)
edad1 = int(input("Ingrese su edad: "))
if 0 <= edad <= 11:
    print("Usted es un niño")
elif 12 <= edad <= 17:
    print("Usted es un adolescente")
elif 18 <= edad <= 29:
    print("Usted es un adulto joven")
else:
    print("Usted es un adulto")

#Actividad 5
pww = input("Ingrese una contraseña entre 8 y 14 caracteres: ")
tam = len(pww)
if 8 <= tam <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña entre 8 y 14 caracteres")

#Actividad 6
numeros_aleatorios = [random.randint(1, 100) for i in range (50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
if media > mediana and mediana > moda:
    print("Hay sesgo positivo")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo")
else:
    print("No hay sesgo")

#Actividad 7
cadena = input("Ingrese un texto: ")
ultima_letra = cadena[-1].lower()
if ultima_letra in "aeiou":
    cadena += "!"
    print(cadena)
else:
    print(cadena)

#Actividad 8
nombre = str(input("Ingrese su nombre: "))
opcion = int(input("Ingrese una opcion:" \
"1. Su nombre en MAYUSCULAS" \
"2. Su nombre en minusculas" \
"3. Su nombre con la primera letra en Mayuscula"))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())

#Actividad 9
terremoto = float(input("Ingrese la magnitud de el terremoto: "))
if terremoto < 3:
    print("Segun la escala de ritcher, el terremoto es MUY LEVE")
elif 3 <= terremoto < 4:
    print("Segun la escala de ritcher, el terremoto es LEVE")
elif 4 <= terremoto < 5: 
    print("Segun la escala de ritcher, el terremoto es MODERADO")
elif 5 <= terremoto < 6:
    print("Segun la escala de ritcher, el terremoto es FUERTE")
elif 6 <= terremoto < 7:
    print("Segun la escala de ritcher, el terremoto es MUY FUERTE")
else:
    print("Segun la escala de ritcher, el terremoto es EXTREMO")

#Actividad 10
hemisferio = str(input("Ingrese en que hemisferio se encuentra, N para Norte y S para Sur: "))
mes = int(input("Ingrese el mes: "))
dia = int(input("Ingrese el dia: "))

if (mes == 12 and dia >= 21) or mes in (1, 2) or (mes == 3 and dia <= 20):
    if hemisferio == "N":
        print("Es invierno en el hemisferio norte")
    elif hemisferio == "S":
        print("Es Verano en el hemisferio sur")
elif (mes == 3 and dia >= 21) or mes in (4, 5) or (mes == 6 and dia <= 20):
    if hemisferio == "N":
        print("Es Primavera en el hemisferio norte")
    elif hemisferio == "S":
        print("Es Otoño en el hemisferio sur")
elif (mes == 6 and dia >= 21) or mes in (7, 8) or (mes == 9 and dia <= 20):
    if hemisferio == "N":
        print("Es Verano en el hemisferio norte")
    elif hemisferio == "S":
        print("Es Invierno en el hemisferio sur")
elif (mes == 9 and dia >= 21) or mes in (10, 11) or (mes == 12 and dia <= 20):
    if hemisferio == "N":
        print("Es Otoño en el hemisferio norte")
    elif hemisferio == "S":
        print("Es Primavera en el hemisferio sur")
else:
    print("Ingrese una opcion valida")
