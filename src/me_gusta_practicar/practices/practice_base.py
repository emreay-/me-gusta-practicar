import pygame

__all__ = ["PracticeBase"]

class PracticeBase:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 74)
        self.medium_font = pygame.font.Font(None, 50)
        self.small_font = pygame.font.Font(None, 25)

    def run(self):
        raise NotImplementedError("Each practice must implement the run method")

    def settings(self):
        raise NotImplementedError("Each practice must implement the settings method")
