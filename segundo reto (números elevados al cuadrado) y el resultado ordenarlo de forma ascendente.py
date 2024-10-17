def sorted_squared_array(numeros, S):
    SS = S * S  # Calcula el cuadrado de S para establecer el límite superior de los valores permitidos.
    
    resultado = []  # Crea una lista vacía para almacenar los cuadrados de los números que cumplan con la condición.

    # Usa dos punteros para recorrer la lista 'numeros'. Un puntero al principio y otro al final de la lista.
    inicio = 0  # Puntero que comienza al inicio de la lista.
    fin = len(numeros) - 1  # Puntero que comienza al final de la lista.

    while inicio <= fin:  # Recorre la lista mientras ambos punteros no se crucen.
        # Calcula los cuadrados de los números en las posiciones apuntadas por los punteros.
        cuadrado_inicio = numeros[inicio] * numeros[inicio]
        cuadrado_fin = numeros[fin] * numeros[fin]

        # Compara los cuadrados y los añade al resultado en orden correcto
        if cuadrado_inicio < cuadrado_fin:
            if cuadrado_inicio <= SS:  # Verifica si el cuadrado está dentro del rango permitido.
                resultado.append(cuadrado_inicio)  # Añade el cuadrado al resultado.
            inicio += 1  # Mueve el puntero 'inicio' hacia la derecha.
        else:
            if cuadrado_fin <= SS:  # Verifica si el cuadrado está dentro del rango permitido.
                resultado.append(cuadrado_fin)  # Añade el cuadrado al resultado.
            fin -= 1  # Mueve el puntero 'fin' hacia la izquierda.

    # Al final, la lista resultado tiene los cuadrados en orden inverso, por lo que debemos invertirla.
    resultado.sort()  # Ordena la lista en orden ascendente antes de retornarla.
    
    return resultado  # Retorna la lista ordenada en orden ascendente.

# Solicita la entrada del usuario
S = float(input("Ingrese el límite superior S: "))  # Pide al usuario que ingrese el límite superior.
numeros_input = input("Ingrese la lista de números separados por comas: ")  # Pide la entrada de valores al usuario.
numeros = [int(numero) for numero in numeros_input.split(",")]  # Convierte la cadena de entrada en una lista de enteros.

# Llama a la función y muestra el resultado
resultado = sorted_squared_array(numeros, S)
print("Los cuadrados ordenados son:", resultado)  # Imprime el resultado.
