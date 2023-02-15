import pygame


class Cube:
    def __init__(self, pos, surface, rows=20, dirx=1, diry=0, color=(255, 0, 0)):
        self.surface = surface
        self.rows = rows
        self.pos = pos
        self.dirx = dirx
        self.diry = diry
        self.color = color

    def draw(self):
        width = self.surface.get_rect().width
        delta = width // self.rows
        x = self.pos[0]
        y = self.pos[1]
        pygame.draw.rect(self.surface, self.color, (x * delta + 1, y * delta + 1, delta - 2, delta - 2))

    def move(self):
        self.pos = (self.pos[0] + self.dirx, self.pos[1] + self.diry)
