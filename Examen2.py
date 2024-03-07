def mostrar_tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")

    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def main():
    while True:
        try:
            entrada = int(input("Ingresa un número entero positivo: "))
            if entrada > 0:
                mostrar_tabla_multiplicar(entrada)
                break
            else:
                print("Por favor, ingresa un número entero positivo.")
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

if __name__ == "__main__":
    main()
