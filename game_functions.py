import sys
from time import sleep

import pygame as py


def check_keydown_events(event, right_bat, left_bat):
    # Controls for the right bat
    if event.key == py.K_UP:
        right_bat.moving_up = True
    elif event.key == py.K_DOWN:
        right_bat.moving_down = True

    # Controls for the left bat
    if event.key == py.K_w:
        left_bat.moving_up = True
    elif event.key == py.K_s:
        left_bat.moving_down = True


def check_keyup_events(event, right_bat, left_bat):
    # Controls for the right bat
    if event.key == py.K_UP:
        right_bat.moving_up = False
    elif event.key == py.K_DOWN:
        right_bat.moving_down = False

    # Controls for the left bat
    if event.key == py.K_w:
        left_bat.moving_up = False
    elif event.key == py.K_s:
        left_bat.moving_down = False


def check_events(stats, play_button, right_bat, left_bat, ball, sb):
    '''Respond to key presses and mouse events'''
    for event in py.event.get():
        if event.type == py.QUIT or event.type == py.K_q:
            sys.exit()

        elif event.type == py.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = py.mouse.get_pos()
            check_play_button(stats, play_button, right_bat, left_bat, ball, sb, mouse_x, mouse_y)

        # Check keydown events
        elif event.type == py.KEYDOWN:
            check_keydown_events(event, right_bat, left_bat)

        # Check keyup events
        elif event.type == py.KEYUP:
            check_keyup_events(event, right_bat, left_bat)


def check_play_button(stats, play_button, right_bat, left_bat, ball, sb, mouse_x, mouse_y):
    '''Start a new game when the player clicks play'''
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        # Reset the game statistics
        stats.reset_stats()
        sb.prep_score()
        # Center the objects
        center_objects(right_bat, left_bat, ball)
        # Hide the mouse cursor.
        py.mouse.set_visible(False)

        stats.game_active = True


def update_screen(pp_settings, screen, right_bat, left_bat, ball, stats, sb, play_button):
    '''Update the images on the screen and flip to the new screen'''
    # Color the screen during each pass through the loop
    screen.fill(pp_settings.bg_color)

    # Draw the score board information
    sb.show_score()

    right_bat.blitme()
    left_bat.blitme()

    ball.update(stats)
    ball.blitme()

    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible
    py.display.flip()


def update_ball(stats, bats, right_bat, left_bat, sb, ball):
    '''Respond appropriately if the ball collides with the edge or the bats'''
    if ball.rect.x <= 0:
        ball_missed(stats, right_bat, left_bat, sb, ball, 0)
    elif ball.rect.right >= ball.screen_rect.right:
        ball_missed(stats, right_bat, left_bat, sb, ball, 1)

    if ball.check_edges():
        change_ball_direction(ball, 0)
    check_bat_ball_collision(bats, ball)


def change_ball_direction(ball, state):
    if state == 0:
        ball.move_up *= -1
    elif state == 1:
        ball.move_right *= -1


def check_bat_ball_collision(bats, ball):
    # Bounce the ball along the x-direction if it hits any bat
    collisions = py.sprite.spritecollideany(ball, bats)
    if collisions:
        change_ball_direction(ball, 1)


def ball_missed(stats, right_bat, left_bat, sb, ball, state):
    '''Respond to a ball being missed'''
    stats.balls_left -= 1
    if stats.balls_left > 0:
        print(stats.balls_left)
        # Center the objects
        center_objects(right_bat, left_bat, ball)

        # Update the score of each player
        if state == 0:
            stats.right_score += 1
        else:
            stats.left_score += 1
        sb.prep_score()
        # Pause
        sleep(1)

    else:
        center_objects(right_bat, left_bat, ball)
        stats.game_active = False
        py.mouse.set_visible(True)


def center_objects(right_bat, left_bat, ball):
    # Center the ball
    ball.center_ball()

    # Center the bats
    right_bat.center_bat()
    left_bat.center_bat()
