"""
9. Escribir un programa que encuentre los números comunes a dos tuplas.
"""

tupla1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
tupla2 = (2, 9, 6, 1, 100, 200, 300)

for i in tupla1:
    for j in tupla2:
        if i == j:
            print(f"Los numeros iguales son: Tupla_1: {i} y Tupla_2: {j}")
