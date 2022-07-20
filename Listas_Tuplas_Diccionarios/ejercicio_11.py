"""
11. Crear un diccionario que defina como llave el número de rut de una persona y como valor
un string con el nombre. Cargar los datos de 4 personas, listar el diccionario completo.
Realice una función que consulte el nombre de la persona introduciendo su rut.
"""

dicc = {
    '11.111.111-1': 'Claudio Perez',
    '22.222.222-2': 'Fernando Wazil',
    '33.333.333-3': 'Maca Ramos',
    '44.444.444-4': 'Katherine Cisterna'
    }

for i in dicc:
    print(f"Rut: {i}, Nombre: {dicc[i]}")

print("\n------------------------------------\n")


def getName(dni):
    if dni in dicc:
        print(f"El nombre de la persona es: {dicc[dni]}")


rut = input("Ingrese el rut de la persona a consultar: ")

getName(rut)




