# Imports
import pprint
import requests
import timeit
from funciones_busqueda import binary_search, linear_search
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

# Ejecución principal

if __name__ == "__main__":
    GET_POKEMONS_LIMIT = 50
    runProgram = True

    # Llamamos a la función para obtener los datos y guardarlos en pokemons_list
    pokemons_list = get_pokemons(GET_POKEMONS_LIMIT)
    pprint.pprint(pokemons_list)

    if not pokemons_list:
        print("Error al obtener los pokemons.")
    else:
        while runProgram:
            # Acá ejecutamos los algoritmos de búsqueda y ordenamiento
            user_option = input("Ingrese la operacion que desea realizar: \n0. Salir \n1. Busqueda por nombre \n2. Busqueda por altura \n3. Ordenamiento por altura \n4. Ordenamiento por nombre: ")
            if (user_option == "1"):

                # Búsqueda por nombre
                desired_pokemon = input("Por favor, ingrese el pokemon que desea buscar: ")

                start_time = timeit.default_timer()
                linear_search(pokemons_list, 'name', desired_pokemon)
                end_time = timeit.default_timer()
                print("Tiempo de ejecución para linear_search por nombre:", end_time - start_time, "segundos")

                start_time = timeit.default_timer()
                binary_search(pokemons_list, 'name', desired_pokemon)
                end_time = timeit.default_timer()
                print("Tiempo de ejecución para binary_search:", end_time - start_time, "segundos")

                print(f"\n\n--- Fin de la ejecución de la opción {user_option} ---\n")

            elif (user_option == "2"):

                # Búsqueda por altura
                desired_height = input("Por favor, ingrese la altura que desea buscar (en decímetros): ")

                start_time = timeit.default_timer()
                linear_search(pokemons_list, 'height', desired_height)
                end_time = timeit.default_timer()
                print("Tiempo de ejecución para linear_search por altura:", end_time - start_time, "segundos")

                start_time = timeit.default_timer()
                binary_search(pokemons_list, 'height', desired_height)
                end_time = timeit.default_timer()
                print("Tiempo de ejecución para binary_search:", end_time - start_time, "segundos")

                print(f"\n\n--- Fin de la ejecución de la opción {user_option} ---\n")

            elif (user_option == "3"):
                # Bubble sort
                start_time = timeit.default_timer()
                sorted_pokemons_bubble = bubble_sort(pokemons_list, 'height', ascending=True)
                end_time = timeit.default_timer()
                print_pokemon_list(sorted_pokemons_bubble, "Pokémon ordenados por altura (ascendente) con Bubble Sort", limit=GET_POKEMONS_LIMIT)
                print("Tiempo de ejecución para bubble_sort:", end_time - start_time, "segundos")

                # Quick sort
                start_time = timeit.default_timer()
                sorted_pokemons_quick = quick_sort(pokemons_list, 'height', ascending=True)
                end_time = timeit.default_timer()
                print_pokemon_list(sorted_pokemons_quick, "Pokémon ordenados por altura (ascendente) con Quick Sort", limit=GET_POKEMONS_LIMIT)
                print("Tiempo de ejecución para quick_sort:", end_time - start_time, "segundos")

            elif (user_option == "4"):
            # Ordenamiento por nombre
                start_time = timeit.default_timer()
                sorted_pokemons_name = bubble_sort(pokemons_list, 'name', ascending=True)
                end_time = timeit.default_timer()

                print_pokemon_list(sorted_pokemons_name, "Pokémon ordenados por nombre (ascendente) con Bubble Sort", limit=GET_POKEMONS_LIMIT)
                print("Tiempo de ejecución para bubble_sort:", end_time - start_time, "segundos")
                # Ordenamiento por nombre ascendente
                start_time = timeit.default_timer()
                sorted_pokemons_name_desc = quick_sort(pokemons_list, 'name', ascending=True)
                end_time = timeit.default_timer()
                print_pokemon_list(sorted_pokemons_name_desc, "Pokémon ordenados por nombre (ascendente) con Quick Sort", limit=GET_POKEMONS_LIMIT)
                print("Tiempo de ejecución para quick_sort:", end_time - start_time, "segundos")

            elif (user_option == "0"):
                print("Saliendo del programa...")
                runProgram = False

            else:
                print("Por favor, ingrese una opción válida.")
