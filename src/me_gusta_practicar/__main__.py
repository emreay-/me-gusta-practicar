import pygame
import json
import random

# Load the JSON data
with open('C:\\Users\\mremr\\personal-dev\\me-gusta-practicar\\src\\assets\\verbs.json') as f:
    data = json.load(f)

verbs = data["verbs"]

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Spanish Practice')

# Fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 50)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
    current_index = random.randint(0, len(verbs) - 1)
    show_translation = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    show_translation = True
                if event.key == pygame.K_SPACE:
                    current_index = random.randint(0, len(verbs) - 1)
                    show_translation = False

        screen.fill(WHITE)

        spanish_text = font.render(verbs[current_index]["spanish"], True, BLACK)
        screen.blit(spanish_text, (WIDTH//2 - spanish_text.get_width()//2, HEIGHT//2 - spanish_text.get_height()//2))

        if show_translation:
            english_text = small_font.render(verbs[current_index]["english"], True, BLACK)
            screen.blit(english_text, (WIDTH//2 - english_text.get_width()//2, HEIGHT//2 + spanish_text.get_height()))

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
