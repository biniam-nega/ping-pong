import random
import tkinter as tk
from tkinter import messagebox

import pygame


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


def get_random_pos(rows, snake, obstacle=None):
    if not obstacle:
        obstacle = list()
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda cube: cube.pos == (x, y), snake.body))) or \
                len(list(filter(lambda cube: cube.pos == (x, y), obstacle))):
            continue
        break
    return x, y


def message_box(subject, content):
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass
