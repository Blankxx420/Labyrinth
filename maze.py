"""File that contains maze class"""
import pygame
from pygame.locals import *
from constant import *

class Maze:
	def __init__(self, file):
		self.file = file
		self.structure = 0
		self.free_path = set()
		self.__get_maze()

	def __get_maze(self):
		with open(self.file , 'r') as file:
			mymaze =[]
			#we read the text file line by line
			num_line = 0
			for line in file:
				line_level = []
				num_char = 0
				#we look at each letters for each line
				for char in line:
					#we ignore \n at the end of lines
					if char != '\n':
						# we add each line in list
						line_level.append(char)
						#checking if letters in file are "@"
						if char == '@':
							#if it's @ add the position of the line and the letter in list set()	
							self.free_path.add((num_line, num_char))
					num_char += 1
				num_line += 1
				#in the list of line we add letters in another list inside
				mymaze.append(line_level)
				num_char += 1

			#we save the structure of the levels
			self.structure = mymaze


		
			


	def displaying(self, window):
		""" loading image of level"""
		wall = pygame.image.load(WALL).convert()
		start = pygame.image.load(START).convert()
		guardian = pygame.image.load(GUARDIAN).convert()
		ground = pygame.image.load(GROUND).convert()
		
		#we browse the list of structure
		num_line = 0
		for line in self.structure:
		 	num_char = 0
		 	for char in line:
		 		#calculating the real postion in pixel
		 		x = num_line * HEIGTH_SPRITE
		 		y = num_char * HEIGTH_SPRITE

		 		if char == 'X':
		 			window.blit(wall, (y,x)) #X == wall
		 			
		 		elif char == 'B':
		 			window.blit(start, (y,x)) #B = start of the game
		 
		 		elif char == 'A':
		 			window.blit(guardian, (y,x)) #A = arrival

		 		elif char == '@':
		 			window.blit(ground, (y,x)) 
		 		num_char += 1
		 	num_line += 1

	


	

	
	








			


		
				