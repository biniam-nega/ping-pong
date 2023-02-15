import pygame

from game_status import GameStatus
from button import Button


def draw_surface(surface, rows):
    surface.fill((0, 0, 0))
    width = surface.get_rect().width
    delta = width // rows
    x = 0
    y = 0
    for i in range(rows):
        x += delta
        y += delta
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, width))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (width, y))


pygame.init()
surface = pygame.display.set_mode((500, 500))

# initialize variables
game_status = GameStatus.init
easy_button = Button(surface, 'Easy', (128, 128, 128), 100)
medium_button = Button(surface, 'Medium', (128, 128, 0), 200)
hard_button = Button(surface, 'Hard', (128, 0, 0), 300)
# end of initialize variables

# main game loop
while True:
    draw_surface(surface, 20)
    if game_status == GameStatus.init:
        easy_button.draw()
        medium_button.draw()
        hard_button.draw()

    elif game_status == GameStatus.easy:
        pass



    pygame.display.update()
