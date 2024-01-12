import pygame
pygame.init()

#générer la fenêtre de notre jeu
pygame.display.set_caption("Pokemon")
screen = pygame.display.set_mode((1000, 570))

#arrière plan de la fenêtre
background = pygame.image.load("images/scene1.png")

running = True

# boucle pour la fenêtre
while running:
    screen.blit(background, (0, 0)) 
    pygame.display.flip() 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()