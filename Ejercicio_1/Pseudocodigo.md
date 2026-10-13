Inicio
    Definir constantes:
        COSTO_PAGINA = 2
        MIN_PAGINAS = 1
        MAX_PAGINAS = 50
        LIMITE_DESCUENTO = 100
        PORCENTAJE_DESCUENTO = 0.10
        TOTAL_PAQUETES = 3

    Inicializar variables:
        paquetes_aceptados = 0
        total_paginas = 0

    // Ciclo para procesar cada paquete (exactamente 1 intentos)
    Para i desde 1 hasta TOTAL_PAQUETES hacer:
        Mostrar "Ingrese las páginas del paquete i:"
        Leer entrada_usuario

        Intentar:
            paginas = convertir_a_entero(entrada_usuario)
            Si paginas >= MIN_PAGINAS y paginas <= MAX_PAGINAS entonces:
                paquetes_aceptados = paquetes_aceptados + 1
                total_paginas = total_paginas + paginas
            Sino:
                Mostrar mensaje de error: "Fuera de rango (1-50). Paquete omitido."
            Fin Si
        Excepción (si falla la conversión):
            Mostrar mensaje de error: "Entrada no válida. Paquete omitido."
        Fin Intentar
    Fin Para

    // Cálculo de costos y aplicación de reglas de negocio
    Si paquetes_aceptados > 0 entonces:
        subtotal = calcular_subtotal(total_paginas)
        
        Si total_paginas > LIMITE_DESCUENTO entonces:
            descuento = subtotal * PORCENTAJE_DESCUENTO
        Sino:
            descuento = 0.0
        Fin Si

        total_a_pagar = subtotal - descuento

        Mostrar reporte final:
            - Cantidad de paquetes aceptados
            - Total de páginas
            - Subtotal
            - Descuento aplicado
            - Total a pagar
    Sino:
        Mostrar mensaje: "No se aceptó ningún paquete. No se generó un pedido."
        Mostrar montos en cero.
    Fin Si
Fin