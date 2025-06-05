#importamos time para poder medir el tiempo de rendimiento de los algoritmos
import time
import functools # Necesario para @functools.wraps
import threading # Necesario para manejar la concurrencia en el decorador
_recursion_depth = threading.local()
#Decorador que mide y muestra el tiempo de ejecución de una función. 
#envuelve nuestras funciones de ordenamiento para medir cuánto tiempo
# tardan en ejecutarse, sin necesidad de modificar el código interno de esas funciones
def timed(func):
    @functools.wraps(func)
    # Preserva el nombre original y la documentación de la función.
    def wrapper(*args, **kwargs):
        # Inicializar la profundidad para esta función y hilo si no existe
        if not hasattr(_recursion_depth, func.__name__):
            setattr(_recursion_depth, func.__name__, 0)

        current_depth = getattr(_recursion_depth, func.__name__)

        # Incrementar la profundidad ANTES de llamar a la función.
        # Si current_depth era 0, esta es la llamada de nivel superior.
        setattr(_recursion_depth, func.__name__, current_depth + 1)

        start_time = time.perf_counter() # Guarda el tiempo al iniciar la función.
        result = func(*args, **kwargs) # Ejecuta la función original.
        end_time = time.perf_counter()   # Guarda el tiempo justo al finalizar la función.
        elapsed_time = end_time - start_time # Calcula cuánto tiempo tardó la función.

        # Decrementar la profundidad después de la ejecución de la función.
        # Volvemos a la profundidad que teníamos antes de esta llamada.
        setattr(_recursion_depth, func.__name__, current_depth)

        # SOLO imprime si esta fue la llamada de nivel superior.
        # Esto lo sabemos porque la profundidad ANTES de incrementar era 0.
        if current_depth == 0:
            print(f"\nTiempo de ejecución de {func.__name__}: {elapsed_time:.6f} segundos.")

        return result
    return wrapper

# Aplica el decorador 'timed' a la función siguiente.
@timed
def bubble_sort (arr, key, ascending=True):
    n = len(arr) # para obtener el numero total de la lista. Basicamente la longitud de la lista que usaremos en la busqueda
    arr_copy = arr[:] #copiamos la lista por las dudas no interfiera con la lista principal de los pokemon
# for exterior Define hasta dónde tiene que trabajar el bucle j.
  
    for i in range(n - 1): # Controla cuántas pasadas principales se necesitan para que todos los grandes lleguen a su lugar final
        for j in range (n -1 - i): # El n - 1 es porque siempre comparamos un Pokémon con el de al lado (j con j+1)
            #accedemos a los elementos que tiene al lado el pokemon encontrado al recorrer
         pokemon1 = arr_copy[j]
         pokemon2 = arr_copy[j + 1]
         #despues extraemos los valores para comparar usando el argumento key
         # manejamos errores con try except en caso de que la clave no exista
         try:
             if key == 'name':
                 value1 = pokemon1[key].lower() # Convertimos a minúsculas para evitar problemas de mayúsculas/minúsculas
                 value2 = pokemon2[key].lower()
             else:
                value1 = int(pokemon1[key])
                value2 = int(pokemon2[key]) #si no convertimos a int los datos vienen como strings haciendolos dificil de comparar
         except KeyError:
                  print(f" Error: la clave {key} no se encontró en uno o ambos diccionarios de pokemones")
                  return arr_copy # devolvemos lo que hay hasta el momento si hay un error
              
         #Realizar la comparación e intercambio
         if (ascending and value1 > value2) or (not ascending and value1 < value2):
                # Intercambio de los elementos en la lista
                #(el lado derecho) son los nuevos valores que quiero poner
                # en esas posiciones, pero en el orden inverso.
                #valúa ambos valores del lado derecho. Una vez que tiene arr_copy[j + 1] y arr_copy[j] listos
                #  los asigna a las posiciones correspondientes en el lado izquierdo.
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
    return arr_copy # se devuelve la lista ordenada

#Imprime una lista de Pokémon de forma formateada, limitando la cantidad mostrada.
def print_pokemon_list(pokemon_list, title="lista de pokemon", limit=10):
    print(f"\n--- {title} ---") #
    if not pokemon_list:
        print("La lista de Pokémon está vacía.")
        return
    #le decimos hasta donde el limite para la devolucion y convertimos a cm porque los datos vienen en decimetros.
    for i, p in enumerate(pokemon_list[:limit]):
        name = p.get('name', 'nombre desconocido') #el segundo valor es para asegurarnos que muestre algo si hay error
        height_dm = p.get('height', 'altura desconocida')
        height_cm = 'altura desconocida'
        if isinstance(height_dm, (int,float)): #preguntamos si heightdm es int o float
            height_cm = height_dm * 10
        elif isinstance(height_dm, str) and height_dm.isdigit(): #preguntamos si es string y si ese string son digitos
            height_cm = int(height_dm) * 10
        print(f"  - {name}: {height_cm} cm")

@timed
def quick_sort(arr, key, ascending=True):
    #caso base: si la lista es vacía o tiene un solo elemento, ya está ordenada
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # Elegimos el pivote como el elemento del medio
    try:
        if key == 'name':
            pivot_value = pivot[key].lower()
        else:
            pivot_value = int(float(pivot[key]))
    except KeyError:
        print(f" Error: la clave '{key}' no se encontró en el pivote ({pivot.get('name', 'desconocido')}).")
        return arr
    except (ValueError, TypeError):
        print(f" Error: el valor del pivote para la clave '{key}' no es numérico en '{pivot.get('name', 'desconocido')}'.")
        return arr
    
    left = [] #pokemones a la izquierda del pivote
    middle = [] # pokemones que son iguales al pivote
    right = [] # pokemones a la derecha del pivote
    
    for pokemon in arr:
        try:
            if key == 'name':
                current_value = pokemon[key].lower()  # Convertimos a minúsculas para evitar problemas de mayúsculas/minúsculas
            else:
                # Convertimos el valor a int, manejando posibles errores de conversión
                current_value = int(float(pokemon[key])) # el valor actual del pokemon que se comparará
        except (KeyError, ValueError, TypeError):
            print(f" Error en Quicksort: la clave {key} no se encontró o su valor no es numérico para el elemento ({pokemon.get('name', 'desconocido')}).")
            return arr
    # Comparamos el valor actual con el valor del pivote si no pasamos al siguiente pokemon.    
        if current_value == pivot_value:
            middle.append(pokemon)
        elif (ascending and current_value < pivot_value) or (not ascending and current_value > pivot_value):
            left.append(pokemon)
        else:
            right.append(pokemon)
    
    return quick_sort(left, key, ascending) + middle + quick_sort(right, key, ascending)