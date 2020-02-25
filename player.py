"""file who contains class player"""


from maze import *
from constant import *


class Player():

	def __init__(self, maze):
		self.p_mg = MG
		self.case_x = 0
		self.case_y = 0
		self.num_x = 0
		self.num_y = 0
		self.maze = maze

	#function of moving the player
	def move(self, direction):
		if direction == "right":
			if self.num_x < (HEIGTH_SPRITE - 1):
				if self.maze[self.num_y][self.num_x+1] != 'X':
						self.num_x += 1
						self.case_x = self.num_x * HEIGTH_SPRITE

		if direction == "left":
				if self.num_x > 0:
					if self.maze[self.num_y][self.num_x-1] != 'X':
						self.num_x -= 1
						self.case_x = self.num_x * HEIGTH_SPRITE

		if direction == "up":
			if self.num_y > 0:
				if self.maze[self.num_y-1][self.num_x] != 'X':
					self.num_y -= 1
					self.case_y = self.num_y * HEIGTH_SPRITE

		if direction == "down":
			if self.num_y < (HEIGTH_SPRITE - 1):
				if self.maze[self.num_y+1][self.num_x] != 'X':
					self.num_y += 1
				self.case_y = self.num_y * HEIGTH_SPRITE
