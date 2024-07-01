from enum import Enum
from typing import Any, List, Dict

import pygame

from me_gusta_practicar.ui.display import Display

class SettingType(Enum):
    Bool = 1,
    String = 2

class ValidationError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class SettingItem:
    def __init__(self, name: str, setting_type: SettingType, default_value: Any, allowed_values: List[str]) -> None:
        self.name = name
        self.setting_type = setting_type
        self._default_value = default_value
        self._allowed_values = allowed_values
        self._current_idx = 0
        self.value = self._default_value

    def validate(self, value) -> str:
        if value not in self._allowed_values:
            raise ValidationError(f"{value} is not allowed for the setting item, allowed values are {self._allowed_values}")
        return value

    @property
    def allowed_values(self) -> List[str]:
        return self._allowed_values

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = self.validate(value)
        self._current_idx = self.allowed_values.index(self.value)

    def advance(self):
        self._current_idx += 1
        self._current_idx %= len(self.allowed_values)
        self._value = self.validate(self.allowed_values[self._current_idx])

class BoolSettingItem(SettingItem):
    def __init__(self, name: str, default_value: str) -> None:
        super().__init__(name, SettingType.Bool, default_value, ["True", "False"])

class StringSettingItem(SettingItem):
    def __init__(self, name: str, default_value: str, allowed_values: List[str]) -> None:
        super().__init__(name, SettingType.String, default_value, allowed_values)

class SettingsInterface:
    def __init__(self, settings: Dict[str, SettingItem], display) -> None:
        self._settings = settings
        self._current_setting_idx = 0
        self._display = display
    
    def _next_setting(self):
        self._current_setting_idx += 1
        self._current_setting_idx %= len(self._settings)
    
    def _prev_setting(self):
        self._current_setting_idx -= 1
        self._current_setting_idx %= len(self._settings)

    @property
    def _current_setting(self) -> SettingItem:
        return list(self._settings.values())[self._current_setting_idx]

    def render(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self._next_setting()
                    if event.key == pygame.K_UP:
                        self._prev_setting()
                    if event.key == pygame.K_RETURN:
                        self._current_setting.advance()
                    if event.key == pygame.K_ESCAPE:
                        return  # Return to main menu

            self._display.screen.fill((255, 255, 255))

            for i, (setting_key, setting_item) in enumerate(self._settings.items()):
                color = (0, 0, 0) if setting_key == self._current_setting.name else (100, 100, 100)
                text = self._display.medium_font.render(f"{setting_key}: {setting_item.value}", True, color)
                self._display.screen.blit(text, (self._display.screen.get_width() // 2 - text.get_width() // 2,
                                        100 + i * 50))

            instruction_text = self._display.small_font.render("Esc: Back to main menu", True, (0, 0, 0))
            self._display.screen.blit(instruction_text, (10, 10))

            pygame.display.flip()