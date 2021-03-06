"""file that contains class player"""
from maze import *
from constant import *


class Player():
    """constructor class of the player"""
    def __init__(self, maze):
        self.p_mg = MG
        self.case_x = 0
        self.case_y = 0
        self.num_x = 0
        self.num_y = 0
        # level where is the player
        self.maze = maze
        self.inventory = 0

    # function of moving the player
    def move(self, direction):
        """ simple function for the player for moving"""
        #verify if player go on i
        if (self.maze.structure[self.num_y][self.num_x] == 'i'):
            # add 1 to the inventory
            self.inventory += 1
            # change the i to @ in file
            self.maze.structure[self.num_y][self.num_x] = '@'

        if direction == "right":
            # for not going out of the screen
            if self.num_x < (HEIGTH_SPRITE - 1):
                # checking it's not a wall
                if self.maze.structure[self.num_y][self.num_x+1] != 'X':
                    # moving of 1 case
                    self.num_x += 1
                    # calculate the real position in pixel
                    self.case_x = self.num_x * HEIGTH_SPRITE

        if direction == "left":
            if self.num_x > 0:
                if self.maze.structure[self.num_y][self.num_x-1] != 'X':
                    self.num_x -= 1
                    self.case_x = self.num_x * HEIGTH_SPRITE

        if direction == "up":
            if self.num_y > 0:
                if self.maze.structure[self.num_y-1][self.num_x] != 'X':
                    self.num_y -= 1
                    self.case_y = self.num_y * HEIGTH_SPRITE

        if direction == "down":
            if self.num_y < (HEIGTH_SPRITE - 1):
                if self.maze.structure[self.num_y+1][self.num_x] != 'X':
                    self.num_y += 1
                self.case_y = self.num_y * HEIGTH_SPRITE
