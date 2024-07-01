import pygame

class Display:
     def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 74)
        self.medium_font = pygame.font.Font(None, 50)
        self.small_font = pygame.font.Font(None, 25)
