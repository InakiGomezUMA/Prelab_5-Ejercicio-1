PRECIO_PAGINA = 2
LIMITE_INFERIOR = 1
LIMITE_SUPERIOR = 50
DESCUENTO = 100
TASA_DESCUENTO = 0.10


def calcular_subtotal(total_paginas, precio_pagina):
    return total_paginas * precio_pagina

def main():
    paquetes = ["Apuntes", "Guía de ejercicios", "Material de consulta"]
    paquetes_aceptados = 0
    total_paginas = 0

    for indice in range(len(paquetes)):
        nombre_paquete = paquetes[indice]
        entrada = input(f"Ingrese la cantidad de páginas para '{nombre_paquete}' "f"({LIMITE_INFERIOR}-{LIMITE_SUPERIOR}): ")

        try:
            paginas = int(entrada)

            if paginas < LIMITE_INFERIOR or paginas > LIMITE_SUPERIOR:
                print(
                    f"-> Error: '{nombre_paquete}' fuera de rango. Paquete omitido.")
                continue

            paquetes_aceptados += 1
            total_paginas += paginas
            print(f"-> Paquete '{nombre_paquete}' aceptado correctamente.")

        except ValueError:
            print(f"-> Error: Entrada no numérica para '{nombre_paquete}'. Paquete omitido.")
            continue

    if paquetes_aceptados == 0:
        print("No se aceptó ningún paquete. No se generó un pedido.")
        subtotal = 0.0
        descuento = 0.0
        total_pagar = 0.0
    else:
        subtotal = calcular_subtotal(total_paginas, PRECIO_PAGINA)

        if total_paginas > DESCUENTO:
            descuento = subtotal * TASA_DESCUENTO
        else:
            descuento = 0.0

        total_pagar = subtotal - descuento


    print(f"Cantidad de paquetes aceptados: {paquetes_aceptados}")
    print(f"Total de páginas aceptadas: {total_paginas}")
    print(f"Subtotal: {subtotal:.2f} unidades")
    print(f"Descuento aplicado (10%): {descuento:.2f} unidades")
    print(f"Total a pagar: {total_pagar:.2f} unidades")

if __name__ == "__main__":
    main()