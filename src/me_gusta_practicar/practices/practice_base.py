import pygame

from me_gusta_practicar.ui.display import Display

__all__ = ["PracticeBase"]

class PracticeBase:
    def __init__(self, display: Display):
        self._display = display

    def run(self):
        raise NotImplementedError("Each practice must implement the run method")

    def settings(self):
        raise NotImplementedError("Each practice must implement the settings method")
