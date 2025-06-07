# TP Integrador de Programación: Búsqueda y Ordenamiento

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

### Funciones
#### get_pokemons()
Obtiene una lista de los 50 primeros pokemons y guarda su nombre y altura
```
    GET_POKEMONS_LIMIT = 50
```
Se hacen dos llamados a endpoints:
- A `/pokemon?offset=0&limit=GET_POKEMONS_LIMIT` para traer los 50 primeros pokemons.
- A `https://pokeapi.co/api/v2/pokemon/{pokemon_id}/` para traer la altura de cada pokemon utilizando su id como parámetro en la url.

## Reflexiones del equipo
