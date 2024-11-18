import pygame
import random
from collections import deque

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
            "Enter: Show translation / next verb",
            "Right: Next verb",
            "Left: Previous verb",
            "Esc: Main menu"
        ]

        self.current_index = 0
        self.index_history = deque(maxlen=10)

        self.show_translation = False
        self.enter_state = 0
        
        self._select_verb()

    def _select_verb(self):
        iterations = 0
        max_iterations = 20

        while iterations < max_iterations:
            new_index = random.randint(0, len(self.verbs) - 1)
            verb = self.verbs[new_index]
            iterations += 1

            if self.settings_options["regulares"].value == "False" and verb.is_regular:
                continue
            if self.settings_options["irregulares"].value == "False" and not verb.is_regular:
                continue
            if self.settings_options["reflexivos"].value == "False" and verb.is_reflexive:
                continue
            
            self.index_history.append(self.current_index)
            self.current_index = new_index

            break

    def _previous_verb(self):
        if self.index_history:
            self.current_index = self.index_history.pop()

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
                        self.enter_state = (self.enter_state + 1) % 2
                        if self.enter_state == 1:
                            self.show_translation = True
                        else:
                            self._select_noun()
                            self.show_translation = False
                    if event.key == pygame.K_RIGHT:
                        self._select_verb()
                        self.show_translation = False
                    if event.key == pygame.K_LEFT:
                        self._previous_verb()
                        self.show_translation = False
                    if event.key == pygame.K_ESCAPE:
                        return  # Return to main menu

            self._display.screen.fill((255, 255, 255))

            source = self._current_verb.name if self.settings_options["type"].value == "From Spanish" else self._current_verb.EN
            translation = self._current_verb.EN if self.settings_options["type"].value == "From Spanish" else self._current_verb.name

            self._display.add_text_center(source)

            if self.show_translation:
                self._display.add_text_center(translation, size="M", color=(100, 100, 100), y_offset=80)

            for i, instruction in enumerate(self.instructions):
                self._display.add_text(instruction, "S", (0, 0, 0), (10, 10 + i * 30))

            pygame.display.flip()

    def settings(self):
        self.settings_interface.render()

