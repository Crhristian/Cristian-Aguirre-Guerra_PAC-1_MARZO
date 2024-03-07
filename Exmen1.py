def contar_vocales(cadena):
    vocales = "aeiou"
    contador_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    for char in cadena:
        if char.lower() in vocales:
            contador_vocales[char.lower()] += 1

    return contador_vocales

def main():
    contador_total = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    while True:
        entrada = input("Ingresa una letra o escribe 'finalizar' para terminar: ")

        if entrada.lower() == 'finalizar':
            break
        elif entrada.isalpha() and len(entrada) == 1:
            resultados = contar_vocales(entrada)
            for vocal, cantidad in resultados.items():
                contador_total[vocal] += cantidad
            print("Cantidad de vocales hasta ahora:")
            for vocal, cantidad in contador_total.items():
                print(f"{vocal}: {cantidad}")
        else:
            print("Ingresa solo una letra válida.")

    print("Programa finalizado. Cantidad total de vocales:")
    for vocal, cantidad in contador_total.items():
        print(f"{vocal}: {cantidad}")

if __name__ == "__main__":
    main()