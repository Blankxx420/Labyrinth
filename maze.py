import pygame
from constant import *
from player import *
from items import *
class Maze:
	def __init__(self, file):
		self.file = file
		self.mymaze = []

	def get_maze(self):
		with open(self.file , 'r') as file:
			for line in file:
				line_level = []
				print(line_level)
				for char in line:
					if char != '\n':
						line_level.append(char)
				self.mymaze.append(line_level)
		
			


	def displaying(self, Window):
		wall = pygame.image.load(WALL).convert()
		start = pygame.image.load(START).convert()
		guardian = pygame.image.load(GUARDIAN).convert()
		mg = pygame.image.load(MG).convert_alpha()
		ground = pygame.image.load(GROUND).convert()
		
		num_line = 0
		for line in self.mymaze:
		 	num_char = 0
		 	for char in line:
		 		x = num_line * HEIGTH_SPRITE
		 		y = num_char * HEIGTH_SPRITE

		 		if char == 'X':
		 			Window.blit(wall, (y,x))

		 		elif char == 'B':
		 			Window.blit(start, (y,x))

		 		elif char == 'A':
		 			Window.blit(guardian, (y,x))

		 		elif char == '@':
		 			Window.blit(ground, (y,x))
		 		num_char += 1
		 	num_line += 1

	


	

	
	








			


		
				