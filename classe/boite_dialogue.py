import pygame
pygame.init()

class Boite_dialogue:
    x_position = 80
    y_position = 60

    def __init__(self):
        self.box = pygame.image.load("assets/dialog_box.png")
        self.box = pygame.transform.scale(self.box, (850, 150))
        self.texte = ["Salut Dresseur de Pokemon !", "T'es pret a combattre ?", "Je t'envoie mon meilleur Pokemon !", "Pokemon à l'attaque !", "Le Pokemon de ton adversaire attaque !", "Oh non ! Liam te crache la fume a la gueule !", "Tu es maintenant defonce pour 2 tours !"]
        self.font = pygame.font.Font("assets/pokemon_font.ttf", )
        self.texte_index = 0
        self.lettre_index = 0
        self.lecture = False

    def render(self, screen):
        if self.lecture:
            self.lettre_index += 1
            if self.lettre_index >= len(self.texte[self.texte_index]):
                self.lettre_index = self.lettre_index
            screen.blit(self.box, (0, 0))
            texte = self.font.render(self.texte[self.texte_index][0:self.lettre_index], False, (0, 0, 0))
            screen.blit(texte, (self.x_position, self.y_position))

    def texte_suivant(self):
        self.texte_index += 1
        self.lettre_index = 0

        if self.texte_index >= len(self.texte):
            self.lecture = False

    def execute(self):
        if self.lecture:
            self.texte_suivant()
        else:
            self.lecture = True
            self.texte_index = 0
