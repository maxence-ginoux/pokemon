import json

class Pokedex:
    def __init__(self):
        pass

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



    
    
    
    
    
    
    
    
    

