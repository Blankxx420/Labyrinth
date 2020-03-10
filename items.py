""" file that contain class items """
import pygame 
import random
from random import sample
from pygame.locals import *
from constant import *
from maze import *

class Items:
	def __init__(self, image, maze):
		self.image = pygame.image.load(image).convert_alpha()
		self.maze = maze
		self.case_x = 0
		self.case_y = 0

		free = sample(maze.free_path, 1)
		maze.free_path.remove(free[0])
		y = free[0][0]
		x = free[0][1]
		self.maze.structure[y][x] = 'i'

		self.case_x = x
		self.case_y = y
		self.x = self.case_x * 30
		self.y = self.case_y * 30
		
		
		
	


 