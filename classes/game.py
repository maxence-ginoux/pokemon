import pygame
from pygame.locals import *
from poke import Poke
from combat import Combat
from pokedex import Pokedex
import random
import json

# Initialiser Pygame
pygame.init()

# Constantes
WIDTH, HEIGHT = 800, 600
FPS = 60

# Couleurs
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pokemon Game")
        self.pokedex = Pokedex()
        self.combat = Combat()
        self.player_pokemon = None
        self.opponent_pokemon = None
        self.winner_message = None
        self.font = pygame.font.Font(None, 36)

    def start_game(self):
        # Charger les données du fichier JSON dans le pokedex
        self.pokedex.load_pokedex()

        # Vérifier si le pokedex contient des données Pokémon
        if not self.pokedex.pokemon_list:
            print("Error: No Pokemon data loaded.")
            return

        # Choisir un adversaire aléatoire dans le Pokedex
        opponent_data = random.choice(self.pokedex.pokemon_list)
        self.opponent_pokemon = Poke(**opponent_data)

        # Charger les données des joueurs depuis le fichier JSON
        with open('pokedex.json', 'r') as json_file:
            all_pokemon_data = json.load(json_file)

        player_data = random.choice(all_pokemon_data)
        self.player_pokemon = Poke(**player_data)

        # Commencer le combat
        self.play_game()

        # Afficher le message du gagnant
        print(self.winner_message)

    def play_game(self):
        running = True
        while running:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        # Attaquer lorsque la touche espace est enfoncée
                        self.combat.attaquer(self.player_pokemon, self.opponent_pokemon)
                    elif event.key == K_ESCAPE:
                        # Ajoutez d'autres actions pour d'autres touches
                        pass

            # Implémenter la logique du jeu en utilisant la classe Combat
            if self.combat.is_battle_over(self.player_pokemon, self.opponent_pokemon):
                self.winner_message = self.combat.determine_winner(
                    self.player_pokemon, self.opponent_pokemon
                )
                running = False

            # Mettre à jour l'affichage
            self.screen.fill(WHITE)
            self.draw_pokemon(self.player_pokemon, 50, 50)
            self.draw_pokemon(self.opponent_pokemon, 600, 50)
            # Dessine des barres de santé
            self.draw_health_bar(self.player_pokemon, 50, 30)
            self.draw_health_bar(self.opponent_pokemon, 600, 30)
            # Dessinez d'autres éléments de jeu
            # ...

            pygame.display.flip()

        pygame.quit()

    def draw_pokemon(self, pokemon, x, y):
        if pokemon:
            text = self.font.render(pokemon.nom, True, WHITE)
            self.screen.blit(text, (x, y))
            imp = pokemon.img.convert()  # Utilisez convert() au lieu de convert_alpha()
            self.screen.blit(imp, (x, y))  # Ajusté pour utiliser les coordonnées spécifiées

    def draw_health_bar(self, pokemon, x, y):
        if pokemon:
            # Dessine le fond de la barre de santé
            pygame.draw.rect(self.screen, RED, (x, y, 100, 20))

            # Éviter une division par zéro potentielle
            if pokemon.point_de_vie > 0:
                # Calculer le pourcentage de santé actuel
                health_percentage = pokemon.point_de_vie / pokemon.point_de_vie_max  # Utilisez point_de_vie_max
                bar_width = int(health_percentage * 100)

                # Dessine la barre de santé
                pygame.draw.rect(self.screen, GREEN, (x, y, bar_width, 20))

            # Afficher la santé actuelle sous forme de texte
            health_text = self.font.render(f"HP: {pokemon.point_de_vie}/{pokemon.point_de_vie_max}", True, WHITE)
            self.screen.blit(health_text, (x + 110, y))

game = Game()
game.start_game()
