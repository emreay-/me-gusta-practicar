import pygame
import json
from main_menu import MainMenu
from verb_practice import VerbPractice

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Spanish Practice')

def main():
    verb_practice = VerbPractice(screen)

    while True:
        menu = MainMenu(screen)
        selected_option = menu.run()

        if selected_option == "Verb Practice":
            verb_practice.run()
        elif selected_option == "Conjugation Practice":
            # Implement and import ConjugationPractice class similarly to VerbPractice
            pass
        elif selected_option == "Settings":
            verb_practice.settings()
        elif selected_option is None:
            break

    pygame.quit()

if __name__ == '__main__':
    main()
