"""
https://www.youtube.com/watch?v=JohZzRRGVAM
6. Escribir un programa que ordene una lista de números sin usar la función sort().
"""

numbers = [10, 6, 2, 8, 7, 3, 1, 5, 9, 4]

for i in range(1, len(numbers)):
    for j in range(len(numbers) - i):
        if numbers[j] > numbers[j+1]:
            temp = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = temp

print(numbers)
