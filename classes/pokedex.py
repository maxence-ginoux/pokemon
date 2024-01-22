import json
from pokemon import Pokemon
import pygame
from pygame.locals import QUIT

pygame.init()

class Pokedex:
    def __init__(self):
        self.pokemon_list = []

    def load_pokedex(self):
        try:
            with open('pokedex.json') as file:
                file_content = file.read()
                loaded_data = json.loads(file_content)
                print("Loaded Data:", loaded_data)

            if all("nom" in pokemon and "types" in pokemon and "defense" in pokemon
                   and "puissance_attaque" in pokemon and "point_de_vie" in pokemon
                   for pokemon in loaded_data):
                # Crée des instances de la classe Pokemon en utilisant les données chargées
                loaded_pokemon_list = []
                for pokemon_data in loaded_data:
                    # Compréhension de dictionnaire pour obtenir dynamiquement des valeurs
                    pokemon_data = {key: pokemon_data.get(key, default) for key, default in [
                        ("img", ""),
                        ("nom", ""),
                        ("point_de_vie", 0),
                        ("point_de_vie_max", 0),
                        ("niveau", 1),
                        ("points_experience", 0),
                        ("points_experience_max", 0),
                        ("puissance_attaque", 0),
                        ("defense", 0),
                        ("types", ""),
                        ("evolution", ""),
                        ("attaques", [])
                    ]}
                    
                    # Convertir les valeurs numériques en entiers si nécessaire
                    for key in ["point_de_vie", "point_de_vie_max", "niveau", "points_experience",
                                "points_experience_max", "puissance_attaque", "defense"]:
                        pokemon_data[key] = int(pokemon_data[key])

                    # Afficher le dictionnaire poke_data
                    print("pokemon_data:", pokemon_data)

                    # Crée une instance Pokemon avec les données fournies
                    pokemon_instance = Pokemon(**pokemon_data)
                    loaded_pokemon_list.append(pokemon_instance)

                self.pokemon_list = loaded_pokemon_list
                return self.pokemon_list
            else:
                print("Error: Incomplete or invalid data in pokedex.json")
        except FileNotFoundError:
            pass
        # except Exception as e:
        #         print(f"Error loading Pokedex: {e}")

    def print_meet_pokemon(self):
        for pokemon in self.pokemon_list:
            print(f"Nom: {pokemon.nom}, Niveau: {pokemon.niveau}, Types: {pokemon.types}")


pokedex = Pokedex()
pokedex.load_pokedex()  # Appeler la méthode load_pokedex pour charger les données
pokedex.print_meet_pokemon()  # Appeler la méthode print_meet_pokemon pour afficher les informations





pygame.init()

# Définir la taille de la fenêtre
largeur, hauteur = 600, 600

# Créer la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))

# Définir la couleur blanche
blanc = (255, 255, 255)

# Remplir la fenêtre avec la couleur blanche
fenetre.fill(blanc)

# Afficher les images des Pokemon sur la fenêtre
for i, pokemon in enumerate(pokedex.pokemon_list):
    img_path = pokemon.img  
    img = pygame.image.load(img_path)
    fenetre.blit(img, (i * 150, 0))  # Dessiner l'image sur la fenêtre

# Mettre à jour l'affichage
pygame.display.flip()

# Boucle principale
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False

# Quitter Pygame
pygame.quit()
























# import json
# from pokemon import Pokemon

# class Pokedex:
#     def __init__(self, file_path="pokedex.json"):
#         self.file_path = file_path
#         self.pokemon_list = self.load_pokedex()

#     def load_pokedex(self):
#         try:
#             with open(self.file_path, "r") as file:
#                 data = json.load(file)
#                 return [self.create_pokemon(entry) for entry in data]
#         except FileNotFoundError:
#             print(f"Error: File '{self.file_path}' not found.")
#             return []
#         except json.JSONDecodeError:
#             print(f"Error: Unable to decode JSON from '{self.file_path}'.")
#             return []

#     def create_pokemon(self, entry):
#         try:
#             return Pokemon(**entry)
#         except TypeError as e:
#             print(f"Error creating Pokemon: {e}")
#             return None

#     def save_pokedex(self):
#         data = [pokemon.to_dict() for pokemon in self.pokemon_list if pokemon]
#         with open(self.file_path, "w") as file:
#             json.dump(data, file, indent=2)

#     def add_pokemon(self, pokemon):
#         if not any(p.nom == pokemon.nom for p in self.pokemon_list):
#             self.pokemon_list.append(pokemon)
#             self.save_pokedex()

#     def display_pokemon_list(self):
#         for pokemon in self.pokemon_list:
#             print(f"Nom: {pokemon.nom}, Types: {pokemon.types}, Defense: {pokemon.defense}, "
#                   f"Puissance d'Attaque: {pokemon.puissance_attaque}, Point de Vie: {pokemon.point_de_vie}")



# pokedex = Pokedex()
# pokedex.load_pokedex()  # Appeler la méthode load_pokedex pour charger les données
# pokedex.print_meet_pokemon()  # Appeler la méthode print_meet_pokemon pour afficher les informations



