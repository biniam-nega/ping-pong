class Settings:
    def __init__(self):
        # Screen settings
        self.screen_height = 600
        self.screen_width = 800
        self.bg_color = [100, 100, 100]

        # Bat settings
        self.bat_speed = 1
        self.bat_height = 100
        self.bat_width = 10
        self.bat_color = (0, 0, 0)

        # Ball settings
        self.ball_speed_factor = 1
        self.ball_height = 10
        self.ball_width = 10
        self.ball_color = (30, 30, 30)
        self.balls_limit = 10

        # Scoring settings
        self.score_point = 1
