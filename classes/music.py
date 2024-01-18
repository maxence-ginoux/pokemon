"""
<sound>.play(loop = 0, time = 0, fadein = 1000)
"""
import pygame
 
class Music:
    def __init__(self):
        pygame.mixer.init() # Initialisation de pygame
        self.current_song = None
    def play(self):
        pygame.mixer.music.play(- 1 ) # Joue en boucle la musique
    def pause(self):
        pygame.mixer.music.pause()
    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume)
    def change_music_opening(self):
        self.current_song = pygame.mixer.music.load( '../Generique.mp3')