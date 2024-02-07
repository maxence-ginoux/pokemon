import json
import pygame
import sys
from pygame.locals import QUIT, MOUSEBUTTONDOWN
#from Combat import Combat  # Importez la classe Combat du fichier combat.py


pygame.init()

# Paramètres de la fenêtre
screen = pygame.display.set_mode((850, 630))
pygame.display.set_caption("Pokémon")

# Charger l'image d'arrière-plan
background_pokedex = pygame.image.load("assets/scene3.png")
background_pokedex = pygame.transform.scale(background_pokedex, (850, 630))

# Couleurs
BLANC = (255, 255, 255)
BLEU = (50, 100, 176)
ROUGE = (255, 0, 0)
JAUNE = (255, 204, 1)

# Initialiser le module de police
pygame.font.init()

class Pokedex:
    def __init__(self):
        self.pokemon_list = []
        self.menu_button_rect = pygame.Rect(600, 500, 180, 50)  # Coordonnées et dimensions du bouton "Retour au menu"
        self.return_to_menu = False  # Variable pour suivre si le bouton "Retour au menu" a été cliqué
        self.pokemon_rects = []  # Stocker les rectangles des boutons pour la détection de collision
        self.selected_pokemon = []  # Stocker les Pokémon sélectionnés

    def load_pokedex(self):
        try:
            with open('Pokedex.json') as file:
                loaded_data = json.load(file)

            if isinstance(loaded_data, list) and len(loaded_data) > 0:
                # Extraire le dictionnaire de la liste
                loaded_data_dict = loaded_data[0]

                loaded_pokemon_list = []
                for pokemon_name, pokemon_info in loaded_data_dict.items():
                    loaded_pokemon_list.append(pokemon_info)

                self.pokemon_list = loaded_pokemon_list
                return self.pokemon_list
            else:
                print("Erreur : Structure incorrecte dans pokedex.json")
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Erreur : {e}")
            return None

    def dessiner_bouton_menu(self, screen):
        pygame.draw.rect(screen, BLEU, self.menu_button_rect)
        font = pygame.font.SysFont(None, 25)
        text_surface = font.render("Retour au menu", True, JAUNE)
        text_rect = text_surface.get_rect(center=self.menu_button_rect.center)
        screen.blit(text_surface, text_rect)            
                
    def choisir_pokemon_combat(self):
        pygame.display.set_caption("Sélection des Pokémon pour le combat")
        screen = pygame.display.set_mode((850, 630))

        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 36)
        input_font = pygame.font.Font(None, 28)

        self.selected_pokemon = []  # Réinitialiser les Pokémon sélectionnés

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.boutton == 1:  # Left mouse button
                        self.gerer_clic_pokemon(event, screen)
                    elif event.button == 3:  # Right mouse button
                        if len(self.selected_pokemon) == 2:
                            # Initiate the battle with the selected Pokémon
                            self.initier_combat(self.selected_pokemon[0], self.selected_pokemon[1], screen)
                            return  # Return after the battle
                        else:
                            self.selected_pokemon = []

            screen.fill((255, 255, 255))

            # Afficher les options de choix des Pokémon
            text = font.render("Sélectionnez deux Pokémon pour le combat:", True, (0, 0, 0))
            screen.blit(text, (20, 20))


            self.pokemon_rects = []   

            for i, (pokemon_info, y_offset) in enumerate(zip(self.pokemon_list, range(60, 60 + len(self.pokemon_list) * 100, 100)), start=1):
                text = input_font.render(f"{i}. {pokemon_info['nom']}", True, (0, 0, 0))
                rect = text.get_rect(topleft=(20, y_offset))
                self.pokemon_rects.append(rect)

                
                img = pygame.image.load(pokemon_info['img'])  
                img = pygame.transform.scale(img, (100, 100))  # Ajustez la taille de l'image selon vos besoins

                # Charger l'image du Pokémon
                pokemon_image_rect = img.get_rect(topleft=(rect.right + 10, y_offset))

                # Blitter le texte et l'image sur l'écran
                screen.blit(text, rect.topleft)
                screen.blit(img, pokemon_image_rect.topleft)

           
            pygame.display.flip()
            clock.tick(30)


    # def initier_combat(self, attaquant, defenseur, screen):
    #     combat_instance = Combat(attaquant, defenseur, screen)
    #     combat_instance.commencer_combat()

    # def gerer_clic_pokemon(self, event, screen):
    #     x, y = event.pos
    #     for i, (pokemon_rect, pokemon_info) in enumerate(zip(self.pokemon_rects, self.pokemon_list), start=1):
    #         if pokemon_rect.collidepoint(x, y):
    #             if pokemon_info not in self.selected_pokemon:
    #                 self.selected_pokemon.append(pokemon_info)

    def display_pokemon_info(self):
        pygame.display.set_caption("Pokedex")
        font = pygame.font.SysFont(None, 36)
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    x, y = event.pos
                    # Vérifie si les coordonnées de la souris sont à l'intérieur du bouton "Retour au menu"
                    if self.menu_button_rect.collidepoint(x, y):
                        self.return_to_menu = True  # Définissez la variable sur True lorsque vous cliquez sur le bouton
                        running = False  # Quitter la boucle

            # Vérifiez si la pokemon_list n'est pas vide avant d'essayer d'accéder à ses éléments
            if self.pokemon_list:
                screen.blit(background_pokedex, (0, 0))

                # Afficher les images et les informations des pokemons
                for i, pokemon_info in enumerate(self.pokemon_list):
                    # Afficher l'image du pokemon
                    img_path = pokemon_info['img']
                    img_surface = pygame.image.load(img_path)
                    screen.blit(img_surface, (350, 120 + i * 120))
                    # Afficher le nom du pokemon
                    font = pygame.font.Font(None, 20)
                    text = font.render(pokemon_info['nom'], True, BLANC)
                    screen.blit(text, (500, 120 + i * 120))
                    # Afficher le niveau du pokemon
                    text = font.render(f"Niveau : {pokemon_info['niveau']}", True, BLANC)
                    screen.blit(text, (500, 140 + i * 120))
                    # Afficher le type du pokemon
                    text = font.render(f"Type : {pokemon_info['types']}", True, BLANC)
                    screen.blit(text, (500, 160 + i * 120))

                # Affiche le bouton "Retour au menu"
                self.dessiner_bouton_menu(screen)

                pygame.display.flip()

# Créer une instance du Pokedex
pokedex_instance = Pokedex()

# Charger les données du Pokedex
pokedex_instance.load_pokedex()




