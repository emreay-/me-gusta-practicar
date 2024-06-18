import pygame

class PracticeBase:
    def __init__(self, screen, data):
        self.screen = screen
        self.data = data
        self.font = pygame.font.Font(None, 74)
        self.medium_font = pygame.font.Font(None, 50)
        self.small_font = pygame.font.Font(None, 25)

    def run(self):
        raise NotImplementedError("Each practice must implement the run method")

    def settings(self):
        raise NotImplementedError("Each practice must implement the settings method")
