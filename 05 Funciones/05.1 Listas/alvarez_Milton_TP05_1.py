# Actividad 1
lista01 = []
for a in range(0, 101):
    if a % 4 == 0:
        lista01.append(a)

# Actividad 2
lista02 = ["Milton", "Lautaro", "Mario", "Rosa", "Matias"]
print(lista02[-2])

# Actividad 3
lista03 = []
lista03.append("Primero")
lista03.append("Segundo")
lista03.append("Tercero")
print(lista03)

# Actividad 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

# Actividad 5
# En esta actividad se remueve de la lista el mayor de los numeros.
# Se asegura que es el mayor porque se utiliza la funcion 'max' en relacion a la lista numeros


# Actividad 6
ct6 = 0
lista06 = []
for b in range(10, 31, 5):
    ct6 += 1
    if ct6 < 3:
        print(b)
    lista06.append(b)

# Actividad 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "amarok"
autos[2] = "taos"

# Actividad 8
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)


# Actividad 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove(compras[0][0])
print(compras)

# Actividad 10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)