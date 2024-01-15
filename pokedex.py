import json

class Pokedex:
    def __init__(self):
        self.liste_pokemon = []

    def ajouter_pokemon(self, pokemon):
        # Vérifier les doublons avant d'ajouter
        if pokemon not in self.liste_pokemon:
            self.liste_pokemon.append(pokemon)
            print(f"{pokemon.nom} ajouté au Pokédex!")

    def afficher_pokedex(self):
        print("Pokédex:")
        for pokemon in self.liste_pokemon:
            pokemon.afficher_informations()

    def sauvegarder_pokedex(self):
        # Sauvegarder le Pokedex dans le fichier pokedex.json
        with open("pokedex.json", "w") as fichier:
            json.dump([vars(p) for p in self.liste_pokemon], fichier)