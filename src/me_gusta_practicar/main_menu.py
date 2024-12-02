import pygame

from me_gusta_practicar.practices import get_practice_display_names

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 74)
        self.medium_font = pygame.font.Font(None, 50)
        self.small_font = pygame.font.Font(None, 25)
        self.menu_options = get_practice_display_names()
        self.selected_option = 0
        self.instructions = [
            "Up/Down: Navigate",
            "Enter: Select option",
            "S: Settings"
        ]

    def last_selected(self):
        return self.menu_options[self.selected_option]

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.menu_options)
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.menu_options)
                    if event.key == pygame.K_RETURN:
                        return self.last_selected()
                    if event.key == pygame.K_s:
                        return "Settings"
                    if event.key == pygame.K_ESCAPE:
                        return

            self.screen.fill((255, 255, 255))

            for i, option in enumerate(self.menu_options):
                color = (0, 0, 0) if i == self.selected_option else (100, 100, 100)
                text = self.font.render(option, True, color)
                self.screen.blit(text, (self.screen.get_width() // 2 - text.get_width() // 2,
                                        100 + i * 100))

            for i, instruction in enumerate(self.instructions):
                instruction_text = self.small_font.render(instruction, True, (0, 0, 0))
                self.screen.blit(instruction_text, (10, 10 + i * 30))

            pygame.display.flip()
