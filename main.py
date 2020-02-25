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
from maze import *
from constant import *
import time



pygame.init()

Window = pygame.display.set_mode((SPRITE, SPRITE))

maze = Maze("Level_1.txt")

maze.get_maze()

mg_player = Player(maze.mymaze)

Loot = Items(maze.mymaze)

Ground = pygame.image.load(GROUND).convert()

Looser = pygame.image.load(LOOSE).convert_alpha()

Winner = pygame.image.load(WIN).convert_alpha()

Homepage = pygame.image.load(HOMEP).convert()

img_macgyver = pygame.image.load(mg_player.p_mg).convert()

img_tube = pygame.image.load(Loot.tube).convert_alpha()

img_ether = pygame.image.load(Loot.ether).convert_alpha()

img_syringe = pygame.image.load(Loot.syringe).convert_alpha()

background = pygame.image.load(BACKGROUND).convert()

Loot.random_pos(Window)

TubeNotPicked = True
EtherNotPicked = True
SyringeNotPicked = True
GAME = False
HOME = True
GameWin = False
Game_loose = False

while HOME:

	Window.blit(Homepage , (0, 0))
	pygame.display.flip()
	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == K_RETURN:
				HOME = False
				GAME = True
			elif event.key == K_ESCAPE:
				HOME = False
				pygame.quit()
				quit()


	while GAME:

		Background = pygame.image.load(BACKGROUND).convert()
		
		maze.displaying(Window)
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

		Window.blit(background, (0 , 0))
		maze.displaying(Window)
		pygame.key.set_repeat(400, 400)

	    # event for picking up object
		Window.blit(img_tube, Loot.positions[0])
		if (mg_player.case_x, mg_player.case_y) == Loot.positions[0]:
			Loot.positions[0] = ((14 * HEIGTH_SPRITE), 0)
			TubeNotPicked = False
			

		Window.blit(img_ether, Loot.positions[1])
		if (mg_player.case_x, mg_player.case_y) == Loot.positions[1]:
			Loot.positions[1] = ((12 * HEIGTH_SPRITE) , 0)
			EtherNotPicked = False
			

		Window.blit(img_syringe, Loot.positions[2])
		if (mg_player.case_x, mg_player.case_y) == Loot.positions[2]:
			Loot.positions[2] = ((13 * HEIGTH_SPRITE) , 0)
			SyringeNotPicked = False

		Window.blit(img_macgyver, (mg_player.case_x, mg_player.case_y))

		if maze.mymaze[mg_player.num_y][mg_player.num_x] == 'A':
			if TubeNotPicked is False and EtherNotPicked is False and SyringeNotPicked is False:
				GameWin = True
			else:
				Game_loose = True

		if GameWin is True:
			Window.blit(Ground, (0, 0))
			Window.blit(Winner, ((3 * HEIGTH_SPRITE), 7))
			if event.key == K_RETURN: 
				HOME = True
				GAME = False


		if Game_loose is True:		
			Window.blit(Ground, (0 , 0))
			Window.blit(Looser, ((5 * HEIGTH_SPRITE), 7))
			if event.key == K_RETURN:
				GAME = False
				HOME = True
			
			if event.key == K_n:
				GAME = False
				HOME = True


		pygame.display.flip()
		pygame.display.update()
	




