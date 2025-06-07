# Imports
import requests
import time
import timeit
from funciones_busqueda import linear_search
from funciones_ordenamiento import bubble_sort, print_pokemon_list, quick_sort


# Funciones

def get_pokemons(limit):
    print("Obteniendo pokemons...")
    # Obtenemos los primeros n (limit) pokemons de la PokéAPI, extrayendo solo su nombre y altura.
    # Devolvemos los datos directamente como una lista de diccionarios.

    # Definimos la url base de la PokéAPI
    base_url = "https://pokeapi.co/api/v2/"

    # Primera petición a endpoint para obtener un listado de los primeros 50 pokemons
    pokemons_list_url = f"{base_url}pokemon?offset=0&limit={limit}"

    # Inicializamos una lista vacía que luego retornaremos al final de la función
    get_pokemons_list = []

    # Hacemos la petición a la PokéAPI usando try except para capturar posibles errores y excepciones
    try:
        response_list = requests.get(pokemons_list_url)
        response_list.raise_for_status()
        list_info = response_list.json()

        # Del json devuelto en la petición, obtenemos el campo "results"
        pokemon_entries = list_info['results']

    except requests.exceptions.RequestException as e:
        # Si hay un error en la request, se imprime un mensaje de error por consola y se devuelve una lista vacía
        print(f"Error en get_pokemons(): {e}")
        return []

    # Segunda petición a endpoint para obtener la altura de cada pokemon
    # Iteramos sobre cada pokemon obtenido en la lista inicial, y de cada uno de ellos, tomamos la url: entry['url']
    for i, entry in enumerate(pokemon_entries):
        pokemon_detail_url = entry['url']

        # Volvemos a utilizar un bloque try except para capturar posibles errores
        try:
            response_detail = requests.get(pokemon_detail_url)
            response_detail.raise_for_status()
            pokemon_info = response_detail.json()

            # Creamos un diccionario pokemon_data para guardar la información que nos interesa: nombre y altura
            pokemon_data = {
                "name": pokemon_info['name'],
                "height": pokemon_info['height']
            }

            # Agregamos el diccionario de cada pokemon a la lista que retornará la función
            get_pokemons_list.append(pokemon_data)

        except requests.exceptions.RequestException as e:
                    # Si hay un error en la request, se imprime un mensaje de error por consola y se devuelve una lista vacía
            print(f"Error al obtener detalles para '{entry['name']}' ({pokemon_detail_url}): {e}")
            continue # Continúa con el siguiente Pokémon si hay un error

    # Devolvemos la lista obtenida mediante las llamadas a la API
    print("Listado de pokemons obtenido exitosamente")
    return get_pokemons_list

"""## Ejecución principal"""

if __name__ == "__main__":
    GET_POKEMONS_LIMIT = 150

    # Llamamos a la función para obtener los datos y guardarlos en pokemons_list
    pokemons_list = get_pokemons(GET_POKEMONS_LIMIT)

    
    if not pokemons_list:
        print("Error al obtener los pokemons.")
    else:
        # Acá ejecutamos los algoritmos de búsqueda y ordenamiento
        run = True
        while run:
            user_option = input("Ingrese la operacion que desea realizar:0. Salir 1. Busqueda lineal 2. Busqueda binaria 3. Ordenamiento Bubble por altura:, 4. Ordenamiento Quick Sort: ")
            if (user_option == "1"):
                desired_pokemon = input("Por favor, ingrese el pokemon que desea buscar: ")
                linear_search_response = linear_search(pokemons_list, desired_pokemon)
            elif (user_option == "2"):
                # Busqueda binaria
                print("Busqueda binaria")
            elif (user_option == "3"):
                # Ordenamiento 1
                sorted_pokemons_bubble = bubble_sort(pokemons_list, 'height', ascending=True)
                print_pokemon_list(sorted_pokemons_bubble, "Pokémon ordenados por altura (ascendente) con Bubble Sort", limit=GET_POKEMONS_LIMIT)

            elif (user_option == "4"):
                # Ordenamiento 2
                sorted_pokemons_quick = quick_sort(pokemons_list, 'height', ascending=True)
                print_pokemon_list(sorted_pokemons_quick, "Pokémon ordenados por altura (ascendente) con Quick Sort", limit=GET_POKEMONS_LIMIT)
            elif (user_option == "5"):
            # Ordenamiento por nombre
                sorted_pokemons_name = bubble_sort(pokemons_list, 'name', ascending=True)
                print_pokemon_list(sorted_pokemons_name, "Pokémon ordenados por nombre (ascendente) con Bubble Sort", limit=GET_POKEMONS_LIMIT)
            elif (user_option == "6"):
                # Ordenamiento por nombre descendente
                sorted_pokemons_name_desc = quick_sort(pokemons_list, 'name', ascending=False)
                print_pokemon_list(sorted_pokemons_name_desc, "Pokémon ordenados por nombre (descendente) con Quick Sort", limit=GET_POKEMONS_LIMIT)
            elif (user_option == "0"):
                print("Saliendo del programa...")
                run = False
            else:
                print("Opcion no valida.")
                
