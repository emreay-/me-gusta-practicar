import pygame

class Display:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 74)
        self.medium_font = pygame.font.Font(None, 50)
        self.small_font = pygame.font.Font(None, 25)

    def get_font(self, size: str) -> pygame.font.Font:
        _size = size.upper()
        if _size in ["L", "LARGE"]:
            return self.font
        if _size in ["M", "MEDIUM"]:
            return self.medium_font
        if _size in ["S", "SMALL"]:
            return self.small_font
        return self.font

    def render_text(self, text: str, size: str = "L", color = (0, 0, 0)) -> pygame.Surface:
        return self.get_font(size).render(text, True, color)
    
    def blit(self, surface, pos) -> None:
        self.screen.blit(surface, pos)

    def blit_center(self, surface: pygame.Surface, y_offset=0) -> None:
        self.blit(surface, (self.screen.get_width() // 2 - surface.get_width() // 2,
                            self.screen.get_height() // 2 - surface.get_height() // 2 + y_offset))

    def add_text(self, text, size: str, color, pos) -> None:
        self.blit(self.render_text(text, size, color), pos)

    def add_text_center(self, text: str, size: str = "L", color = (0, 0, 0), y_offset=0) -> None:
        self.blit_center(self.render_text(text, size, color), y_offset)