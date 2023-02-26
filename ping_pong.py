import pygame as py
from pygame.sprite import Group

from setting import Settings
from bat import Bat
from ball import Ball
from game_stats import GameStats
from button import Button
from score_board import ScoreBoard
import game_functions as gf


def run_game():
    # Initialize the game, settings and create a screen object
    py.init()
    pp_settings = Settings()
    screen = py.display.set_mode([pp_settings.screen_width, pp_settings.screen_height])
    # Make a button
    play_button = Button(screen, "Play")
    # Initialize game statistics
    stats = GameStats(pp_settings)
    # Create an instance of the score board
    sb = ScoreBoard(pp_settings, screen, stats)
    # Make the bats
    right_bat = Bat(pp_settings, screen, False)
    left_bat = Bat(pp_settings, screen, True)
    bats = Group()
    bats.add(right_bat)
    bats.add(left_bat)
    # Make the ball
    ball = Ball(pp_settings, screen)
    py.display.set_caption("Ping Pong")

    # Start the main loop for the game
    while True:
        # Watch for the keyboard events
        gf.check_events(stats, play_button, right_bat, left_bat, ball, sb)

        if stats.game_active:
            right_bat.update()
            left_bat.update()
            gf.update_ball(stats, bats, right_bat, left_bat, sb, ball)
        gf.update_screen(pp_settings, screen, right_bat, left_bat, ball, stats, sb, play_button)


run_game()
