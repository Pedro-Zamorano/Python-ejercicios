"""
10. Cree un diccionario que la clave sea los nombres en español y el valor, el equivalente del
nombre en inglés. Añada un INPUT que solicite un nombre en español y la salida sea el
nombre en inglés.
"""

dicc = {'rojo': 'red',
        'azul': 'blue',
        'morado': 'purple',
        'negro': 'black'}

getName = input("Ingrese un color en español: ")


if getName in dicc:
    print(f"El color es: {dicc[getName]}")
else:
    print("Color no encontrado")

