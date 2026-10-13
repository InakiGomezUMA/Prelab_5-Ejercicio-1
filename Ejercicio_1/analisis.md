Entrada:
La persona debe de indicar la cantidad de paginas por cada uno de los paquetes y los paquetes pueden incluir de 1 a 50 paginas.

Salidas:
La cantidad de paquetes debe estar formado por numeros enteros.
Las paginas totales deben ser enteros
Subtotal: Tipo real/decimal (total de páginas multiplicado por 2 unidades monetarias).
El desdcuento puede dar numeros con decimales como enteros pero no puede ser negativo.
EL total a pagar no pueden ser numeros negativos.

Restricciones explícitas: 
Deben ser 3 paquetes.
Cada paquete solo puede tener 1 o 50 paginas.
El descuento solo aplica cuando se supera el numero de 100 paginas entre los 3 paquetes.

Restricciones implícitas:
Las cantidades no deben de estar acompañadas de letras ni simbolos.
El precio tiene que ser reprecentado con dos decimales que pueden ser mayor o igual que 0 pero no menor.

Ambigüedades:
En el enunciado no hay ninguna ambiguedad ya que todas las instrucciones quedan claras a la primera lectura sin ningun  tipo de confucion a la hora de indicar.

Precondiciones :
El algoritmo debe comprobar que los valores ingresados son numeros enteros en la parte de la cantidad de paginas, paquetes y que no superen el limite de paquetes, ni paginas por paquete. 

Postcondiciones: 
Se muestra un mensaje de ser invalido el pedido o se muestra la cantidad de paginas y paquetes a imprimir.

Módulo/Función calcular_subtotal:
Precondiciones: 
El algoritmo recibe un numero entero no negativo valido.

Postcondiciones: 
El algoritmo muestra el precio siendo este mayor o igual que cero y con la restriciones de que debe contener dos decimales que pueden ser iguales a 0.

Pseudocodigo:

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