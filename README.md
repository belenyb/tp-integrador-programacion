# Trabajo Práctico Integrador de Programación: Búsqueda y Ordenamiento
## "Análisis y aplicación de búsqueda y ordenamiento en Python sobre datos de la Poké API"

## Integrantes

- Arturo Kaadú, Comisión 15
- Belén Yarde Buller, Comisión 23

## Carpeta digital 

En este [enlace](https://drive.google.com/drive/folders/1xX3k4BufiF828CFBPqrVavEFupXtGB5e?usp=drive_link) se encuentra la carpeta digital de Google Drive con todo el contenido del proyecto.

## Descripción

Este proyecto busca implementar y comprender el funcionamiento de los algoritmos de búsqueda lineal y binaria, y los algoritmos de ordenamiento bubble sort y quick sort mediante el uso del lenguaje de programación Python. Para ello se utilizarán datos provenientes de la [Poké API](https://pokeapi.co/), sirviendo como una oportunidad para integrar diversos conceptos como el uso de APIs y de librerías de Python.

## Video explicativo

La presentación de este proyecto se puede ver en este [enlace](https://youtu.be/h9AMFHeEWss).

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

Estas funciones, `bubble_sort` y `quick_sort`, se encargan de reordenar la lista de Pokémon `pokemons_list` basándose en un criterio específico (`key`, que puede ser 'name' o 'height') y en un orden determinado (ascending, que puede ser True para ascendente o False para descendente).

##### bubble_sort(arr, key, ascending=True)

Implementa el algoritmo de ordenamiento Bubble Sort. Este método compara repetidamente pares de elementos adyacentes en la lista. Si están en el orden incorrecto (según el parámetro ascending), los intercambia. Este proceso se repite hasta que no se necesitan más intercambios, lo cual indica que la lista está ordenada.
**Preparación de los Datos:** Antes de realizar las comparaciones, la función crea una copia de la lista original para evitar modificaciones inesperadas. También se extraen los valores a comparar, `name` y `height` de cada elemento. En el caso de los nombres,los convierte a minúsculas para asegurar una comparación insensible a mayúsculas y minúsculas.
**Caso de Éxito:** Si la lista original ya está ordenada, o después de varias iteraciones, el algoritmo logra colocar todos los elementos en el orden correcto, la función devuelve la lista ordenada.
**Caso de Falla:** Si la clave especificada `key` no existe en alguno de los diccionarios de Pokémon, o si los valores a comparar no son del tipo esperado (por ejemplo, si `height` no es numérico), la función imprime un mensaje de error y devuelve la copia de la lista sin modificar, indicando que el ordenamiento no pudo completarse.

##### quick_sort(arr, key, ascending=True)

Implementa el algoritmo de ordenamiento Quick Sort. Este método utiliza la estrategia de "divide y vencerás" para ordenar la lista de forma eficiente. Selecciona un elemento como `pivot` y particiona la lista en sublistas `left`, `middle`, `right`: elementos menores al pivote y elementos mayores al pivote. Luego, aplica recursivamente el mismo proceso a las sublistas. 
**Preparacion de los Datos:** La función extrae los valores a comparar y los prepara adecuadamente. Para los nombres, los convierte a minúsculas. Para las alturas, intenta convertirlos a números, manejando posibles errores si no son válidos.
**Caso de Éxito:**  Después de aplicar recursivamente el proceso de partición y ordenamiento a las sublistas, la función devuelve la lista completamente ordenada.
**Caso de Falla:** Si la clave especificada no existe en algún diccionario de Pokémon, o si los valores a comparar no son del tipo esperado, la función imprime un mensaje de error y devuelve la lista original sin modificar. Esto asegura que el programa no se detenga abruptamente si encuentra datos inesperados.

##### print_pokemon_list(pokemon_list, title="Lista de Pokémon", limit=10)

Esta es una función auxiliar diseñada para mostrar las listas de Pokémon en la consola de una manera clara y formateada. Permite especificar un título para la lista y limitar la cantidad de Pokémon que se imprimen, lo cual es muy útil para revisar los resultados de los ordenamientos sin saturar la pantalla. Además, se encarga de convertir la altura de los Pokémon de decímetros a centímetros para una mejor comprensión y maneja casos donde los datos puedan estar ausentes o en formatos inesperados.

## Reflexiones del equipo

Durante la realización de este trabajo, se consolidó una comprensión profunda de los algoritmos de búsqueda lineal y binaria, así como de los métodos de ordenamiento Bubble Sort y Quick Sort. Se pudo apreciar de primera mano cómo la complejidad temporal de cada algoritmo se traduce en diferencias significativas en el tiempo de ejecución real, especialmente a medida que el tamaño de los datos aumenta. Se aprendió, también, la importancia crítica de las precondiciones de un algoritmo (como el ordenamiento para la búsqueda binaria) y cómo su costo debe ser considerado en el análisis de rendimiento global.
