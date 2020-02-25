""" file that contain class items """
import random
from constant import *
from maze import *

class Items:
	def __init__(self, maze):
		self.maze = maze
		self.tube = TUBE
		self.ether = ETHER
		self.syringe = SYRINGE
		self.loaded = True
		self.positions = []

	def random_pos(self, Window):
		for x in range(3):
			while True:
				num_x = random.randrange(0, 14)
				num_y = random.randrange(0, 14)
				x = num_x * HEIGTH_SPRITE
				y = num_y * HEIGTH_SPRITE
				if self.maze[num_y][num_x] == '@' and (x, y) not in self.positions:
					self.positions.append((x, y))
					break
 