"""## Algoritmos de búsqueda"""

def linear_search(pokemons_list, desired_pokemon):
  print("\n--- Prueba de Búsqueda Lineal: ---")

  for pokemon in pokemons_list:
    if pokemon['name'] == desired_pokemon.lower():
      print(f"'{desired_pokemon}' encontrado: {pokemon}")
      return pokemon

  print(f"'{desired_pokemon}' no encontrado.")
  return None
