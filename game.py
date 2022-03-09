from lib2to3.pytree import Node
import pygame
import math
import itertools
from utils import board

#initialize screen
width, height = 800, 800
screen = pygame.display.set_mode((width,height))
events = pygame.event.get()

def infoScreen():
    pygame.display.set_caption('Maze Runner: the impossible level -- Information Screen')
    infoScreen = pygame.image.load("infoScreen.jpg")
    screen.blit(infoScreen, (0,0))

def game(level, px, py, rx, ry):
    pygame.display.set_caption('Maze Runner: the impossible level')
    board.board.drawSquares(screen, level)
    board.board.drawOnBoard(screen, px, py, level, 'player.png')
    board.board.drawOnBoard(screen, rx, ry, level, 'robot.png')

#main game loop
level = 20
px, py, rx, ry = 0, 0, 0, 0
newPlayer = True
running = True
while(running):
    for event in pygame.event.get():
        #if the quit button is pressed
        if event.type == pygame.QUIT:
            running = False

        #while player is on info screen
        if(newPlayer):
            infoScreen()
            #if enter is pressed, continue to game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    newPlayer = False

        #game loop
        else:
            game(level, px, py, rx, ry)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    py-=1
                if event.key == pygame.K_DOWN:
                    py+=1
                if event.key == pygame.K_RIGHT:
                    px+=1
                if event.key == pygame.K_LEFT:
                    px-=1
                if event.key == pygame.K_w:
                    ry-=1
                if event.key == pygame.K_s:
                    ry+=1
                if event.key == pygame.K_d:
                    rx+=1
                if event.key == pygame.K_a:
                    rx-=1

    pygame.display.update()