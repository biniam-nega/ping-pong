import pygame

from snake2.cube import Cube
from snake2.game_functions import get_random_pos, message_box
from snake2.game_status import GameStatus


class Snake:
    body = list()
    turns = dict()

    def __init__(self, surface, color, pos, dirx=1, diry=0, rows=20):
        self.surface = surface
        self.color = color
        self.head = Cube(pos, surface)
        self.body.append(self.head)
        self.rows = rows
        self.dirx = dirx
        self.diry = diry

    def move(self):
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.dirx = 0
                self.diry = -1
                self.turns[self.head.pos[:]] = [self.dirx, self.diry]
            elif keys[pygame.K_DOWN]:
                self.dirx = 0
                self.diry = 1
                self.turns[self.head.pos[:]] = [self.dirx, self.diry]
            elif keys[pygame.K_RIGHT]:
                self.dirx = 1
                self.diry = 0
                self.turns[self.head.pos[:]] = [self.dirx, self.diry]
            elif keys[pygame.K_LEFT]:
                self.dirx = -1
                self.diry = 0
                self.turns[self.head.pos[:]] = [self.dirx, self.diry]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns: # change the direction of the square
                turn = self.turns[p]
                c.dirx, c.diry = turn[0], turn[1]
                c.move()
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                if c.dirx == 1 and c.pos[0] >= self.rows - 1:
                    c.pos = (0, c.pos[1])
                elif c.dirx == -1 and c.pos[0] <= 0:
                    c.pos = (self.rows - 1, c.pos[1])
                elif c.diry == 1 and c.pos[1] >= self.rows - 1:
                    c.pos = (c.pos[0], 0)
                elif c.diry == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], self.rows - 1)
                else:
                    c.move()

    def draw(self):
        for c in self.body:
            c.draw()

    def check_snack(self, snack):
        snack = snack
        if self.head.pos == snack.pos:
            snack = Cube(get_random_pos(self.rows, self), self.surface, color=(0, 128, 0))
            self.add_body()
        return snack

    def add_body(self):
        tail = self.body[-1]
        dirx = tail.dirx
        diry = tail.diry
        if dirx == -1:
            cube = Cube((tail.pos[0] + 1, tail.pos[1]), self.surface, dirx=dirx, diry=diry)
        elif dirx == 1:
            cube = Cube((tail.pos[0] - 1, tail.pos[1]), self.surface, dirx=dirx, diry=diry)
        elif diry == -1:
            cube = Cube((tail.pos[0], tail.pos[1] + 1), self.surface, dirx=dirx, diry=diry)
        else:
            cube = Cube((tail.pos[0], tail.pos[1] - 1), self.surface, dirx=dirx, diry=diry)
        self.body.append(cube)

    def update(self):
        self.draw()
        self.move()
        return self.check_collision()

    def check_collision(self):
        head = self.head
        if len(list(filter(lambda c: c.pos == head.pos, self.body[1:]))):
            message_box('You\'ve lost!', 'Your score: ' + str(len(self.body)))
            return True
        return False

    def reset(self):
        self.body = []
        self.head = Cube((10, 10), self.surface)
        self.body.append(self.head)
        self.turns = {}
        self.dirx = 0
        self.diry = 0
