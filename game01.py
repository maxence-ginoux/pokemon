import pygame
from pygame.locals import *
from poke import Poke
from combat import Combat
from pokedex import Pokedex
import random
import json

# Initialiser Pygame
pygame.init()

# Contraste
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
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
        self.opponent_pokemon = ""
        self.winner_message = None
        self.font = pygame.font.Font(None, 36)

    def start_game(self):
        # Chargez les données du fichier JSON dans le pokedex
        self.pokedex.load_pokedex()
        # print(self.pokedex.load_pokedex())
        # self.img  =  pygame.image("./pokemon/teste/images/Rondoudou.png") 
   
        # Vérifiez si le pokedex contient des données Pokémon
        if not self.pokedex.pokemon_list:
            print("Error: No Pokemon data loaded.")
            return
          
        # Choisissez un adversaire aléatoire dans le Pokedex
        self.opponent_data = random.choice(self.pokedex.pokemon_list)
        # print(self.opponent_data, "test")
        # return self.opponent_data
        # self.opponent_pokemon = Poke(**opponent_data)

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

            # Implémenter la logique du jeu en utilisant la classe Combat
            if self.combat.is_battle_over(self.player_pokemon, self.opponent_pokemon):
                self.gagnant_message = self.combat.determine_gagnant(
                    self.player_pokemon, self.opponent_pokemon
                )
                running = False

            # Gérer les entrées utilisateur (remplacer par votre propre logique de gestion des entrées)
            keys = pygame.key.get_pressed()
            if keys[K_SPACE]:
                # Par exemple, attaquer lorsque la touche espace est enfoncée
                self.combat.attaquer(self.player_pokemon, self.opponent_pokemon)

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

    def draw_pokemon(self, x, y):
        # if self.opponent_data:
        print(self.opponent_data)
        text = self.font.render(self.opponent_data.nom, True, WHITE)
        self.screen.blit(text, (x, y))
        pygame.display.set_caption('image')
        imp = self.opponent_data.img.convert_alpha()
        self.screen.blit(imp, (0, 0))
        pygame.display.flip()
        

    def draw_health_bar(self, pokemon, x, y):
        if pokemon:
            # Dessine le fond de la barre de santé
            pygame.draw.rect(self.screen, RED, (x, y, 100, 20))

            # Éviter une division par zéro potentielle
            if pokemon.point_de_vie > 0:
                # Calculer la largeur de la barre de santé en fonction de la santé actuelle
                health_percentage = pokemon.point_de_vie / pokemon.point_de_vie
                bar_width = int(health_percentage * 100)

                # Dessine la barre de santé
                pygame.draw.rect(self.screen, GREEN, (x, y, bar_width, 20))

            # Afficher la santé actuelle sous forme de texte
            health_text = self.font.render(f"HP: {pokemon.point_de_vie}/{pokemon.point_de_vie}", True, WHITE)
            self.screen.blit(health_text, (x + 110, y))

# if __name__ == "__main__":
#     game = Game()
#     game.start_game()
            

game = Game()
game.start_game()


