import json
from poke import Poke

class Pokedex:
    def __init__(self, file_path="pokedex.json"):
        self.file_path = file_path
        self.pokemon_list = self.load_pokedex()

    def load_pokedex(self):
        try:
            with open(self.file_path, "r") as file:
                return [Poke(**entry) for entry in json.load(file)]
        except (FileNotFoundError, PermissionError, json.JSONDecodeError) as e:
            print(f"Error loading Pokedex: {e}")
            return []

    def save_pokedex(self):
        data = [pokemon.to_dict() for pokemon in self.pokemon_list]
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=2)

    def add_pokemon(self, pokemon):
        if not any(p.nom == pokemon.nom for p in self.pokemon_list):
            self.pokemon_list.append(pokemon)
            self.save_pokedex()

    def display_pokemon_list(self):
        for pokemon in self.pokemon_list:
            print(f"Nom: {pokemon.nom}, Types: {pokemon.types}, Defense: {pokemon.defense}, "
                  f"Puissance d'Attaque: {pokemon.puissance_attaque}, Point de Vie: {pokemon.point_de_vie}")

















# import json
# from poke import Poke

# class Pokedex:
#     def __init__(self):
#         self.pokemon_list = []

#     def load_pokedex(self):
#         try:
#             with open('pokedex.json') as file:
#                 file_content = file.read()
#                 loaded_data = json.loads(file_content)
#                 print(loaded_data)

#             if all("nom" in pokemon and "types" in pokemon and "defense" in pokemon
#                    and "puissance_attaque" in pokemon and "point_de_vie" in pokemon
#                    for pokemon in loaded_data):
#                 # Crée des instances de la classe Poke en utilisant les données chargées
#                 loaded_pokemon_list = []
#                 for pokemon_data in loaded_data:
                    
#             # compréhension de dictionnaire pour obtenir dynamiquement des valeurs

#                     poke_data = {key: pokemon_data.get(key, default) for key, default in [
#                         ("img", ""),
#                         ("nom", ""),
#                         ("point_de_vie", 0),
#                         ("niveau", 1),
#                         ("puissance_attaque", 0),
#                         ("defense", 0),
#                         ("types", ""),
#                         ("evolution", "")
#                     ]}
                    
#                     # Crée une instance Poke avec les données fournies
#                     poke_instance = Poke(**poke_data)
#                     loaded_pokemon_list.append(poke_instance)


#                 self.pokemon_list = loaded_pokemon_list
#                 return self.pokemon_list
#             else:
#                 print("Error: Incomplete or invalid data in pokedex.json")
#         except FileNotFoundError:
#             pass

# if __name__ == "__main__":
#     pokedex = Pokedex()

#     pokedex.load_pokedex()

#     new_pokemon = ("")

#     # ajout nouveau pokemon
#     pokedex.ajout_pokemon_dans_pokedex(new_pokemon)

# #    sauvegarde
#     pokedex.save_pokedex()

# pokedex_instance = Pokedex()
# pokedex_instance.ajout_pokemon_dans_pokedex(new_pokemon)
            

# import json

# class Pokedex:
#     def __init__(self):
#         self.pokemon_list = []

#     def load_pokedex(self):
#         try:
#             with open("pokedex.json", "r") as file:
#                 self.pokemon_list = json.load(file)
#         except FileNotFoundError:
#             pass

#     def ajout_pokemon_dans_pokedex(self, nouveau_pokemon):
#         if not any(pokemon["nom"] == nouveau_pokemon.nom for pokemon in self.pokemon_list):
#             self.pokemon_list.append(nouveau_pokemon.to_dict())

#             with open("pokedex.json", "w") as file:
#                 json.dump(self.pokemon_list, file, indent=2)
#             print(f"Le Pokémon {nouveau_pokemon.nom} a été ajouté au pokedex.")
#         else:
#             print(f"Le Pokémon {nouveau_pokemon.nom} est déjà présent dans le pokedex.")

#     def ajout_pokemon(self, nouveau_pokemon):
#         if not any(pokemon["nom"] == nouveau_pokemon.nom for pokemon in self.pokemon_list):
#             self.pokemon_list.append(nouveau_pokemon.to_dict())
#             print(f"Le Pokémon {nouveau_pokemon.nom} a été ajouté au pokedex.")
#         else:
#             print(f"Le Pokémon {nouveau_pokemon.nom} est déjà présent dans le pokedex.")

#     def save_pokedex(self):
#         with open("pokedex.json", "w") as file:
#             json.dump(self.pokemon_list, file, indent=2)            
            

# import json
# import random

# class Pokedex:
#     def __init__(self):
#         self.pokemon_list = []

#     def load_pokedex(self):
#         try:
#             with open('pokedex.json') as file:
#                 self.pokemon_list = json.load(file)
#         except FileNotFoundError:
#             pass

#     def add_pokemon(self, pokemon):
#         if pokemon not in self.pokemon_list:
#             self.pokemon_list.append(pokemon)
#             with open('pokedex.json', 'w') as file:
#                 json.dump(self.pokemon_list, file)

#     def get_random_pokemon(self):
#         if self.pokemon_list:
#             return random.choice(self.pokemon_list)
#         else:
#             print("Error: No Pokemon in the Pokedex.")
#             return None









# pokedex.load_pokedex()


#     def load_pokedex(self):
#         try:
#             with open("pokedex.json", "r") as file:
#                 self.pokemon_list = json.load(file)
#         except FileNotFoundError:
#             pass

#     def ajout_pokemon(self, pokemon):
#         if not any(p["nom"] == pokemon.nom for p in self.pokemon_list):
#             self.pokemon_list.append(pokemon.to_dict())
#             with open("pokedex.json", "w") as file:
#                 json.dump(self.pokemon_list, file, indent=2)

#     def afficher_list_pokemon(self):
#         for pokemon in self.pokemon_list:
#             print(f"Nom: {pokemon['nom']}, Types: {pokemon['types']}, Defense: {pokemon['defense']}, "
#                   f"Puissance d'Attaque: {pokemon['puissance_attaque']}, Point de Vie: {pokemon['point_de_vie']}")


