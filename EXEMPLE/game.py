import pygame
from menu import Menu

class PokemonGame:
    MENU = 1
    SELECTION = 2
    POKEDEX = 3
    COMBAT = 4
    def __init__(self):
        self.menu = Menu()
        
        # Boucle tant que cette condition est vraie
        self.running = True
        self.current_state = PokemonGame.MENU

    def run(self):
        while self.running:
            if self.current_state == PokemonGame.MENU:
                self.menu.update_menu_screen()
                self.handle_menu_events()
            elif self.current_state == PokemonGame.SELECTION:
                self.update_selection_screen()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
            elif self.current_state == PokemonGame.POKEDEX:
                self.update_pokedex_screen()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
            
            

        pygame.quit()

    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.menu.enter_button_rect.collidepoint(event.pos):
                    print("Bouton Jouer cliqué")
                    self.current_state = PokemonGame.SELECTION
                if self.menu.pokedex_button_rect.collidepoint(event.pos):
                    print("Bouton Jouer cliqué")
                    self.current_state = PokemonGame.POKEDEX
                
    
    
    def update_selection_screen(self):
        self.menu.screen.fill('purple')
        
        #Ajouter le dessin de la nouvelles page
        rect = pygame.Rect(100, 100, 100, 100)
        pygame.draw.rect(self.menu.screen, 'black', rect, 15)
        pygame.draw.rect(self.menu.screen, 'white', rect, 10)
        
        
        pygame.display.flip()
        
    def update_pokedex_screen(self):
        self.screen.fill('green')
        pygame.display.flip()


# Créer une instance de la classe PokemonGame
game = PokemonGame()
game.run()
