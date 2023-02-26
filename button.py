import pygame.font
import pygame as py


class Button:
    def __init__(self, screen, msg):
        '''Initialize button attributes'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        print(self.screen_rect.width)

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (50, 50, 50)
        self.text_color = (255, 255, 255)
        self.font = py.font.SysFont(None, 48)

        # Build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped once
        self.prep_message(msg)

    def prep_message(self, msg):
        '''Turn msg into a rendered image and centers text on the button'''
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw a blank button then draw message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
