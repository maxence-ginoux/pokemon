import json


class Pokemon:
    def __init__(self, nom, points_de_vie, niveau, puissance_attaque, defense, types):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.niveau = niveau
        self.puissance_attaque = puissance_attaque
        self.defense = defense
        self.types = types

    def to_dict(self):
        return {
            "nom": self.nom,
            "points_de_vie": self.points_de_vie,
            "niveau": self.niveau,
            "puissance_attaque": self.puissance_attaque,
            "defense": self.defense,
            "types": self.types
        }

def ajouter_pokemon_au_pokedex(nouveau_pokemon, pokedex):
    try:
        with open("pokedex.json", "r") as file:
            pokedex = json.load(file)
    except FileNotFoundError:
        pass

    if not any(pokemon["nom"] == nouveau_pokemon.nom for pokemon in pokedex):
        pokedex.append(nouveau_pokemon.to_dict())

        with open("pokedex.json", "w") as file:
            json.dump(pokedex, file, indent=2)
        print(f"Le Pokémon {nouveau_pokemon.nom} a été ajouté au pokedex.")
    else:
        print(f"Le Pokémon {nouveau_pokemon.nom} est déjà présent dans le pokedex.")


    
    
    
    
    
    
    
    
    

