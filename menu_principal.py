import pygame
from music import *
from game import *
from combat import *
from pokemon import *
from pokedex import *

class NewInterface:
    def __init__(self, screen):
        # Initialiser votre nouvelle interface ici
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.black = (252, 212, 66)

    def update_screen(self):
        # Ajoutez le code pour mettre à jour l'interface
        text = self.font.render("Nouvelle Interface", True, self.black)
        self.screen.blit(text, (100, 100))

class PokemonGame:
    def __init__(self):
        pygame.init()

        # Générer la fenêtre de notre jeu
        pygame.display.set_caption("Pokemon")
        self.screen = pygame.display.set_mode((750, 630))

        # Charger l'image d'arrière-plan
        original_background = pygame.image.load('asetsi/ii.jpg')
        new_size = (750, 630)
        self.background = pygame.transform.scale(original_background, new_size)

        # Charger logo pokemon
        self.overlay_image = pygame.image.load('asetsi/pokemon_image.png')

        # Définir la police
        self.font = pygame.font.Font(None, 36)

        # Définir les couleurs
        self.black = (252, 212, 66)

        # Définir les boutons
        self.enter_button_rect = pygame.Rect(100, 500, 150, 50)  # bouton jouer
        self.add_pokemon_button_rect = pygame.Rect(240, 550, 270, 50)  # bouton ajouter pokemon
        self.pokedex_button_rect = pygame.Rect(500, 500, 150, 50)  # bouton poedex
        self.combat_button_rect = pygame.Rect(300, 470, 150, 50)  # bouton Combat

        # Musique
        self.music = Music()
        self.music.change_music_opening()
        self.music.play()
        self.music.set_volume(0.01)

        # Boucle tant que cette condition est vraie
        self.running = True

        # Créer une instance de la nouvelle interface (initialisée à None au début)
        self.new_interface = None

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
                    print("Bouton Jouer cliqué")
                    # Créer et afficher la nouvelle interface lorsque le bouton "Jouer" est cliqué
                    self.new_interface = NewInterface(self.screen)

    def update_screen(self):
        # Appliquer l'arrière-plan de notre jeu
        self.screen.blit(self.background, (0, 0))

        # Obtenir les dimensions de l'image pokemon
        image_width, image_height = self.overlay_image.get_size()

        # Calculer les coordonnées pour centrer l'image
        x = (self.screen.get_width() - image_width) // 2
        y = (self.screen.get_height() - image_height) // 2

        # Superposer l'image centrée
        self.screen.blit(self.overlay_image, (x, y))

        # Dessiner les boutons
        # pygame.draw.rect(self.screen, self.black, self.enter_button_rect)
        # pygame.draw.rect(self.screen, self.black, self.add_pokemon_button_rect)
        # pygame.draw.rect(self.screen, self.black, self.pokedex_button_rect)
        # pygame.draw.rect(self.screen, self.black, self.combat_button_rect)

        # Afficher le texte des boutons
        enter_text = self.font.render("Jouer", True, self.black)
        add_pokemon_text = self.font.render("Ajoute un Pokémon", True, self.black)
        pokedex_text = self.font.render("Pokédex", True, self.black)
        combat_text = self.font.render("Combat", True, self.black)

        self.screen.blit(enter_text, (self.enter_button_rect.x + 20, self.enter_button_rect.y + 15))
        self.screen.blit(add_pokemon_text, (self.add_pokemon_button_rect.x + 20, self.add_pokemon_button_rect.y + 15))
        self.screen.blit(pokedex_text, (self.pokedex_button_rect.x + 20, self.pokedex_button_rect.y + 15))
        self.screen.blit(combat_text, (self.combat_button_rect.x + 20, self.combat_button_rect.y + 15))

        # Mettre à jour l'écran
        pygame.display.flip()

        # Si une nouvelle interface existe, mettre à jour et afficher cette interface
        if self.new_interface:
            self.new_interface.update_screen()

# Créer une instance de la classe PokemonGame
game = PokemonGame()
game.run()
