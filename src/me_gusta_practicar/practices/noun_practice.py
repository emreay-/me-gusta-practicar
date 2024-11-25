import pygame
import random
from collections import deque

from typing import List

from me_gusta_practicar.core.nouns import load_nouns, Noun, Gender
from me_gusta_practicar.practices.practice_base import PracticeBase
from me_gusta_practicar.ui.display import Display
from me_gusta_practicar.ui.settings import SettingItem, BoolSettingItem, StringSettingItem, SettingsInterface

__all__ = ["NounPractice"]

class NounPractice(PracticeBase):
    display_name = "Practice Nouns"

    def __init__(self, display: Display):
        super().__init__(display)

        self.nouns: List[Noun] = load_nouns()

        self.settings_options = {
            "type": StringSettingItem(
                name="type", default_value="From Spanish", allowed_values=["From Spanish", "From English"]
            ),
            "masculinos": BoolSettingItem(name="masculinos", default_value="True"),
            "femeninas": BoolSettingItem(name="femeninas", default_value="True"),
        }

        self.settings_interface = SettingsInterface(self.settings_options, self._display)

        self.instructions = [
            "Enter: Show translation / next noun",
            "Right: Next noun",
            "Left: Previous noun",
            "Esc: Main menu"
        ]

        self.current_index = 0
        self.index_history = deque(maxlen=10)
        self.index_coverage = set()
        self.current_coverage = 0

        self.show_translation = False
        self.enter_state = 0
        
        self._select_noun()

    def _select_noun(self):
        iterations = 0
        max_iterations = 20

        while iterations < max_iterations:
            new_index = random.randint(0, len(self.nouns) - 1)
            noun = self.nouns[new_index]
            iterations += 1

            if self.settings_options["masculinos"].value == "False" and noun.gender == Gender.Masculine:
                continue
            if self.settings_options["femeninas"].value == "False" and not noun.gender == Gender.Feminine:
                continue
            
            self.index_history.append(self.current_index)
            self.current_index = new_index
            self.index_coverage.add(self.current_index)
            self.current_coverage = len(self.index_coverage) / len(self.nouns) * 100.0
            
            break
    
    def _previous_noun(self):
        if self.index_history:
            self.current_index = self.index_history.pop()

    @property
    def _current_noun(self) -> Noun:
        return self.nouns[self.current_index]

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.enter_state = (self.enter_state + 1) % 2
                        if self.enter_state == 1:
                            self.show_translation = True
                        else:
                            self._select_noun()
                            self.show_translation = False    
                    if event.key == pygame.K_RIGHT:
                        self._select_noun()
                        self.show_translation = False
                    if event.key == pygame.K_LEFT:
                        self._previous_noun()
                        self.show_translation = False    
                    if event.key == pygame.K_ESCAPE:
                        return  # Return to main menu

            self._display.screen.fill((255, 255, 255))

            source = self._current_noun.in_spanish if self.settings_options["type"].value == "From Spanish" else self._current_noun.in_english
            translation = self._current_noun.in_english if self.settings_options["type"].value == "From Spanish" else self._current_noun.in_spanish

            self._display.add_text_center(source)

            if self.show_translation:
                self._display.add_text_center(translation, size="M", color=(100, 100, 100), y_offset=80)

            for i, instruction in enumerate(self.instructions):
                self._display.add_text(instruction, "S", (0, 0, 0), (10, 10 + i * 30))
            
            self._display.add_text(f"{self.current_coverage:.2f} %", "S", (125, 125, 125), (self._display.screen.get_width() - 55, 10))

            pygame.display.flip()

    def settings(self):
        self.settings_interface.render()

