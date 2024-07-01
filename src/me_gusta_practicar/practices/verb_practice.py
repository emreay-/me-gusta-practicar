import pygame
import random

from typing import List

from me_gusta_practicar.core.verbs import load_verbs, Verb
from me_gusta_practicar.practices.practice_base import PracticeBase
from me_gusta_practicar.ui.display import Display
from me_gusta_practicar.ui.settings import SettingItem, BoolSettingItem, StringSettingItem, SettingsInterface

__all__ = ["VerbPractice"]

class VerbPractice(PracticeBase):
    def __init__(self, display: Display):
        super().__init__(display)

        self.verbs: List[Verb] = load_verbs()

        self.settings_options = {
            "type": StringSettingItem(
                name="type", default_value="From Spanish", allowed_values=["From Spanish", "From English"]
            ),
            "regulares": BoolSettingItem(name="regulares", default_value="True"),
            "irregulares": BoolSettingItem(name="irregulares", default_value="True"),
            "reflexivos": BoolSettingItem(name="reflexivos", default_value="True")
        }

        self.settings_interface = SettingsInterface(self.settings_options, self._display)

        self.instructions = [
            "Enter: Show translation",
            "Space: Next verb",
            "Esc: Main menu"
        ]

        self.current_index = 0
        self.show_translation = False
        
        self._select_verb()

    def _select_verb(self):
        iterations = 0
        max_iterations = 20

        while iterations < max_iterations:
            self.current_index = random.randint(0, len(self.verbs) - 1)
            verb = self.verbs[self.current_index]
            iterations += 1

            if self.settings_options["regulares"].value == "False" and verb.is_regular:
                continue
            if self.settings_options["irregulares"].value == "False" and not verb.is_regular:
                continue
            if self.settings_options["reflexivos"].value == "False" and verb.is_reflexive:
                continue

            break

    @property
    def _current_verb(self) -> Verb:
        return self.verbs[self.current_index]

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

            self._display.screen.fill((255, 255, 255))

            source = self._current_verb.name if self.settings_options["type"].value == "From Spanish" else self._current_verb.EN
            translation = self._current_verb.EN if self.settings_options["type"].value == "From Spanish" else self._current_verb.name

            source_text = self._display.font.render(source, True, (0, 0, 0))
            self._display.screen.blit(source_text, (self._display.screen.get_width() // 2 - source_text.get_width() // 2,
                                                    self._display.screen.get_height() // 2 - source_text.get_height() // 2))

            if self.show_translation:
                translation_text = self._display.medium_font.render(translation, True, (0, 0, 0))
                self._display.screen.blit(translation_text, (self._display.screen.get_width() // 2 - translation_text.get_width() // 2,
                                                             self._display.screen.get_height() // 2 + source_text.get_height()))

            for i, instruction in enumerate(self.instructions):
                instruction_text = self._display.small_font.render(instruction, True, (0, 0, 0))
                self._display.screen.blit(instruction_text, (10, 10 + i * 30))

            pygame.display.flip()

    def settings(self):
        self.settings_interface.render()

