import pygame
import random

from me_gusta_practicar.core.verbs import load_verbs
from me_gusta_practicar.practices.practice_base import PracticeBase

__all__ = ["VerbPractice"]

class VerbPractice(PracticeBase):
    def __init__(self, screen):
        super().__init__(screen)

        self.verbs = load_verbs()

        self.settings_options = {
            "regulares": True,
            "irregulares": True,
            "reflexivos": True
        }
        self.instructions = [
            "Enter: Show translation",
            "Space: Next verb",
            "Esc: Main menu"
        ]

        self.current_index = 0
        self.show_translation = False
        
        self._select_verb()

    def _select_verb(self):
        found = False
        while not found:
            self.current_index = random.randint(0, len(self.verbs) - 1)
            verb = self.verbs[self.current_index]
            if self.settings_options["regulares"] is False and verb.is_regular:
                continue
            if self.settings_options["irregulares"] is False and not verb.is_regular:
                continue
            if self.settings_options["reflexivos"] is False and verb.is_reflexive:
                continue
            found = True

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.show_translation = True
                    if event.key == pygame.K_SPACE:
                        self._select_verb()
                        self.show_translation = False
                    if event.key == pygame.K_ESCAPE:
                        return  # Return to main menu

            self.screen.fill((255, 255, 255))

            spanish_text = self.font.render(self.verbs[self.current_index].name, True, (0, 0, 0))
            self.screen.blit(spanish_text, (self.screen.get_width() // 2 - spanish_text.get_width() // 2,
                                            self.screen.get_height() // 2 - spanish_text.get_height() // 2))

            if self.show_translation:
                english_text = self.medium_font.render(self.verbs[self.current_index].EN, True, (0, 0, 0))
                self.screen.blit(english_text, (self.screen.get_width() // 2 - english_text.get_width() // 2,
                                                self.screen.get_height() // 2 + spanish_text.get_height()))

            for i, instruction in enumerate(self.instructions):
                instruction_text = self.small_font.render(instruction, True, (0, 0, 0))
                self.screen.blit(instruction_text, (10, 10 + i * 30))

            pygame.display.flip()

    def settings(self):
        options = list(self.settings_options.keys())
        selected_option = 0

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        selected_option = (selected_option + 1) % len(options)
                    if event.key == pygame.K_UP:
                        selected_option = (selected_option - 1) % len(options)
                    if event.key == pygame.K_RETURN:
                        self.settings_options[options[selected_option]] = not self.settings_options[options[selected_option]]
                    if event.key == pygame.K_ESCAPE:
                        return  # Return to main menu

            self.screen.fill((255, 255, 255))

            for i, option in enumerate(options):
                color = (0, 0, 0) if i == selected_option else (100, 100, 100)
                status = "On" if self.settings_options[option] else "Off"
                text = self.medium_font.render(f"{option}: {status}", True, color)
                self.screen.blit(text, (self.screen.get_width() // 2 - text.get_width() // 2,
                                        100 + i * 50))

            instruction_text = self.small_font.render("Esc: Back to main menu", True, (0, 0, 0))
            self.screen.blit(instruction_text, (10, 10))

            pygame.display.flip()
