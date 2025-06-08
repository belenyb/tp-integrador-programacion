from utils.string_utils import getKeyTranslation, normalizeInput
from funciones_ordenamiento import quick_sort

'''
Algoritmos de búsqueda lineal y binaria.
Ambas funciones reciben 3 parámetros:
    - La lista de pokemon (pokemons_list)
    - La clave de búsqueda (search_key), que puede ser 'name' o 'height'
    - El valor de búsqueda (search_query), que será el valor de búsqueda ingresado por el usuario en consola (se
    guarda en las variables desired_pokemon o desired_height dentro del archivo main.py)
'''

# Busqueda Lineal
def linear_search(pokemons_list, search_key, search_query):

    print(f"\n\n--- Ejecutando Búsqueda Lineal por {getKeyTranslation(search_key)}: ---\n")

    # Busqueda por nombre
    if search_key == 'name':
        search_query = normalizeInput(search_query)
        for pokemon in pokemons_list:
            if pokemon.get(search_key) and pokemon[search_key].lower() == search_query:
                print(f"'{search_query}' encontrado: {pokemon}")
                return pokemon

    # Busqueda por altura
    elif search_key == 'height':
        # Intentamos convertir el valor de búsqueda a un tipo numérico para comparar alturas
        try:
            search_query = float(search_query)
        except ValueError:
            # Si la conversión falla, capturamos el error, imprimimos un mensaje informativo y devolvemos None
            print("Error: El valor de altura debe ser un número.")
            return None

        for pokemon in pokemons_list:
            if pokemon.get(search_key) and pokemon[search_key] == search_query:
                print(f"pokemon con altura '{search_query}' encontrado: {pokemon}")
                return pokemon

    else:
    # Si la clave de búsqueda no es 'name' ni 'height', imprimimos un mensaje informativo y devolvemos None
    # Esto no ocurrirá ya que el programa manejará las claves de búsqueda 'name' y 'height', pero se incluye para evitar
    # posibles errores y asegurarse de que el programa funcione correctamente
        print(f"Criterio de búsqueda '{search_key}' no válido. Opciones válidas: 'name' o 'height'.")
        return None

    print(f"'{search_query}' no encontrado por {getKeyTranslation(search_key)}.")
    return None

# Busqueda Binaria
def binary_search(pokemons_list, search_key, search_query):

    print(f"\n--- Ejecutando Búsqueda Binaria por {getKeyTranslation(search_key)}: ---\n")

    # Tomamos en cuenta el caso de que la función reciba una lista vacía
    if not pokemons_list:
        print("La lista de pokemon está vacía.")
        return None

    # Ordenamos la lista de pokemons utilizando la funcion quick_sort del archivo funciones_ordenamiento. Esta función
    # ordena la lista de forma ascendente por defecto. Guardamos el resultado en la variable pokemons_list_sorted.
    pokemons_list_sorted = quick_sort(pokemons_list[:], search_key)

    # Inicializamos los punteros low y high para el algoritmo de búsqueda binaria
    # 'low' es el índice más bajo de la lista, el primer elemento.
    low = 0
    # 'high' es el índice más alto, es decir, el último elemento de la lista ordenada.
    # Se le resta 1 a len() ya que el rango de la lista comienza en 0.
    high = len(pokemons_list_sorted) - 1

    # Normalizamos el valor de search_query que proviene del input ingresado por el usuario en consola
    search_query_normalized = None
    if search_key == 'name':
        # Si se trata de un string, usamos nuestra función normalizeUserInput de /utils
        search_query_normalized = normalizeInput(search_query)
    elif search_key == 'height':
        try:
            # Si se trata de un valor referido a altura, lo convertimos a float
            search_query_normalized = float(search_query)
        except ValueError:
            print("Error: El valor de altura para búsqueda binaria debe ser un número válido.")
            return None
    else:
        print(f"Criterio de búsqueda '{search_key}' no válido para búsqueda binaria. Use 'name' o 'height'.")
        return None

    # ------------------ Bucle Principal de la Búsqueda Binaria ------------------

    # El bucle 'while' continuará mientras 'low' sea menor o igual que 'high'.
    # Esto significa que todavía hay un rango de elementos para examinar:
    while low <= high:
        # Paso 1: Calcular el punto medio (índice 'mid')
        # 'mid' es el índice del elemento central en el segmento actual de la lista.
        # Usamos división entera '//' para asegurar que 'mid' sea un índice válido
        mid = (low + high) // 2

        # Paso 2: Obtener el pokemon en la posición media
        current_pokemon = pokemons_list_sorted[mid]

        # Extraemos el valor del pokemon actual basándonos en la clave de búsqueda
        # Usamos .get() para manejar el caso de que la clave no exista.
        current_value = current_pokemon.get(search_key)

        # Manejamos el caso de que el valor no exista para este pokemon
        if current_value is None:
            print(f"Advertencia: pokemon en índice {mid} no tiene la clave '{search_key}'. No se puede continuar la búsqueda.")
            return None

        # Paso 3: Normalizar el valor del pokemon actual para la comparación.
        normalized_current_value = current_value
        if search_key == 'name':
            normalized_current_value = normalizeInput(str(current_value))

        # Si search_key es 'height', el valor de current_value ya es numérico (int/float),
        # por lo que no necesita una normalización adicional.

        # Acá decidimos qué mitad descartar
        if normalized_current_value == search_query_normalized:
            # El valor del medio coincide con lo que buscamos. Devolvemos el resultado.
            print(f"'{search_query}' encontrado por {getKeyTranslation(search_key)}: {current_pokemon}")
            return current_pokemon

        elif normalized_current_value < search_query_normalized:
            # El valor en el medio es MENOR que lo que buscamos.
            # Esto significa que el pokemon buscado (si existe) debe estar en la mitad DERECHA de la lista.
            # Por lo tanto, movemos el límite inferior ('low') para empezar la búsqueda después del medio.
            low = mid + 1

        else: # normalized_current_value > search_query_normalized
            # El valor en el medio es MAYOR que lo que buscamos.
            # Esto significa que el pokemon buscado (si existe) debe estar en la mitad IZQUIERDA de la lista.
            # Por lo tanto, movemos el límite superior ('high') para terminar la búsqueda antes del medio.
            high = mid - 1

    # Si el bucle 'while' termina, significa que 'low' se volvió mayor que 'high'.
    # Esto ocurre cuando el rango de búsqueda se ha reducido a cero o menos,
    # lo que indica que el elemento buscado no fue encontrado en la lista.
    print(f"'{search_query}' no encontrado por {getKeyTranslation(search_key)}.")
    return None
