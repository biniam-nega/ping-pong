import random

import pygame

from snake2.game_status import GameStatus
from snake2.button import Button
from snake2.snake import Snake
from snake2.cube import Cube
from snake2.game_functions import draw_surface, get_random_pos


pygame.init()
surface = pygame.display.set_mode((500, 500))

# initialize variables
game_status = GameStatus.medium
easy_button = Button(surface, 'Easy', (128, 128, 128), 100)
medium_button = Button(surface, 'Medium', (128, 128, 0), 200)
hard_button = Button(surface, 'Hard', (128, 0, 0), 300)

clock = pygame.time.Clock()

snake = Snake(surface, (255, 0, 0), (10, 10))
snack = Cube(get_random_pos(20, snake), surface, color=(0, 128, 0))
# end of initialize variables

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    pygame.time.delay(50)
    clock.tick(10)
    draw_surface(surface, 20)
    if game_status == GameStatus.init:
        easy_button.draw()
        medium_button.draw()
        hard_button.draw()

    elif game_status == GameStatus.easy:
        status = snake.update()
        game_status = GameStatus.init if status else game_status
        snack = snake.check_snack(snack)
        snack.draw()

    elif game_status == GameStatus.medium:
        status = snake.update()

    pygame.display.update()
