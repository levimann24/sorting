import pygame


class Bars:
    def __init__(self, main, height, x):
        self.settings = main.settings
        self.screen = main.screen
        self.screen_rect = self.screen.get_rect()
        self.height = height
        self.border_color = (0, 0, 0)

        self.color = self.settings.bar_color

        # initialization
        self.rect = pygame.Rect(x, 0, self.settings.bar_width, self.height)
        self.border = pygame.Rect(x, 0, self.settings.bar_width, self.height)
        self.rect.bottom = self.screen_rect.bottom
        self.border.bottom = self.screen_rect.bottom
        self.x = self.rect.x
        self.y = self.rect.y

    def move_bar(self, x):
        self.x = x
        self.rect.x = self.x
        self.border.x = self.x

    def draw_bar(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, self.border_color, self.border, 1)
