import pygame
import json

from me_gusta_practicar.main_menu import MainMenu
from me_gusta_practicar.practices import create_practices
from me_gusta_practicar.ui.display import Display

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Spanish Practice')

def main():
    display = Display(screen=screen)
    practices = create_practices(display)

    while True:
        menu = MainMenu(screen)
        selected_option = menu.run()

        if selected_option is None:
            break

        if selected_option == "Settings":
            practices[menu.last_selected()].settings()
            continue

        practices[selected_option].run()

    pygame.quit()

if __name__ == '__main__':
    main()
