import pygame

from snake2.game_functions import message_box, get_random_pos
from snake2.cube import Cube


class Obstacle:
    def __init__(self, surface, snake, rows=20, random=False):
        self.surface = surface
        self.rows = rows
        self.snake = snake
        self.random = random
        self.body = list()
        self.color = (128, 128, 128)
        self.init()

    def init(self):
        if self.random:
            for i in range(self.rows // 2):
                self.body.append(Cube(get_random_pos(self.rows, self.snake, self.body), self.surface, color=self.color))
                self.body.append(Cube(get_random_pos(self.rows, self.snake, self.body), self.surface, color=self.color))
                self.body.append(Cube(get_random_pos(self.rows, self.snake, self.body), self.surface, color=self.color))
                self.body.append(Cube(get_random_pos(self.rows, self.snake, self.body), self.surface, color=self.color))
        else:
            for i in range(self.rows):
                self.body.append(Cube((i, 0), self.surface, color=self.color))
                self.body.append(Cube((i, self.rows - 1), self.surface, color=self.color))
                self.body.append(Cube((0, i), self.surface, color=self.color))
                self.body.append(Cube((self.rows - 1, i), self.surface, color=self.color))

    def draw(self):
        for c in self.body:
            c.draw()
        return self.check_collision()

    def check_collision(self):
        head = self.snake.head
        if len(list(filter(lambda c: c.pos == head.pos, self.body))):
            message_box('You lost!', 'Your Score: ' + str(len(self.snake.body)))
            self.snake.reset()
            return True
        return False
