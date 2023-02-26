import pygame as py


class Ball():
    def __init__(self, pp_settings, screen):
        '''Initialize the ball and set its starting position'''
        self.screen = screen
        self.pp_settings = pp_settings

        self.move_right = 1
        self.move_up = 0.3

        # Create a ball at (0, 0) and then set its correct position
        self.rect = py.Rect(0, 0, self.pp_settings.ball_height, self.pp_settings.ball_width)
        self.screen_rect = self.screen.get_rect()
        self.rect.centery = self.screen_rect.centery
        self.rect.centerx = self.screen_rect.centerx

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.color = self.pp_settings.ball_color

    def blitme(self):
        '''Draw the ball at its current position'''
        py.draw.rect(self.screen, self.color, self.rect)

    def update(self, stats):
        '''Update the position of the ball based on the current position'''
        if stats.game_active:
            self.centery += self.move_up
            self.centerx += self.move_right
            self.rect.centerx = self.centerx
            self.rect.centery = self.centery

    def check_edges(self):
        '''Return true if the ball is at the edge of the screen'''
        screen_rect = self.screen.get_rect()
        if self.rect.y <= 0 or self.rect.bottom > self.screen_rect.bottom:
            return True

    def center_ball(self):
        '''Center the ball in the middle of the screen'''
        self.centery = self.screen_rect.centery
        self.centerx = self.screen_rect.centerx
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
