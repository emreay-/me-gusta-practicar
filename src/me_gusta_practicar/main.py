import pygame
import json

from me_gusta_practicar.main_menu import MainMenu
from me_gusta_practicar.practices.verb_practice import VerbPractice
from me_gusta_practicar.ui.display import Display

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Spanish Practice')

def main():
    display = Display(screen=screen)

    verb_practice = VerbPractice(display)

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
