def procesar_numeros(numeros, S):
    # Inicializa una lista para almacenar el resultado
    resultado = []

    # Recorre cada número en la lista
    for numero in numeros:
        # Convierte el número a cadena para procesar dígitos
        numero_str = str(numero)
        
        # Inicializa una variable para el nuevo número
        nuevo_numero = ""

        # Recorre cada dígito del número
        for digito in numero_str:
            # Comprueba si el dígito es menor que S
            if int(digito) < S:
                nuevo_numero += digito
        
        # Si hay un número válido, se agrega a la lista de resultados
        if nuevo_numero != "":
            resultado.append(int(nuevo_numero))

    # Invierte el orden de los números en el resultado
    resultado_ordenado = []
    while resultado:
        maximo = resultado[0]
        for numero in resultado:
            # Encuentra el máximo en la lista
            if numero > maximo:
                maximo = numero
        # Agrega el máximo al resultado ordenado
        resultado_ordenado.append(maximo)
        resultado.remove(maximo)
    
    # Devuelve el resultado ordenado
    return resultado_ordenado


# Solicita el valor de S al usuario
S = int(input("Ingresa el valor de S: "))

# Solicita la lista de números al usuario
numeros_input = input("Ingresa la lista de números separados por comas: ")

# Convierte la entrada a una lista de enteros
numeros = [int(numero) for numero in numeros_input.split(",")]

# Llama a la función con los números ingresados y el valor de S
resultado_final = procesar_numeros(numeros, S)

# Imprime el resultado en consola
print("Resultado:", resultado_final)
