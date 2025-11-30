opcion = 0

while opcion != 4:
    print("1. Saludar")
    print("2. Sumar dos números")
    print("3. Mostrar un mensaje")
    print("4. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        print("¡Hola! ¿Cómo estás?")
    
    elif opcion == 2:
        a = int(input("Ingresa el primer número: "))
        b = int(input("Ingresa el segundo número: "))
        print(f"La suma es: {a + b}")

    elif opcion == 3:
        print("Este es un mensaje de ejemplo.")

    elif opcion == 4:
        print("Saliendo del programa")

    else:
        print("Opción no válida, intenta de nuevo.")
