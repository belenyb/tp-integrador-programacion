def normalizeInput(input):
    # Normaliza la entrada del usuario pasando todo a minúsculas y eliminando espacios en blanco
    return input.lower().strip()

def getKeyTranslation(key):
    # Recibe una key y devuelve su traducción en castellano
    if(key == 'name'):
        return 'Nombre'
    elif(key == 'height'):
        return 'Altura'
