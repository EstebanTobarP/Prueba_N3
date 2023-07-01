import numpy as np

residencial = [[' ' for _ in range(5)] for _ in range(4)]

lotes = [
    {'numero': '1', 'tamaño': '100 m2', 'precio': '$1,000,000'},
    {'numero': '2', 'tamaño': '150 m2', 'precio': '$1,500,000'},
    {'numero': '3', 'tamaño': '120 m2', 'precio': '$1,200,000'},
    {'numero': '4', 'tamaño': '200 m2', 'precio': '$2,000,000'}
]

clientes = []

def mostrar_disponibilidad_lotes():
    print("Lotes Disponibles:")
    for fila_idx, fila in enumerate(residencial, start=1):
        for col_idx, lote in enumerate(fila, start=1):
            if lote == ' ':
                print(f"[ ]", end="")
            else:
                print("[X]", end=" ")
        print()

def seleccionar_lote():
    rut = input("Ingrese su RUT: ")
    nombre = input("Ingrese su nombre completo: ")
    telefono = input("Ingrese su número de teléfono: ")
    email = input("Ingrese su dirección de correo electrónico: ")

    fila = int(input("Ingrese el número de fila del lote: "))
    columna = int(input("Ingrese el número de columna del lote: "))

    if fila < 1 or fila >= len(residencial) or columna < 1 or columna >= len(residencial[0]):
        print("Las coordenadas no son válidas, intente nuevamente.")
        return

    if residencial[fila - 1][columna - 1] == ' ':
        residencial[fila - 1][columna - 1] = 'X'
        clientes.append({'RUT': rut, 'Nombre': nombre, 'Teléfono': telefono, 'Email': email})
        print("Lote seleccionado!")
    else:
        print("El lote seleccionado no está disponible. Por favor, elija otro lote.")

def mostrar_detalles_lote():
    if len(clientes) == 0:
        print("No se han seleccionado lotes, por favor seleccione uno.")
        return

    cliente = clientes[-1]
    lote = lotes[len(clientes) - 1]

    print("Detalles del lote seleccionado:")
    print(f"Número de lote: {lote['numero']}")
    print(f"Tamaño del terreno: {lote['tamaño']}")
    print(f"Precio: {lote['precio']}")
    print(f"Cliente: {cliente['Nombre']}")
    print(f"RUT: {cliente['RUT']}")
    print(f"Teléfono: {cliente['Teléfono']}")
    print(f"Email: {cliente['Email']}")

def mostrar_clientes():
    if len(clientes) == 0:
        print("No hay clientes registrados.")
        return

    print("Clientes:")
    for cliente in clientes:
        print(f"Nombre: {cliente['Nombre']}")
        print(f"RUT: {cliente['RUT']}")
        print(f"Teléfono: {cliente['Teléfono']}")
        print(f"Email: {cliente['Email']}")
        print()

def main():
    while True:
        print("\n--- Bienvenido a LoteosDuoc ---")
        print("1. Ver disponibilidad de lotes")
        print("2. Seleccionar un lote")
        print("3. Ver detalles del lote seleccionado")
        print("4. Ver clientes")
        print("5. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            mostrar_disponibilidad_lotes()
        elif opcion == '2':
            seleccionar_lote()
        elif opcion == '3':
            mostrar_detalles_lote()
        elif opcion == '4':
            mostrar_clientes()
        elif opcion == '5':
            print("¡Muchas gracias! ¡Vuelva pronto.")
            break
        else:
            print("Opción incorrecta. Por favor, ingrese una opción correcta.")

main()