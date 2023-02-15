import pygame
import pygame.font


class Button:
    def __init__(self, surface, message, color, pos_x):
        self.surface = surface

        self.width, self.height = 200, 60
        self.button_color = color
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 40)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.surface.get_rect().centery, pos_x

        self.prep_message(message)

    def prep_message(self, message):
        self.message_image = self.font.render(message, True, self.text_color, self.button_color)
        self.message_image_rect = self.message_image.get_rect()
        self.message_image_rect.center = self.rect.center

    def draw(self):
        self.surface.fill(self.button_color, self.rect)
        self.surface.blit(self.message_image, self.message_image_rect)
