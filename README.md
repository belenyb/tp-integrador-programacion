# Trabajo Práctico Integrador de Programación: Búsqueda y Ordenamiento
## "Análisis y aplicación de búsqueda y ordenamiento en Python sobre datos de la Poké API"

## Integrantes:

- Arturo Kaadú, Comisión 15
- Belén Yarde Buller, Comisión 23

## Descripción

Este proyecto busca implementar y comprender el funcionamiento de los algoritmos de búsqueda lineal y binaria, y los algoritmos de ordenamiento bubble sort y quick sort mediante el uso del lenguaje de programación Python. Para ello se utilizarán datos provenientes de la [Poké API](https://pokeapi.co/), sirviendo como una oportunidad para integrar diversos conceptos como el uso de APIs y de librerías de Python.


## Objetivos del proyecto

- Desarrollar y comprender el funcionamiento de los algoritmos de búsqueda (lineal y binaria) y ordenamiento (bubble sort y quick sort) en Python.
- Aplicar estos algoritmos en un caso práctico real y concreto como la utilización de APIs para la consulta de datos.
- Medir los tiempos de ejecución y entender el comportamiento de los algoritmos en diferentes escenarios.

## Instrucciones de uso

1. Ejecutar el archivo principal del programa
```
python3 main.py
```
2. Ingresar por consola la opción indicada acorde a la operación que desee realizar:
```
Obteniendo pokemons...
Listado de pokemons obtenido exitosamente
Ingrese la operacion que desea realizar:
0. Salir
1. Busqueda lineal
2. Busqueda binaria
3. Ordenamiento Bubble por altura
4. Ordenamiento Quick Sort
5. Ordenamiento por nombre
6. Ordenamiento por nombre descendente
```
- En caso de seleccionar la opción 1, debe ingresar un nombre por consola para continuar:
```
Por favor, ingrese el pokemon que desea buscar:
```

## Aspectos importantes del código

### Imports

- Usamos librería `requests` para hacer llamadas a la PokéAPI
- Usamos librería `timeit` para calcular los tiempos de cada algoritmo de búsqueda
- Usamos la librería `pprint` para imprimir la data obtenida desde la API de manera ordenada
- Creamos el directorio `/utils` con funciones básicas (`getKeyTranslation`, `normalizeInput`) para normalizar las entradas del usuario

### Funciones

#### Relativas a la API

##### get_pokemons()

Obtiene una lista de los 50 primeros pokemons y guarda su nombre y altura. Este valor se puede cambiar modificando la siguiente variable:
```
    GET_POKEMONS_LIMIT = 50
```
Se hacen dos llamados a endpoints:
- A `/pokemon?offset=0&limit=GET_POKEMONS_LIMIT` para traer los 50 primeros pokemons.
- A `https://pokeapi.co/api/v2/pokemon/{pokemon_id}/` para traer la altura de cada pokemon utilizando su id como parámetro en la url.

#### Relativas a algoritmos de búsqueda

Ambas funciones, `linear_search` y `binary_search`, están diseñadas para buscar un pokemon específico dentro de una lista (`pokemons_list`) basándose en un criterio (`search_key`, que puede ser `'name'` o `'height'`) y un valor de búsqueda (`search_query`) proporcionado por el usuario.

##### `linear_search(pokemons_list, search_key, search_query)`

Implementa el algoritmo de búsqueda lineal. Este método recorre la lista secuencialmente, elemento por elemento, desde el inicio hasta encontrar la primera coincidencia con el `search_query` o hasta el final de la lista.
- **Normalización de la Búsqueda:** Internamente, la función normaliza el `search_query` (convierte nombres a minúsculas usando `normalizeUserInput` y alturas a `float`) y los valores de los pokemon (`.lower()` para nombres) para asegurar comparaciones precisas e insensibles a mayúsculas/minúsculas.
- **Caso de Éxito:** Si encuentra un pokemon que coincide, lo imprime y lo retorna.
- **Caso de Falla:** Si recorre toda la lista sin encontrar una coincidencia, informa que el pokemon no fue hallado.

##### `binary_search(pokemons_list, search_key, search_query)`

Implementa el algoritmo de búsqueda binaria, el cual requiere que la lista esté ordenada previamente para funcionar de forma eficiente.
- **Pre-ordenamiento:** Al inicio de la función, la `pokemons_list` es ordenada utilizando la función `quick_sort` (importada de `funciones_ordenamiento`) basándose en la `search_key` especificada.
- **Normalización:** Similar a la búsqueda lineal, `search_query` y los valores de los pokemon son normalizados para garantizar comparaciones correctas. El valor se guarda en la variable `search_query_normalized`.
- **Proceso de Búsqueda:** Establece límites (`low` y `high`) y, en un bucle `while`, y calcula un punto medio (`mid`). Compara el valor del pokemon en `mid` con `search_query_normalized`:
    - Si coinciden, el pokemon es encontrado y retornado.
    - Si el valor en `mid` es menor, ajusta `low` para buscar en la mitad superior.
    - Si es mayor, ajusta `high` para buscar en la mitad inferior.
- **Caso de Falla:** Si los límites `low` y `high` se cruzan sin encontrar el elemento, informa que el pokemon no fue hallado.

#### Relativas a algoritmos de ordenamiento

##### bubble_sort()

##### quick_sort()

## Reflexiones del equipo

Durante la realización de este trabajo, se consolidó una comprensión profunda de los algoritmos de búsqueda lineal y binaria, así como de los métodos de ordenamiento Bubble Sort y Quick Sort. Se pudo apreciar de primera mano cómo la complejidad temporal de cada algoritmo se traduce en diferencias significativas en el tiempo de ejecución real, especialmente a medida que el tamaño de los datos aumenta. Se aprendió, también, la importancia crítica de las precondiciones de un algoritmo (como el ordenamiento para la búsqueda binaria) y cómo su costo debe ser considerado en el análisis de rendimiento global.
