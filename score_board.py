import pygame.font


class ScoreBoard:
    '''A class to report the scoring information'''
    def __init__(self, pp_settings, screen, stats):
        '''Initialize the scorekeeping attribute'''
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.pp_settings = pp_settings
        self.stats = stats

        # Font settings for scoring information
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image
        self.prep_score()

    def prep_score(self):
        '''Turn the score into a rendered image'''
        score_right_str = str(self.stats.right_score)
        score_left_str = str(self.stats.left_score)
        self.right_score_image = self.font.render(score_right_str, True, self.text_color, self.pp_settings.bg_color)
        self.left_score_image = self.font.render(score_left_str, True, self.text_color, self.pp_settings.bg_color)
        # Display the scores at their respective corners
        self.right_score_rect = self.right_score_image.get_rect()
        self.right_score_rect.right = self.screen_rect.right - 10
        self.right_score_rect.top = 10

        self.left_score_rect = self.left_score_image.get_rect()
        self.left_score_rect.left = self.screen_rect.left + 10
        self.left_score_rect.top = 10

    def show_score(self):
        '''Draw the scores on the screen'''
        self.screen.blit(self.right_score_image, self.right_score_rect)
        self.screen.blit(self.left_score_image, self.left_score_rect)
