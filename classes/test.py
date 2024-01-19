import pygame
from pygame.locals import *
import time
import math
import random
from pygame.sprite import _Group
import requests
import io
from urllib.request import urlopen

pygame.init()

# création de la fenetre jeu 
game_width = 500
game_heigth = 500
size = (game_width, game_heigth)
game = pygame.display.set_mode(size)
pygame.display.set_caption("Pokemon Combat")

# défini couleur
black = (0, 0, 0)
gold = (218, 165, 32)
grey = (200, 200, 200)
green = (0, 200, 0)
red = (200, 0, 0)
white = (255, 255, 255)

# url de l'API
base_url = "https://pokeapi.co/api/v2"

class Test(pygame.sprite.Sprite):

    def __init__(self, nom, niveau, x, y):
        
        pygame.sprite.Sprite.__init__(self)

       # appeler le point de terminaison de l'API Pokémon
        req = requests.get(f"{base_url}/pokemon/{nom.lower()}")
        self.json = req.json()

        #définir le nom et le niveau du Pokémon
        self.nom = nom
        self.niveau = niveau

        #définir la position du sprite sur l'écran
        self.x = x
        self.y = y 

        # nombre de postes restants
        self.num_positions = 3

        # récupère les statistiques du Pokémon depuis l'API
        stats = self.json["stats"]
        for stat in stats:
            if stat["stat"]["nom"] == "hp":
                self.current_point_de_vie = stat["base_stat"]


# boucle de jeu
game_status = "select pokemon"
while game_status != "quit":
    
    for event in pygame.event.get():
        if event.type == QUIT:
            game_status = "quit"

pygame.quit()



