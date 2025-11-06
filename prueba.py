def cifrar(texto, desplazamiento):
    resultado = ""
    for caracter in textos:
        if 'a' <= caracter.lower() <= 'z':kl
            inicio = ord('a')
            if 'A' <= caracter <= 'Z':
                inicio = ord('A')
            
            valor_original = ord(caracter)
            valor_cifrado = (valor_original - inicio + desplazamiento) % 26 + inicio
            resultado += chr(valor_cifrado)
        else:
            resultado += caracter
    return resultado
# Pedir al usuario que ingrese el texto y el número de desplazamiento hi
mensaje_original = input("Ingresa el texto para codificar: ")
desplazamiento_str = input("Ingresa el número de desplazamiento (por ejemplo, 3): ")

# Convertir el desplazamiento a un número entero  hola como esta.
try:
    desplazamiento_clave = int(desplazamiento_str)
    
    # Usar la función para cifrar el mensaje
    mensaje_cifrado = cifrar(mensaje_original, desplazamiento_clave)

    # Imprimir los resultados
    print(f"\nMensaje Original: {mensaje_original}")
    print(f"Desplazamiento: {desplazamiento_clave}")
    print(f"Mensaje Cifrado: {mensaje_cifrado}")

except ValueError:
    print("\nError: El desplazamiento debe ser un número entero.")