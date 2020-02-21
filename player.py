import pygame
from maze import *
from constant import *
from items import *
class Player():

	def __init__(self, maze):
		self.mg = MG
		self.x = 0
		self.y = 0
		self.num_x = 0
		self.num_y = 0
		self.maze = maze
		

	def move(self , direction):
		if direction == "right":
			if self.num_x < (heigth_sprite - 1):
				if self.maze[self.num_y][self.num_x+1] != 'X': 
						self.num_x += 1
						self.x = self.num_x * heigth_sprite
						
		if direction == "left":
				if self.num_x > 0:
					if self.maze[self.num_y][self.num_x-1] != 'X': 
						self.num_x -= 1
						self.x = self.num_x * heigth_sprite
				

		if direction == "up":
			if self.num_y > 0:
				if self.maze[self.num_y-1][self.num_x] != 'X':
					self.num_y -= 1
					self.y = self.num_y * heigth_sprite
				

		if direction == "down":
			if self.num_y < (heigth_sprite - 1):
				if self.maze[self.num_y+1][self.num_x] != 'X':
					self.num_y += 1
				self.y = self.num_y * heigth_sprite