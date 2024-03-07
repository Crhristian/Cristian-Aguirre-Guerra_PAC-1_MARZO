def convertir_temperatura(temperatura, escala):
    return (temperatura * 9/5) + 32 if escala == 'C' else (temperatura - 32) * 5/9 if escala == 'F' else None

while True:
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Finalizar")

    opcion = input("Selecciona una opción (1, 2, 3): ")

    if opcion == '3':
        print("Programa finalizado.")
        break

    try:
        temperatura = float(input("Ingresa la temperatura: "))
        escala = 'C' if opcion == '1' else 'F' if opcion == '2' else None

        if escala:
            print(f"{temperatura} grados {escala} son {convertir_temperatura(temperatura, escala)} grados {'F' if escala == 'C' else 'C'}.\n")
        else:
            print("Opción no válida. Por favor, elige 1, 2 o 3.\n")

    except ValueError:
        print("Por favor, ingresa una temperatura válida.\n")
