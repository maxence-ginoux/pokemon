import pokedex
import pokemon

class Combat:
    @staticmethod
    def calculer_degats(attaque, defense, type_attaquant, type_defenseur):
        # Logique de calcul des dégâts en fonction des types
        facteurs_efficacite = {
            ('eau', 'feu'): 2,
            ('feu', 'terre'): 2,
            ('terre', 'eau'): 2,
            ('normal', 'normal'): 1,
            # Ajoutez d'autres relations de type ici
        }

        effetivite = facteurs_efficacite.get((type_attaquant, type_defenseur), 1)
        degats = int(attaque * effetivite * (1 - defense/100))
        return degats

    def attaquer(self, attaquant, defenseur):
        # Logique d'attaque pendant le combat
        degats = self.calculer_degats(attaquant.puissance_attaque, defenseur.defense,
                                      attaquant.type_pokemon, defenseur.type_pokemon)
        defenseur.modifier_points_de_vie(degats)
        print(f"{attaquant.nom} attaque {defenseur.nom} et inflige {degats} dégâts!")

    def verifier_victoire(self, pokemon1, pokemon2):
        # Logique pour déterminer le vainqueur
        if pokemon1.points_de_vie <= 0:
            print(f"{pokemon2.nom} remporte le combat!")
            return pokemon2
        elif pokemon2.points_de_vie <= 0:
            print(f"{pokemon1.nom} remporte le combat!")
            return pokemon1
        else:
            return None

    def enregistrer_pokemon(self, pokemon, pokedex):
        pokedex.ajouter_pokemon(pokemon)
        pokedex.sauvegarder_pokedex()