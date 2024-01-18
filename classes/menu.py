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
from game1 import Game

class Menu:
    SCREEN_SIZE = (750, 630)

    def __init__(self):
        pygame.init()
        self.init_game()

    def init_game(self):
        # from game import Game  # Import Game inside the method
        pygame.display.set_caption("Pokemon")
        self.screen = pygame.display.set_mode(Menu.SCREEN_SIZE)
        self.load_pokedex()  # Corrected method name
        self.init_buttons()
        self.game = Game()
        self.music = Music()
        self.music.change_music_opening()
        self.music.play()
        self.music.set_volume(0.01)
        self.running = True

    def load_pokedex(self):
    # Assuming 'asetsi/Ma.jpg' is in the 'asetsi' directory relative to the script
        self.background = pygame.transform.scale(pygame.image.load('images/Ma.jpg'), Menu.SCREEN_SIZE)
        self.overlay_image = pygame.image.load('images/pokemon_image.png')
        self.font = pygame.font.Font(pygame.font.get_default_font(), 36)  # Use default system font
        self.black = (252, 212, 66)

    def init_buttons(self):
        self.enter_button_rect = pygame.Rect(100, 440, 150, 50)
        self.add_pokemon_button_rect = pygame.Rect(240, 500, 270, 50)
        self.pokedex_button_rect = pygame.Rect(500, 440, 150, 50)

    def run(self):
        while self.running:
            self.handle_events()
            self.update_screen()

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
        # Add functionality for the "Jouer" button click
        self.font = pygame.font.Font(pygame.font.get_default_font(), 36)

        print("Bouton Jouer cliqué")

    def handle_add_pokemon_button_click(self):
        # Add functionality for the "Ajouter un Pokémon" button click
        print("Bouton Ajouter un Pokémon cliqué")

    def handle_pokedex_button_click(self):
        # Add functionality for the "Pokédex" button click
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



