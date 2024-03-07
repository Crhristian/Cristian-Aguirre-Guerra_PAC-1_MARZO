def calcular_descuento(categoria, precio):
    descuentos = {'Ferretería': 0.10, 'Aseo': 0.05, 'Seguridad': 0.15, 'Alimentos': 0.08, 'Electrodomésticos': 0.12}

    if categoria in descuentos:
        descuento = descuentos[categoria]
        precio_con_descuento = precio - (precio * descuento)
        return precio_con_descuento
    else:
        return precio

def main():
    categorias = {'Ferretería': 0, 'Aseo': 0, 'Seguridad': 0, 'Alimentos': 0, 'Electrodomésticos': 0}
    total_recaudado = 0

    print("Bienvenido a la tienda")

    while True:
        print("\nCategorías disponibles: Ferretería, Aseo, Seguridad, Alimentos, Electrodomésticos")
        categoria = input("Ingresa la categoría del producto (o escribe 'TERMINAR' para finalizar): ").capitalize()

        if categoria == 'Terminar':
            break

        if categoria in categorias:
            try:
                precio = float(input("Ingresa el precio del producto: "))
                if precio > 0:
                    precio_con_descuento = calcular_descuento(categoria, precio)
                    total_recaudado += precio_con_descuento
                    categorias[categoria] += 1

                    print(f"\nProducto añadido a la categoría {categoria}:")
                    print(f"Precio original: ${precio:.2f}")
                    print(f"Descuento aplicado: {calcular_descuento(categoria, precio) * 100:.2f}%")
                    print(f"Precio con descuento: ${precio_con_descuento:.2f}")
                else:
                    print("Por favor, ingresa un precio válido mayor que cero.")
            except ValueError:
                print("Por favor, ingresa un precio válido.")
        else:
            print("Categoría no válida. Por favor, elige una categoría existente.")

    print("\nResumen de compras:")
    for categoria, cantidad in categorias.items():
        print(f"{categoria}: {cantidad} productos")
    print(f"Total recaudado: ${total_recaudado:.2f}")

    print("\n¡Gracias por comprar en nuestra tienda!")

if __name__ == "__main__":
    main()
