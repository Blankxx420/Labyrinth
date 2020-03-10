import pygame
from pygame.locals import *
from constant import *
from player import *
from items import *
class Maze:
	def __init__(self, file):
		self.file = file
		self.structure = 0
		self.free_path = set()
		self.__get_maze()

	def __get_maze(self):
		with open(self.file , 'r') as file:
			mymaze =[]
			num_line = 0
			for line in file:
				line_level = []
				num_char = 0
				for char in line:
					if char != '\n':
						line_level.append(char)
						if char == '@':
							self.free_path.add((num_line, num_char))
					num_char += 1
				num_line += 1
				mymaze.append(line_level)
				num_char += 1

			self.structure = mymaze


		
			


	def displaying(self, window):
		wall = pygame.image.load(WALL).convert()
		start = pygame.image.load(START).convert()
		guardian = pygame.image.load(GUARDIAN).convert()
		mg = pygame.image.load(MG).convert_alpha()
		ground = pygame.image.load(GROUND).convert()
		
		num_line = 0
		for line in self.structure:
		 	num_char = 0
		 	for char in line:
		 		x = num_line * HEIGTH_SPRITE
		 		y = num_char * HEIGTH_SPRITE

		 		if char == 'X':
		 			window.blit(wall, (y,x))

		 		elif char == 'B':
		 			window.blit(start, (y,x))

		 		elif char == 'A':
		 			window.blit(guardian, (y,x))

		 		elif char == '@':
		 			window.blit(ground, (y,x))
		 		num_char += 1
		 	num_line += 1

	


	

	
	








			


		
				