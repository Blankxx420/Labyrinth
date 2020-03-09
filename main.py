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



pygame.init()
window = pygame.display.set_mode((SPRITE, SPRITE))
maze = Maze("Level_1.txt")
maze.get_maze()
mg_player = Player(maze.mymaze)
loot = Items(maze.mymaze)
ground = pygame.image.load(GROUND).convert()
looser = pygame.image.load(LOOSE).convert_alpha()
winner = pygame.image.load(WIN).convert_alpha()
homepage = pygame.image.load(HOMEP).convert()
img_macgyver = pygame.image.load(mg_player.p_mg).convert()
img_tube = pygame.image.load(loot.tube).convert_alpha()
img_ether = pygame.image.load(loot.ether).convert_alpha()
img_syringe = pygame.image.load(loot.syringe).convert_alpha()
background = pygame.image.load(BACKGROUND).convert()
loot.random_pos(window)
tubenotpicked = True
ethernotpicked = True
syringenotpicked = True
game = False
home = True
game_win = False
game_loose = False

while home:

	window.blit(homepage , (0, 0))
	pygame.display.flip()
	pygame.display.update()

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

		background = pygame.image.load(BACKGROUND).convert()
		
		maze.displaying(window)
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
		pygame.key.set_repeat(400, 400)

	    # event for picking up object
		window.blit(img_tube, loot.positions[0])
		if (mg_player.case_x, mg_player.case_y) == loot.positions[0]:
			loot.positions[0] = ((14 * HEIGTH_SPRITE), 0)
			tubenotpicked = False
			
			

		window.blit(img_ether, loot.positions[1])
		if (mg_player.case_x, mg_player.case_y) == loot.positions[1]:
			loot.positions[1] = ((12 * HEIGTH_SPRITE) , 0)
			ethernotpicked = False
			

		window.blit(img_syringe, loot.positions[2])
		if (mg_player.case_x, mg_player.case_y) == loot.positions[2]:
			loot.positions[2] = ((13 * HEIGTH_SPRITE) , 0)
			syringenotpicked = False
			

		window.blit(img_macgyver, (mg_player.case_x, mg_player.case_y))

		if maze.mymaze[mg_player.num_y][mg_player.num_x] == 'A':
			if tubenotpicked is False and ethernotpicked is False and syringenotpicked is False:
				game_win = True
			else:
				game_loose = True

		if game_win is True:
			window.blit(ground, (0, 0))
			window.blit(winner, ((3 * HEIGTH_SPRITE), 7))
			if event.key == K_RETURN:
				
				home = True
				game = False
				

		if game_loose is True:		
			window.blit(ground, (0 , 0))
			window.blit(looser, ((5 * HEIGTH_SPRITE), 7))
			if event.key == K_RETURN:
				game = False
				home = True
				
			
			if event.key == K_n:
				game = False
				home = False


		pygame.display.flip()
		pygame.display.update()
	




