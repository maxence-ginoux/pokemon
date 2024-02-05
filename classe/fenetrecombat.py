# Phase de combat
import pygame
from music_combat import Music
from boite_dialogue import Boite_dialogue
from Pokemon import Pokemon
import global_vars

# Paramètres de la fenêtre
screen = pygame.display.set_mode((850, 630))
pygame.display.set_caption("Pokémon")

dialog_box = Boite_dialogue()

# Charger l'image d'arrière-plan
background = pygame.image.load("assets/scene1.png")
background = pygame.transform.scale(background, (850, 630))

# Musique
music = Music()
music.change_music_opening()
music.play()
music.set_volume(0.1)

class Barre_de_vie():
 def __init__(self, x, y, w, h, points_de_vie_max):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.points_de_vie = points_de_vie_max
    self.points_de_vie_max = points_de_vie_max

 def draw(self, surface):
    #calcul du ratio de vie
    ratio = self.points_de_vie / self.points_de_vie_max
    pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
    pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))

barre_de_vie_joueur = Barre_de_vie(580, 520, 200, 20, 100)
barre_de_vie_rival = Barre_de_vie(150, 250, 200, 20, 100)

# Couleurs
BLANC = (255, 255, 255)
BLEU = (50, 100, 176)
ROUGE = (255, 0, 0)
JAUNE = (255, 204, 1)

def attaquer(self, adversaire, attaque_index):
        if 0 <= attaque_index < len(self.attaque):
            degats = self.attaque[attaque_index]['degats']
            subir_degats = Pokemon.subir_degats(degats)

while True:
    # appliquer l'arrière plan du jeu
    screen.blit(background, (0, 0))
    dialog_box.render(screen)
    barre_de_vie_joueur.points_de_vie = 100
    barre_de_vie_joueur.draw(screen)
    barre_de_vie_rival.points_de_vie = 100
    barre_de_vie_rival.draw(screen)

    # Afficher l'image du pokemon du joueur
    if global_vars.pokemon_joueur is not None: # Utilisez la variable pokemon_joueur
        image_pokemon_joueur = pygame.image.load(global_vars.pokemon_joueur['img']) # Utilisez la variable pokemon_joueur
        image_pokemon_joueur = pygame.transform.scale(image_pokemon_joueur, (200, 200))
        screen.blit(image_pokemon_joueur, (160, 400))

    # Afficher le nom et le niveau du pokemon du joueur
    if global_vars.pokemon_joueur is not None: # Utilisez la variable pokemon_joueur
        font = pygame.font.Font(None, 36)
        text = font.render(f"{global_vars.pokemon_joueur['nom']} - Niveau: {global_vars.pokemon_joueur['niveau']}", True, (0, 0, 0))
        screen.blit(text, (580, 550))

    # Afficher l'image du pokemon rival
    if global_vars.pokemon_rival is not None: # Utilisez la variable pokemon_rival
        image_pokemon_rival = pygame.image.load(global_vars.pokemon_rival['img']) # Utilisez la variable pokemon_rival
        image_pokemon_rival = pygame.transform.scale(image_pokemon_rival, (150, 150))
        screen.blit(image_pokemon_rival, (580, 230))

    # Afficher le nom et le niveau du pokemon rival
    if global_vars.pokemon_rival is not None: # Utilisez la variable pokemon_rival
        font = pygame.font.Font(None, 36)
        text = font.render(f"{global_vars.pokemon_rival['nom']} - Niveau: {global_vars.pokemon_rival['niveau']}", True, (0, 0, 0))
        screen.blit(text, (150, 280))

    # Mettre à jour l'affichage
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:

                dialog_box.execute()
