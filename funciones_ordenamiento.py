#importamos time para poder medir el tiempo de rendimiento de los algoritmos
import time
import functools # Necesario para @functools.wraps
#Decorador que mide y muestra el tiempo de ejecución de una función.
#envuelve nuestras funciones de ordenamiento para medir cuánto tiempo
# tardan en ejecutarse, sin necesidad de modificar el código interno
# de esas funciones


def timed(func):

    @functools.wraps(func)
    # Preserva el nombre original y la documentación de la función.
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter() # Guarda el tiempo al iniciar la función.
        result = func(*args, **kwargs) # Ejecuta la función original.
        end_time = time.perf_counter()  # Guarda el tiempo justo al finalizar la función.
        elapsed_time = end_time - start_time # Calcula cuánto tiempo tardó la función.
        
        print(f"\nTiempo de ejecución de {func.__name__}: {elapsed_time:.6f} segundos.")
        
        return result
    return wrapper


""" 
 Bubble Sort funciona comparando elementos adyacentes y, 
si están en el orden incorrecto, los intercambia. Esto se repite en varias "pasadas" 
hasta que no haya más intercambios.
Ordena una lista de diccionarios 'arr' basándose en el valor de una 'key' específica.
    La ordenación puede ser ascendente o descendente.

    Args:
        arr (list): La lista de diccionarios a ordenar.
        key (str): La clave del diccionario por la cual se realizará el ordenamiento
                   (ej. 'height', 'name').
        ascending (bool, optional): Si es True, ordena de forma ascendente.
                                    Si es False, ordena de forma descendente.
                                    Por defecto es True.

    Returns:
        list: Una nueva lista con los diccionarios ordenados.
              Retorna una copia de la lista original para no modificarla directamente.
   
"""
##arr representa la lista
#key representa los atributos de esa lista. como los objetos
#key sera height para altura y name para nombre
# funciones_ordenamiento.py

# ... (imports y el decorador 'timed') ...



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
             value1 = int(pokemon1[key])
             value2 = int(pokemon2[key]) #si no convertimos a int los datos vienen como strings haciendolos dificil de comparar
         except KeyError:
                  print(f" Error: la clave {key} no se encontró en uno o ambos diccionarios de pokemones")
                  return arr_copy # devolvemos lo que hay hasta el momento si hay un error
              
         #Realizar la comparación e intercambio
            # Lógica:
            # - Si es ascendente y el primero es mayor que el segundo (fuera de orden)
            # - O si es descendente y el primero es menor que el segundo (fuera de orden)
            # Entonces, se realiza el intercambio.
            # Si queremos ordenar de forma ascendente (de menor a mayor) 
            # Y el primer valor es mayor que el segundo, significa que están en el orden incorrecto
            # y necesitan ser intercambiados.
            # : Si NO queremos ordenar de forma ascendente (es decir, queremos descendente) Y el primer valor
            # es menor que el segundo, también significa que están en el orden incorrecto (para un orden descendente)
            # y necesitan ser intercambiados.
         if (ascending and value1 > value2) or (not ascending and value1 < value2):
                # Intercambio de los elementos en la lista
                #(el lado derecho) son los nuevos valores que quiero poner
                # en esas posiciones, pero en el orden inverso.
                #valúa ambos valores del lado derecho. Una vez que tiene arr_copy[j + 1] y arr_copy[j] listos
                #  los asigna a las posiciones correspondientes en el lado izquierdo.
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
    return arr_copy # se devuelve la lista ordenada
"""

    Imprime una lista de Pokémon de forma formateada, limitando la cantidad mostrada.

    Args:
        pokemon_list (list): La lista de diccionarios de Pokémon a imprimir.
        title (str, optional): Un título para la sección de impresión. Por defecto es "Lista de Pokémon".
        limit (int, optional): El número máximo de Pokémon a mostrar. Por defecto es 10.
    """
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