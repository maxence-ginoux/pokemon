from game1 import Game

if __name__ == "__main__":
    game = Game()
    game.start_menu()

# main.py
from classes.pokedex import Pokedex
from pokemon import Pokemon

# Exemple d'utilisation
poke = Pokedex()

# Créer un nouveau Pokémon
new_pokemon = Pokemon("Bulbasaur", ["Grass", "Poison"], 49, 49, 45)

# Ajouter le nouveau Pokémon au Pokedex
poke.add_pokemon(new_pokemon)

# Afficher la liste des Pokémon dans le Pokedex
poke.display_pokemon_list()
