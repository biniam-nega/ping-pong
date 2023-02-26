import pygame as py
from pygame.sprite import Sprite


class Bat(Sprite):
    def __init__(self, pp_settings, screen, left):
        '''Initialize the bats and set their starting location'''
        super(Bat, self).__init__()
        self.screen = screen
        self.left = left
        self.pp_settings = pp_settings

        # Create a bat rect at (0, 0) and then set its correct position
        self.rect = py.Rect(0, 0, self.pp_settings.bat_width, pp_settings.bat_height)
        self.screen_rect = self.screen.get_rect()
        self.rect.centery = self.screen_rect.centery
        if self.left:
            self.rect.left = self.screen_rect.left + 20
        else:
            self.rect.right = self.screen_rect.right - 20

        self.color = self.pp_settings.bat_color

        # Movement flag of the ship
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        '''Draw the bat at its current position'''
        py.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        '''Update the postion of the bat based on the movement flag'''
        if self.moving_up and self.rect.y > 0:
            self.rect.centery -= self.pp_settings.bat_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.pp_settings.bat_speed

    def center_bat(self):
        '''Center the bat on the screen'''
        self.rect.centery = self.screen_rect.centery
