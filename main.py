"""
Save MacGyver !
A Game in wich we must help MacGyver finding is way around a maze
in order to escape he must reach the exit, but before then he must
pick up objects along the way in order to conceive a siringue of chemical
so he can put to sleep the guard at the exit !

 Python Script
 Files : maze.py, items.py, constantes.py, player.py , level_1.txt , Images + sound
 """

import pygame
from pygame.locals import *
from constant import *
from maze import *
from items import *
from player import *
import time

def end(x,y):
	if maze.structure[x][y] == 'A':
		if mg_player.inventory == 3:
			window.blit(winner, (50, 50))
		else:
			window.blit(looser, (50, 50))
		pygame.display.flip()
		pygame.time.delay(5000)
		return False
	else:
		return True

pygame.init()
window = pygame.display.set_mode((SPRITE, SPRITE))
ground = pygame.image.load(GROUND).convert()
looser = pygame.image.load(LOOSE).convert_alpha()
winner = pygame.image.load(WIN).convert_alpha()
homepage = pygame.image.load(HOMEP).convert()


game = False
home = True


while home:

	window.blit(homepage , (0, 0))
	pygame.display.flip()
	pygame.display.update()
	pygame.time.Clock().tick(30)
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == K_RETURN:
				home = False
				game = True
			elif event.key == K_ESCAPE:
				home = False
				pygame.quit()
				quit()


	while game:
		"""Generation of level by file"""
		maze = Maze("Level_1.txt")
		maze.displaying(window)
		background = pygame.image.load(BACKGROUND).convert()

		"""Creation of player"""
		mg_player = Player(maze.structure)
		img_macgyver = pygame.image.load(mg_player.p_mg).convert()
		looser = pygame.image.load(LOOSE).convert_alpha()
		winner = pygame.image.load(WIN).convert_alpha()
		"""placement of the items"""
		tube = Items(TUBE, maze)
		syringe = Items(SYRINGE, maze)
		ether = Items(ETHER, maze)
		pygame.time.Clock().tick(30)
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					HOME = False
					pygame.quit()
					quit()

				#control for player
				elif event.key == pygame.K_UP:
					mg_player.move("up")

				elif event.key == pygame.K_RIGHT:
					mg_player.move("right")
			
				elif event.key == pygame.K_LEFT:
					mg_player.move("left")

				elif event.key == pygame.K_DOWN:
					mg_player.move("down") 

		window.blit(background, (0 , 0))
		maze.displaying(window)
		window.blit(img_macgyver, (mg_player.case_x, mg_player.case_y))
		if(maze.structure[tube.case_y][tube.case_x] == 'i'):
			window.blit(tube.image, (tube.x, tube.y))
		if(maze.structure[ether.case_y][ether.case_x] == 'i'):
			window.blit(ether.image, (ether.x, ether.y))
		if(maze.structure[syringe.case_y][syringe.case_x] == 'i'):
			window.blit(syringe.image, (syringe.x, syringe.y))
		pygame.display.flip()
		game = end(mg_player.case_y, mg_player.case_x)



	


