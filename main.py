import random

import pygame

from snake2.game_status import GameStatus
from snake2.button import Button
from snake2.snake import Snake
from snake2.obstacle import Obstacle
from snake2.cube import Cube
from snake2.game_functions import draw_surface, get_random_pos


def check_play_button(current_status, buttons, pos, surface, snake, snack, obstacle):
    snack, obstacle = snack, obstacle
    status = current_status
    if status == GameStatus.init:
        for i, button in enumerate(buttons):
            if button.rect.collidepoint(pos[0], pos[1]):
                if i == 0:
                    status = GameStatus.easy
                elif i == 1:
                    status = GameStatus.medium
                else:
                    status = GameStatus.hard
                snack, obstacle = init_game(surface, status, snake)
                break
    return status, snack, obstacle


def init_game(surface, game_status, snake):
    pos = (0, 0)
    obstacle = None
    if game_status == GameStatus.easy:
        pos = get_random_pos(20, snake)
    elif game_status == GameStatus.medium:
        obstacle = Obstacle(surface, snake)
        pos = get_random_pos(20, snake, obstacle.body)
    elif game_status == GameStatus.hard:
        obstacle = Obstacle(surface, snake, random=True)
        pos = get_random_pos(20, snake, obstacle.body, rand=True)

    snack = Cube(pos, surface, color=(0, 128, 0))
    return snack, obstacle


pygame.init()
surface = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Snake By Biniam')

# initialize variables
game_status = GameStatus.init
current_status = False
easy_button = Button(surface, 'Easy', (128, 128, 128), 100)
medium_button = Button(surface, 'Medium', (128, 128, 0), 200)
hard_button = Button(surface, 'Hard', (128, 0, 0), 300)

clock = pygame.time.Clock()

snake = Snake(surface, (255, 0, 0), (10, 10))

snack, obstacle = init_game(surface, game_status, snake)
# end of initialize variables

# main game loop
while True:
    current_status = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y =pygame.mouse.get_pos()
            buttons = (easy_button, medium_button, hard_button)
            game_status, snack, obstacle = check_play_button(game_status, buttons, (x, y), surface, snake, snack, obstacle)

    pygame.time.delay(50)
    clock.tick(10)
    draw_surface(surface, 20)
    if game_status == GameStatus.init:
        easy_button.draw()
        medium_button.draw()
        hard_button.draw()

    elif game_status == GameStatus.easy:
        current_status = snake.update()
        snack = snake.check_snack(snack)
        snack.draw()

    elif game_status == GameStatus.medium:
        snake.obstacle = obstacle
        snack = snake.check_snack(snack)
        snack.draw()
        current_status = obstacle.draw() or snake.update()

    elif game_status == GameStatus.hard:
        snake.obstacle = obstacle
        snack = snake.check_snack(snack)
        snack.draw()
        current_status = obstacle.draw() or snake.update()
    game_status = GameStatus.init if current_status else game_status

    pygame.display.update()
