class Combat:
    @staticmethod
    def calcul_dommage(types_attaque, puissance_attaque, types_defense):
        type_efficacite = {
            'feu': {'terre': 2.0, 'eau': 0.5, 'normal': 1.0},
            'eau': {'feu': 2.0, 'terre': 0.5, 'normal': 1.0},
            'terre': {'eau': 2.0, 'feu': 0.5, 'normal': 1.0},
            'normal': {'feu': 1.0, 'eau': 1.0, 'terre': 1.0}
        }

        efficacite = type_efficacite.get(types_attaque, {}).get(types_defense, 1.0)
        return int(puissance_attaque * efficacite)

    @staticmethod
    def is_battle_over(player_pokemon, opponent_pokemon):
        if player_pokemon is None or opponent_pokemon is None:
            return True  # or False, depending on your logic
        return not player_pokemon.vie() or not opponent_pokemon.vie()

    @staticmethod
    def appliquer_dommage(defense, dommage):
        # defense.charger_dommage(dommage)
        defense.health -= dommage

    @staticmethod
    def determine_gagnant(joueur, adversaire):
        if not joueur.vie() and not adversaire.vie():
            return "C'est un match nul!"
        elif not joueur.vie():
            return f"Le gagnant est {adversaire.nom}!"
        elif not adversaire.vie():
            return f"Le gagnant est {joueur.nom}!"
        else:
            return None

    def attaquer(attaquer, defendre):
       
# Remplacez ceci par votre logique réelle pour calculer les dégâts en fonction des statistiques, du mouvement, etc. de l'attaquant.
        dommage_dealt = Combat.calcul_dommage(attaquer.types[0], attaquer.puissance_attaque, defendre.types[0])

        Combat.appliquer_dommage(defendre, dommage_dealt)


        print(f"{attaquer.nom} attaque {defendre.nom} et inflige {dommage_dealt} points de dégâts!")




# Make sure you have properly initialized player_pokemon and opponent_pokemon objects
# player_pokemon = Poke()  # Replace with your actual initialization
# opponent_pokemon = Poke()  # Replace with your actual initialization







