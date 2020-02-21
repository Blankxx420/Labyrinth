import pygame
from pygame.locals import *
from maze import *
from constant import *
import time

pygame.init()

window = pygame.display.set_mode((sprite, sprite))
maze = Maze("Level_1.txt")
maze.get_maze()
mg_player = Player(maze.mymaze)
loot = Items(maze.mymaze)
GROUD = pygame.image.load(GROUND).convert()
LOOSER = pygame.image.load(LOOSE).convert_alpha()
WINNER = pygame.image.load(WIN).convert_alpha()
img_macgyver = pygame.image.load(mg_player.mg).convert()
img_tube = pygame.image.load(loot.tube).convert_alpha()
img_ether = pygame.image.load(loot.ether).convert_alpha()
img_syringe = pygame.image.load(loot.syringe).convert_alpha()
background = pygame.image.load(BACKGROUND).convert()
TubeNotPicked = True
EtherNotPicked = True
SyringeNotPicked = True

loot.random_pos(window)

HOME = True
GameWin = False
Game_loose = False
END = False
while HOME:

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

    # event for picking up object
	window.blit(img_tube, loot.positions[0])
	if (mg_player.x, mg_player.y) == loot.positions[0]:
		loot.positions[0] = ((14 * heigth_sprite), 0)
		TubeNotPicked = False
		

	window.blit(img_ether, loot.positions[1])
	if (mg_player.x, mg_player.y) == loot.positions[1]:
		loot.positions[1] = ((12 * heigth_sprite) , 0)
		EtherNotPicked = False
		

	window.blit(img_syringe, loot.positions[2])
	if (mg_player.x, mg_player.y) == loot.positions[2]:
		loot.positions[2] = ((13 * heigth_sprite) , 0)
		SyringeNotPicked = False

	window.blit(img_macgyver, (mg_player.x, mg_player.y))

	if maze.mymaze[mg_player.num_y][mg_player.num_x] == 'A':
		if TubeNotPicked is False and EtherNotPicked is False and SyringeNotPicked is False:
			GameWin = True
		else:
			Game_loose = True

	if GameWin is True:
		window.blit(WINNER, ((3 * heigth_sprite), 7))

	if Game_loose is True:		
		window.blit(GROUD, (0 , 0))
		window.blit(LOOSER, ((5 * heigth_sprite), 7)) 


	pygame.display.flip()
	pygame.display.update()
	




