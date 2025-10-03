# Definimos el alfabeto y la clave de sustitución
alfabeto = "abcdefghijklmnopqrstuvwxyz"
clave    = "qwertyuiopasdfghjklzxcvbnm"

def encriptar(texto, alfabeto, clave):
    """
    Encripta un mensaje usando el cifrado de sustitución.
    """
    texto_encriptado = ""
    # Creamos un diccionario para el mapeo rápido de letras
    tabla_sustitucion = str.maketrans(alfabeto, clave)
    
    for caracter in texto:
        # Encriptamos solo si el carácter es una letra
        if caracter.lower() in alfabeto:
            # Mantenemos las mayúsculas/minúsculas
            if caracter.islower():
                texto_encriptado += caracter.translate(tabla_sustitucion)
            else:
                texto_encriptado += caracter.lower().translate(tabla_sustitucion).upper()
        else:
            # Los caracteres que no son letras se mantienen igual
            texto_encriptado += caracter
            
    return texto_encriptado

# --- Interacción con el usuario ---
# Pedimos al usuario que ingrese el mensaje a encriptar
mensaje = input("Ingresa el texto que quieres encriptar: ")

# Usamos la función para encriptar el mensaje
mensaje_encriptado = encriptar(mensaje, alfabeto, clave)

# Mostramos los resultados
print(f"\nMensaje original: {mensaje}")
print(f"Mensaje encriptado: {mensaje_encriptado}")