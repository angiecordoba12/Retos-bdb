def cantidad_minima_no_dada(monedas):
    # Ordena las monedas para facilitar el cálculo
    monedas.sort()

    # Encuentra la cantidad mínima que no se puede dar
    cantidad_no_dada = 1  

    # Recorré las monedas para calcular la cantidad mínima no alcanzable
    for moneda in monedas:
        # Si la moneda actual es mayor que la cantidad no dada, no se puede formar esa cantidad
        if moneda > cantidad_no_dada:
            break
        # Suma el valor de la moneda a la cantidad no dada
        cantidad_no_dada += moneda

    return cantidad_no_dada

def main():
    # Solicita los valores de las monedas
    monedas_input = input("Ingrese los valores de las monedas para tú caja, separados por comas (ejemplo: 1,2,5): ")
    monedas = [int(x) for x in monedas_input.split(",")]  # Convertir una lista de enteros

    # Calcula la cantidad mínima que no se puede dar
    resultado = cantidad_minima_no_dada(monedas)

    # Muestra el resultado 
    print(f"La cantidad mínima de cambio que NO puedes dar es: {resultado}")

if __name__ == "__main__":
    main()