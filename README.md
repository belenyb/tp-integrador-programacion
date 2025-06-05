# TP Integrador de Programación: Búsqueda y Ordenamiento

## Integrantes:
- Arturo Kaadú
- Belén Yarde Buller

## Imports
- Usamos librería `requests` para hacer llamadas a la PokéAPI
- Usamos librería `time` para calcular los tiempos de cada algoritmo de búsqueda

## Funciones
### get_pokemons()
Obtiene una lista de los 50 primeros pokemons y guarda su nombre y altura
Se hacen dos llamados a endpoints:
- A `/pokemon?offset=0&limit=50` para traer los 50 primeros pokemons.
- A `https://pokeapi.co/api/v2/pokemon/{pokemon_id}/` para traer la altura de cada pokemon utilizando su id como parámetro en la url.
