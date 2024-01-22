import random
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from pokedex import Pokedex

class Game:
    def __init__(self):
        pygame.init()

        self.pokedex = Pokedex()
        self.player_pokemon = None
        self.opponent_pokemon = None

        self.largeur, self.hauteur = 800, 600
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("Menu Pokémon")

        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font(None, 36)

    def display_menu(self):
        self.fenetre.fill((255, 255, 255))

        text_lancer = self.font.render("Lancer une partie", True, (0, 0, 0))
        text_ajouter = self.font.render("Ajouter un Pokémon", True, (0, 0, 0))
        text_acceder = self.font.render("Accéder à son Pokedex", True, (0, 0, 0))
        text_quitter = self.font.render("Quitter", True, (0, 0, 0))

        self.fenetre.blit(text_lancer, (300, 150))
        self.fenetre.blit(text_ajouter, (300, 200))
        self.fenetre.blit(text_acceder, (300, 250))
        self.fenetre.blit(text_quitter, (300, 300))

        pygame.display.flip()

    def choose_player_pokemon(self):
        # Afficher les Pokémon disponibles
        self.fenetre.fill((255, 255, 255))

        text_header = self.font.render("Choisissez votre Pokémon:", True, (0, 0, 0))
        self.fenetre.blit(text_header, (300, 50))

        for i, pokemon in enumerate(self.pokedex.pokemon_list):
            text_pokemon = self.font.render(f"{i + 1}. {pokemon.nom}", True, (0, 0, 0))
            self.fenetre.blit(text_pokemon, (300, 100 + i * 50))

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    return
                elif event.type == MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if 300 <= x <= 500 and 100 <= y <= 100 + len(self.pokedex.pokemon_list) * 50:
                        index = (y - 100) // 50
                        if 0 <= index < len(self.pokedex.pokemon_list):
                            self.player_pokemon = self.pokedex.pokemon_list[index]
                            print(f"Vous avez choisi {self.player_pokemon.nom}!\n")
                            return

            self.clock.tick(60)

    def choose_opponent_pokemon(self):
        # Choisir un adversaire au hasard parmi la liste des Pokémon
        self.opponent_pokemon = random.choice(self.pokedex.pokemon_list)
        print(f"L'adversaire a choisi {self.opponent_pokemon.nom}!\n")

    def start_game(self):
        print("Bienvenue dans le jeu Pokémon!\n")

        while True:
            self.display_menu()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    return
                elif event.type == MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if 300 <= x <= 500 and 150 <= y <= 180:
                        self.choose_player_pokemon()
                        self.choose_opponent_pokemon()
                        # Commencer le jeu...
                    elif 300 <= x <= 500 and 200 <= y <= 230:
                        self.add_pokemon()
                    elif 300 <= x <= 500 and 250 <= y <= 280:
                        self.access_pokedex()
                    elif 300 <= x <= 500 and 300 <= y <= 330:
                        pygame.quit()
                        return

            self.clock.tick(60)

    def add_pokemon(self):
        # Implémenter la logique pour ajouter un Pokémon
        pass

    def access_pokedex(self):
        # Implémenter la logique pour accéder au Pokedex
        pass


if __name__ == "__main__":
    game = Game()
    game.start_game()
