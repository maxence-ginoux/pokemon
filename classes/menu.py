# import pygame
# from music import *
# from game import Game
# from pokedex import Pokedex


# class Menu:
#     def __init__(self):
#         pygame.init()

#         # Générer la fenêtre de notre jeu
#         pygame.display.set_caption("Pokemon")
#         self.screen = pygame.display.set_mode((750, 630))

#         # Charger l'image d'arrière-plan
#         original_background = pygame.image.load('asetsi/Ma.jpg')
#         new_size = (750, 630)
#         self.background = pygame.transform.scale(original_background, new_size)

#         # Charger logo pokemon
#         self.overlay_image = pygame.image.load('asetsi/pokemon_image.png')

#         # Définir la police
#         self.font = pygame.font.Font(None, 36)

#         # Définir les couleurs
#         self.black = (252, 212, 66)

#         # Définir les boutons
#         self.enter_button_rect = pygame.Rect(100, 440, 150, 50)
#         self.add_pokemon_button_rect = pygame.Rect(240, 500, 270, 50)  # Nouveau bouton
#         self.pokedex_button_rect = pygame.Rect(500, 440, 150, 50)  # Nouveau bouton

#         # Musique
#         self.music = Music()
#         self.music.change_music_opening()
#         self.music.play()
#         self.music.set_volume(0.01)

#         # Boucle tant que cette condition est vraie
#         self.running = True

#     def run(self):
#         while self.running:
#             self.handle_events()
#             self.update_screen()

#         pygame.quit()

#     def handle_events(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 self.running = False
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 # Vérifier si les coordonnées de la souris sont à l'intérieur des boutons
#                 if self.enter_button_rect.collidepoint(event.pos):
#                     print("Bouton Jouer cliqué")
#                     # Ajoutez ici le code à exécuter lors du clic sur le bouton Jouer
#                 elif self.add_pokemon_button_rect.collidepoint(event.pos):
#                     print("Bouton Ajouter un Pokémon cliqué")
#                     # Ajoutez ici le code à exécuter lors du clic sur le bouton Ajouter un Pokémon
#                 elif self.pokedex_button_rect.collidepoint(event.pos):
#                     print("Bouton Pokédex cliqué")
#                     # Ajoutez ici le code à exécuter lors du clic sur le bouton Pokédex

#     def update_screen(self):
#         # Appliquer l'arrière-plan de notre jeu
#         self.screen.blit(self.background, (0, 0))

#         # Obtenir les dimensions de l'image pokemon
#         image_width, image_height = self.overlay_image.get_size()

#         # Calculer les coordonnées pour centrer l'image
#         x = (self.screen.get_width() - image_width) // 2
#         y = (self.screen.get_height() - image_height) // 2

#         # Superposer l'image centrée
#         self.screen.blit(self.overlay_image, (x, y))

#         # Dessiner les boutons
#         # pygame.draw.rect(self.screen, self.black, self.enter_button_rect)
#         # pygame.draw.rect(self.screen, self.black, self.add_pokemon_button_rect)
#         # pygame.draw.rect(self.screen, self.black, self.pokedex_button_rect)

#         # Afficher le texte des boutons
#         enter_text = self.font.render("Jouer", True, self.black)
#         add_pokemon_text = self.font.render("Ajoute un Pokémon", True, self.black)
#         pokedex_text = self.font.render("Pokédex", True, self.black)
#         self.screen.blit(enter_text, (self.enter_button_rect.x + 20, self.enter_button_rect.y + 15))
#         self.screen.blit(add_pokemon_text, (self.add_pokemon_button_rect.x + 20, self.add_pokemon_button_rect.y + 15))
#         self.screen.blit(pokedex_text, (self.pokedex_button_rect.x + 20, self.pokedex_button_rect.y + 15))

#         # Mettre à jour l'écran
#         pygame.display.flip()

# # Créer une instance de la classe PokemonGame
# game = Menu()
# game.run()





import pygame
from pygame.locals import *
from music import Music
from pokedex import Pokedex
from combat import Combat
from pokemon import Pokemon
import random
import json
import sys
import os

class Menu:
    SCREEN_SIZE = (750, 630)
    FPS = 60

    def __init__(self):
        pygame.init()
        self.init_game()

    def init_game(self):
        pygame.display.set_caption("Pokemon")
        self.screen = pygame.display.set_mode(Menu.SCREEN_SIZE)
        self.load_pokedex()
        self.init_buttons()
        self.pokedex = Pokedex()
        self.combat = Combat()
        self.player_pokemon = None
        self.to_dict_pokemon = None
        self.winner_message = None
        self.font = pygame.font.Font(None, 36)
        self.music = Music()
        self.music.change_music_opening()
        self.music.play()
        self.music.set_volume(0.01)
        self.running = True
        self.clock = pygame.time.Clock()

    def load_pokedex(self):
        try:
            image_path = os.path.join(os.path.dirname(__file__), 'images', 'Ma.jpg')
            self.background = pygame.transform.scale(pygame.image.load(image_path), Menu.SCREEN_SIZE)

            overlay_path = os.path.join('images', 'pokemon_image.png')
            self.overlay_image = pygame.image.load(overlay_path)

            self.black = (0, 0, 0)
        except pygame.error as e:
            print(f"Error loading images: {e}")
    pygame.quit()
    sys.exit()


    def init_buttons(self):
        self.enter_button_rect = pygame.Rect(100, 440, 150, 50)
        self.add_pokemon_button_rect = pygame.Rect(240, 500, 270, 50)
        self.pokedex_button_rect = pygame.Rect(500, 440, 150, 50)

    def run(self):
        while self.running:
            self.handle_events()
            self.update_screen()

    def start_game(self):
        self.pokedex.load_pokedex()

        if not self.pokedex.pokemon_list:
            print("Error: No Pokemon data loaded.")
            return

        to_dict = random.choice(self.pokedex.pokemon_list)
        self.to_dict_pokemon = Pokemon(**to_dict)

        with open('pokedex.json', 'r') as json_file:
            all_pokemon_data = json.load(json_file)

        player_data = random.choice(all_pokemon_data)
        self.player_pokemon = Pokemon(**player_data)

        self.play_game()
        print(self.winner_message)

    def play_game(self):
        running = True
        while running:
            self.clock.tick(Menu.FPS)

            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.combat.attaquer(self.player_pokemon, self.to_dict_pokemon)
                    elif event.key == K_ESCAPE:
                        pass

            if self.combat.is_battle_over(self.player_pokemon, self.to_dict_pokemon):
                self.winner_message = self.combat.determine_winner(
                    self.player_pokemon, self.to_dict_pokemon
                )
                running = False

            self.screen.fill((255, 255, 255))
            self.draw_pokemon(self.player_pokemon, 50, 50)
            self.draw_pokemon(self.to_dict_pokemon, 600, 50)
            self.draw_health_bar(self.player_pokemon, 50, 30)
            self.draw_health_bar(self.to_dict_pokemon, 600, 30)

            pygame.display.flip()

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.enter_button_rect.collidepoint(event.pos):
                    self.handle_play_button_click()
                elif self.add_pokemon_button_rect.collidepoint(event.pos):
                    self.handle_add_pokemon_button_click()
                elif self.pokedex_button_rect.collidepoint(event.pos):
                    self.handle_pokedex_button_click()

    def handle_play_button_click(self):
        self.font = pygame.font.Font(pygame.font.get_default_font(), 36)
        print("Bouton Jouer cliqué")

    def handle_add_pokemon_button_click(self):
        print("Bouton Ajouter un Pokémon cliqué")

    def handle_pokedex_button_click(self):
        print("Bouton Pokédex cliqué")

    def update_screen(self):
        self.screen.blit(self.background, (0, 0))
        image_width, image_height = self.overlay_image.get_size()
        x = (self.screen.get_width() - image_width) // 2
        y = (self.screen.get_height() - image_height) // 2
        self.screen.blit(self.overlay_image, (x, y))

        self.draw_buttons()
        pygame.display.flip()

    def draw_buttons(self):
        pygame.draw.rect(self.screen, self.black, self.enter_button_rect)
        pygame.draw.rect(self.screen, self.black, self.add_pokemon_button_rect)
        pygame.draw.rect(self.screen, self.black, self.pokedex_button_rect)

        enter_text = self.font.render("Jouer", True, self.black)
        add_pokemon_text = self.font.render("Ajoute un Pokémon", True, self.black)
        pokedex_text = self.font.render("Pokédex", True, self.black)

        self.screen.blit(enter_text, (self.enter_button_rect.x + 20, self.enter_button_rect.y + 15))
        self.screen.blit(add_pokemon_text, (self.add_pokemon_button_rect.x + 20, self.add_pokemon_button_rect.y + 15))
        self.screen.blit(pokedex_text, (self.pokedex_button_rect.x + 20, self.pokedex_button_rect.y + 15))

if __name__ == "__main__":
    game = Menu()
    game.run()
