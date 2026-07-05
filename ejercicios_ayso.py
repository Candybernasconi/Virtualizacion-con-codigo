# Ejercicio: manejo de listas
# Creo una lista con algunos numeros

numeros = [4, 8, 15, 16, 23, 42]

# Sumo todos los numeros de la lista
suma_total = sum(numeros)
print("La suma de los numeros es:", suma_total)

# Busco el numero mas grande
mayor = max(numeros)
print("El numero mas grande es:", mayor)

# Busco el numero mas chico
menor = min(numeros)
print("El numero mas chico es:", menor)

# Agrego un numero nuevo a la lista
numeros.append(100)
print("Lista despues de agregar un numero:", numeros)

# Elimino el primer numero de la lista
numeros.pop(0)
print("Lista despues de eliminar el primero:", numeros)

# Recorro la lista e imprimo cada numero
for n in numeros:
    print("Numero:", n)

# Ahora cuento cuantos numeros son pares
contador_pares = 0
for n in numeros:
    if n % 2 == 0:
        contador_pares += 1

print("Cantidad de numeros pares:", contador_pares)