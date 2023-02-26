class GameStats:
    '''Track the statistics for the game'''
    def __init__(self, pp_settings):
        '''Initialize statistics'''
        self.pp_settings = pp_settings
        self.reset_stats()
        # Start the game in an active state
        self.game_active = False

    def reset_stats(self):
        '''Initialize statistics that can change during the game'''
        self.balls_left = self.pp_settings.balls_limit
        self.right_score = 0
        self.left_score = 0
