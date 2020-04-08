"""
Save MacGyver !
A Game in wich we must help MacGyver finding is way around a maze
in order to escape he must reach the exit, but before then he must
pick up objects along the way in order to conceive a siringue of chemical
so he can put to sleep the guard at the exit !

 Python Script
 Files : maze.py, items.py, constantes.py, player.py , level_1.txt , Images
 """

import pygame
from pygame.locals import *
from constant import *
from maze import *
from items import *
from player import *
import time


def end(y, x):
    """Function of winning condtion"""
    if maze.structure[y][x] == 'A':
        if mg_player.inventory == 3:
            window.blit(winner, (120, 120))
        else:
            window.blit(looser, (150, 150))
        pygame.display.flip()
        pygame.time.delay(3000)
        return False
    else:
        return True


pygame.init()
# setting the window
window = pygame.display.set_mode((SPRITE, SPRITE))
# load image of menu
homepage = pygame.image.load(HOMEP).convert()

game = False
home = True

# MAIN LOOP
while home:
    # homepage mmenu of the game
    window.blit(homepage, (0, 0))
    pygame.display.flip()
    pygame.display.update()

    # event for quiting menu and game
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_RETURN:
                home = False
                game = True
            elif event.key == K_ESCAPE:
                home = False
                pygame.quit()
                quit()

    # load of level 
    maze = Maze("Level_1.txt")
    # creation of items in level
    tube = Items(TUBE, maze)
    syringe = Items(SYRINGE, maze)
    ether = Items(ETHER, maze)
    # creation of player
    mg_player = Player(maze)
    looser = pygame.image.load(LOOSE).convert_alpha()
    winner = pygame.image.load(WIN).convert_alpha()
    # GAME LOOP
    while game:
        img_macgyver = pygame.image.load(mg_player.p_mg).convert()
        maze.displaying(window)
        # limitation speedc of the loop
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    HOME = False
                    pygame.quit()
                    quit()
                # control for player
                elif event.key == pygame.K_UP:
                    mg_player.move("up")

                elif event.key == pygame.K_RIGHT:
                    mg_player.move("right")

                elif event.key == pygame.K_LEFT:
                    mg_player.move("left")

                elif event.key == pygame.K_DOWN:
                    mg_player.move("down")
        # displaying image of player character
        window.blit(img_macgyver, (mg_player.case_x, mg_player.case_y))
        # verify in text file if "i" is present
        if(maze.structure[tube.case_y][tube.case_x] == 'i'):
            # if present display image at the "i" position
            window.blit(tube.image, (tube.x, tube.y))

        elif (maze.structure[tube.case_y][tube.case_x] == '@'):
            window.blit(tube.image, (400, 0))

        if(maze.structure[ether.case_y][ether.case_x] == 'i'):
            window.blit(ether.image, (ether.x, ether.y))

        elif (maze.structure[ether.case_y][ether.case_x] == '@'):
            window.blit(ether.image, (420, 0))

        if(maze.structure[syringe.case_y][syringe.case_x] == 'i'):
            window.blit(syringe.image, (syringe.x, syringe.y))

        elif (maze.structure[syringe.case_y][syringe.case_x] == '@'):
            window.blit(syringe.image, (380, 0))
        # if player is on A call function end
        game = end(mg_player.num_y, mg_player.num_x)

        pygame.display.flip()
        pygame.display.update()
