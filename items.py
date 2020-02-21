import pygame
from constant import *
from maze import *
import random

class Items:
	def __init__(self, maze):
		self.maze = maze
		self.tube = TUBE
		self.ether = ETHER
		self.syringe = SYRINGE
		self.loaded = True
		self.positions = []


	def random_pos(self, window):
		for x in range(3):
			while True:
				num_x = random.randrange(0, 14)
				num_y = random.randrange(0, 14)
				x = num_x * heigth_sprite
				y = num_y * heigth_sprite
				if self.maze[num_y][num_x] == '@' and (x, y) not in self.positions :
					print(num_x, num_y)
					self.positions.append((x, y))
					break