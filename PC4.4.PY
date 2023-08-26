#PC4 
#Mauro Pretto 
#Manejo de archivos 
#) 4

def guardar_tabla_multiplicar(n):
    with open(f"tabla-{n}.txt", "w") as f:
        for i in range(1, 11):
            f.write(f"{n} x {i} = {n * i}\n")

def mostrar_tabla_multiplicar(n):
    try:
        with open(f"tabla-{n}.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"El archivo tabla-{n}.txt no existe.")

def mostrar_linea_tabla_multiplicar(n, m):
    try:
        with open(f"tabla-{n}.txt", "r") as f:
            lineas = f.readlines()
            if m > len(lineas):
                print(f"La línea {m} no existe en el archivo tabla-{n}.txt.")
            else:
                print(lineas[m - 1])
    except FileNotFoundError:
        print(f"El archivo tabla-{n}.txt no existe.")

while True:
    print("1. Guardar tabla de multiplicar")
    print("2. Mostrar tabla de multiplicar")
    print("3. Mostrar línea de tabla de multiplicar")
    print("4. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        n = int(input("Ingrese un número entre 1 y 10: "))
        guardar_tabla_multiplicar(n)
        print(f"La tabla de multiplicar del número {n} se ha guardado en el archivo tabla-{n}.txt.")
    elif opcion == "2":
        n = int(input("Ingrese un número entre 1 y 10: "))
        mostrar_tabla_multiplicar(n)
    elif opcion == "3":
        n = int(input("Ingrese un número entre 1 y 10: "))
        m = int(input("Ingrese un número entre 1 y 10: "))
        mostrar_linea_tabla_multiplicar(n, m)
    elif opcion == "4":
        break
    else:
        print("Opción inválida.")


