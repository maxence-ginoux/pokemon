import pygame
import sys
from Pokemon import Pokemon
from music_menu import Music
from Pokedex import Pokedex
from tkinter import filedialog  # Importer la boîte de dialogue de fichier pour ajout_pokemon

# Initialiser Pygame
pygame.init()

# Paramètres de la fenêtre
screen = pygame.display.set_mode((850, 630))
pygame.display.set_caption("Pokémon")

# Charger l'image de fond
background = pygame.image.load("assets/bgmenu.png")
background = pygame.transform.scale(background, (850, 630))

# Colors
BLANC = (255, 255, 255)
BLEU = (50, 100, 176)
ROUGE = (255, 0, 0)
JAUNE = (255, 204, 1)

class Game:
    def __init__(self):
        self.pokedex = Pokedex()
        # self.pokemon = Pokemon()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)

# Fonction pour dessiner le bouton
def dessiner_bouton(rectangle, couleur, texte, couleur_texte, taille_texte):
    pygame.draw.rect(screen, couleur, rectangle)
    
    police = pygame.font.Font(None, taille_texte)
    texte_surface = police.render(texte, True, couleur_texte)
    texte_rect = texte_surface.get_rect(center=rectangle.center)
    
    screen.blit(texte_surface, texte_rect)

# Créer une instance du Pokedex
pokedex_instance = Pokedex()

def ajout_pokemon():
    # Ajouter un Pokémon à partir d'un fichier
    files = filedialog.askopenfilenames(filetypes=[("pokemon.json")])
    for file in files:
        print(file)

def display_pokemon_info():
    # Afficher le Pokédex
    pokedex_instance.load_pokedex()
    pokedex_instance.display_pokemon_info()
   
# Coordonnées et dimensions du bouton
bouton1 = 150, 500, 100, 50
bouton2 = 350, 500, 100, 50
bouton3 = 550, 500, 180, 50
rectangle_bouton1 = pygame.Rect(bouton1)
rectangle_bouton2 = pygame.Rect(bouton2)
rectangle_bouton3 = pygame.Rect(bouton3)

# Music
music = Music()
music.change_music_opening()
music.play()
music.set_volume(0.1)

# Créer une instance du jeu
game = Game()

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if rectangle_bouton1.collidepoint(event.pos):
                from Choix_pokemon import *
            elif rectangle_bouton2.collidepoint(event.pos):
                # Créer et afficher le Pokedex
                pokedex_instance.load_pokedex()
                pokedex_instance.display_pokemon_info()
            elif rectangle_bouton3.collidepoint(event.pos):
                # Ajouter un Pokémon à partir d'un fichier
                pokedex_instance.ajout_pokemon()

    # Appliquer l'arrière-plan du jeu
    screen.blit(background, (0, 0))

    # Dessinez les boutons
    dessiner_bouton(rectangle_bouton1, BLEU, "Jouer", JAUNE, 25)
    dessiner_bouton(rectangle_bouton2, BLEU, "Pokédex", JAUNE, 25)
    dessiner_bouton(rectangle_bouton3, BLEU, "Ajouter un Pokémon", JAUNE, 25)                

   # Mettre à jour l'affichage
    pygame.display.flip()

    # Contrôler la fréquence d'images
    game.clock.tick(60)

# Quittez Pygame à la fin de la boucle
pygame.quit()
sys.exit()

