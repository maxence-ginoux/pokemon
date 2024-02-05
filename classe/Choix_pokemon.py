# Phase de sélection
import pygame
import json
import os
import Pokemon
import random
import global_vars


# Initialiser Pygame
pygame.init()

# Paramètres de la fenêtre
screen = pygame.display.set_mode((850, 630))
pygame.display.set_caption("Pokémon")

# Charger l'image d'arrière-plan
background_pokedex = pygame.image.load("assets/scene2.png")
background_pokedex = pygame.transform.scale(background_pokedex, (850, 630))

# Couleurs
BLANC = (255, 255, 255)
BLEU = (50, 100, 176)
ROUGE = (255, 0, 0)
JAUNE = (255, 204, 1)

# Initialiser le module de police
pygame.font.init()

# Lire les informations des pokemons à partir du fichier JSON
with open('Pokedex.json') as f:
    data = json.load(f)

# Créer une liste vide pour stocker les informations des pokemons
liste_pokemons = []

# Parcourir la liste de données et extraire les informations de chaque pokemon
for info in data:
    for key, value in info.items():
        # Charger l'image du pokemon
        value['image'] = pygame.image.load(value['img'])
        value['image'] = pygame.transform.scale(value['image'], (80, 80))
        liste_pokemons.append(value)

# Créer des rectangles pour chaque Pokémon
rectangles_pokemons = [pygame.Rect(350, 120 + i*120, 80, 80) for i in range(len(liste_pokemons))]

while True:
    # appliquer l'arrière plan du jeu
    screen.blit(background_pokedex, (0, 0))

    # Afficher les images et les informations des pokemons
    for i, pokemon in enumerate(liste_pokemons):
        # Afficher l'image du pokemon
        screen.blit(pokemon['image'], (350, 120 + i*120))
        # Afficher le nom du pokemon
        font = pygame.font.Font(None, 20)
        text = font.render(pokemon['nom'], True, BLANC)
        screen.blit(text, (500, 120 + i*120))
        # Afficher le niveau du pokemon
        text = font.render(f"Niveau: {pokemon['niveau']}", True, BLANC)
        screen.blit(text, (500, 140 + i*120))
        # Afficher le type du pokemon
        text = font.render(f"Type: {pokemon['types']}", True, BLANC)
        screen.blit(text, (500, 160 + i*120))

    # Mettre à jour l'affichage
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i, rectangle in enumerate(rectangles_pokemons):
                if rectangle.collidepoint(event.pos):
                    global_vars.pokemon_joueur = liste_pokemons[i] # Modifiez la variable pokemon_joueur
                    global_vars.pokemon_rival = random.choice([p for p in liste_pokemons if p != global_vars.pokemon_joueur]) # Modifiez la variable pokemon_rival
                    from fenetrecombat import *
                    print("Bouton pokemon cliqué")