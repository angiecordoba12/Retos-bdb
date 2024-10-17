def procesar_lista(numeros, S):
    resultado = []  # Lista para almacenar los resultados

    for numero in numeros:  # Itera sobre cada número en la lista
        nuevo_numero = ''  # Inicializa una cadena vacía para construir el nuevo número
        
        for digito in str(numero):  # Convierte el número en cadena y recorre cada dígito
            if int(digito) < S:  # Verifica si el dígito es menor que S
                nuevo_numero += digito  # Si es válido, lo agrega a la cadena nuevo_numero
        
        if nuevo_numero != '':  # Comprueba si nuevo_numero no está vacío
            resultado.append(nuevo_numero)  # Agrega el número resultante a la lista como cadena

    # Invierte la lista de resultados
    resultado_invertido = resultado[::-1]

    # Muestra la lista invertida con números enteros
    print(f"La lista invertida es: {resultado_invertido}")

# Solicita al usuario que asigne un valor a S
S = int(input("Asigne un valor a S: "))

# Solicita al usuario que introduzca los números separados por comas
numeros = [int(x) for x in input("Introduzca los números separados por comas (ejemplo: 1,2,5): ").split(",")]

# Llama la función para procesar la lista
procesar_lista(numeros, S)
