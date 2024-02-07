import random
from json import *
from Pokemon import *
from Pokedex import *
import pygame

# Paramètres de la fenêtre
screen = pygame.display.set_mode((850, 630))
pygame.display.set_caption("Pokémon")

# Charger l'image d'arrière-plan
background = pygame.image.load("assets/bgmenu.png")
background = pygame.transform.scale(background, (850, 630))


class Combat:
    def __init__(self, attaquant, defenseur):
        self.attaquant = attaquant
        self.defenseur = defenseur

    def calculer_degats(self):
        type_attaquant = self.attaquant.types_pokemon
        type_defenseur = self.defenseur.types_pokemon

        efficacite_types = {
            "Feu": {"Feu": 0.5, "Eau": 0.5, "Plante": 2.0, "Normal": 1.0},
            "Eau": {"Feu": 2.0, "Eau": 0.5, "Plante": 0.5, "Normal": 1.0},
            "Plante": {"Feu": 0.5, "Eau": 2.0, "Plante": 0.5, "Normal": 1.0},
            "Normal": {"Feu": 1.0, "Eau": 1.0, "Plante": 1.0, "Normal": 1.0},
        }

        coefficient_efficacite = efficacite_types.get(type_attaquant, {}).get(type_defenseur, 1.0)
        degats = int(self.attaquant.puissance_attaque * coefficient_efficacite)

        return degats

    def enlever_points_de_vie(self, degats):
        points_de_vie_restants = max(self.defenseur.points_de_vie - degats, 0)
        self.defenseur.points_de_vie = points_de_vie_restants

    def verifier_victoire(self):
        if self.defenseur.points_de_vie == 0:
            return f"{self.attaquant.nom} remporte le combat !"
        elif self.attaquant.points_de_vie == 0:
            return f"{self.defenseur.nom} remporte le combat !"
        else:
            return None

    def enregistrer_combat(self, pokedex):
        self.defenseur.enregistrer_pokedex(pokedex)

    def simuler_attaque_adversaire(self):
        degats_adversaire = self.calculer_degats()
        self.enlever_points_de_vie_adversaire(degats_adversaire)

    def enlever_points_de_vie_adversaire(self, degats):
        points_de_vie_restants = max(self.attaquant.points_de_vie - degats, 0)
        self.attaquant.points_de_vie = points_de_vie_restants

    def simuler_tour(self):
        degats_joueur = self.calculer_degats()
        self.enlever_points_de_vie(degats_joueur)
        resultat_joueur = self.verifier_victoire()

        if resultat_joueur:
            return resultat_joueur

        self.simuler_attaque_adversaire()
        resultat_adversaire = self.verifier_victoire()

        return resultat_adversaire

    def afficher_etat_combat(self):
        print(f"{self.attaquant.nom} - Points de vie : {self.attaquant.points_de_vie}")
        print(f"{self.defenseur.nom} - Points de vie : {self.defenseur.points_de_vie}")


# Condition pour la sortie de la boucle infinie
running = True

while running:
    # appliquer l'arrière-plan du jeu
    screen.blit(background, (0, 0))

    # Mettre à jour l'affichage
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quitter Pygame à la fin de la boucle
pygame.quit()
