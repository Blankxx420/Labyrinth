""" file that contain class items """
import pygame
from pygame.locals import *
from constant import *
from random import *


class Items:
    """Constructor of Items with module random.sample"""
    def __init__(self, image, maze):
        # loading sprite for items
        self.image = pygame.image.load(image).convert_alpha()
        # level where items is
        self.maze = maze
        self.case_x = 0
        self.case_y = 0

        free = sample(maze.free_path, 1)
        maze.free_path.remove(free[0])
        y = free[0][0]
        x = free[0][1]
        # change @ to 'i' in file for free
        self.maze.structure[y][x] = 'i'

        self.case_x = x
        self.case_y = y
        # calculating the real position in pixels
        self.x = self.case_x * 30
        self.y = self.case_y * 30
