"""
2.	Crear una tupla formada por 20 elementos numéricos. Mostrar:
	El número mayor.
	El número menor.
	La suma de todos los elementos.
	Los elementos ordenados.
	Cuantas veces se repite en la tupla, un número que solicitamos e ingresamos por teclado.
"""

nums = (100, 200, 5, 400, 900, 20, 200, 60, 15, 5,
        1, 700, 1000, 925, 0, 431, 90, 15, 30, 20)

# El numero mayor
print(f"El numero mayor de la tupla es: {max(nums)}")

# El numero menor
print(f"El numero menor de la tupla es: {min(nums)}")

# La suma de todos los elementos
print(f"La suma de todos los elementos es: {sum(nums)}")

# Elementos ordenados
print(f"Elementos ordenados: {sorted(nums)}")

# Repeticion de numero en la tupla, consultado por el usuario
numUser = int(input("Ingrese un numero: "))

for i in nums:
    if i == numUser:
        print(f"El numero {i} se encontro en la tupla, y se repite {nums.count(i)} veces.")
        exit()
