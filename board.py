import pygame
import math
import random

#variables
white = (255,255,255)
black = (0,0,0)
width, height = 800, 800

class board:
    def __init__(self):
        self.board = []
        self.selectedPath = None

    def drawSquares(win, level):
        win.fill(white)
        squares = (8*8)*level
        rows = int(math.sqrt(squares))
        size = height/rows
        for y in range(rows):
            for x in range(y % 2, rows, 2):
                pygame.draw.rect(win, black, (y*size, x*size, size, size))

    def drawOnBoard(win, x, y, level, file):
        squares = (8*8)*level
        rows = int(math.sqrt(squares))
        size = height/rows
        imageSize = (size*(3/4), size*(3/4))
        image = pygame.image.load(file)
        image = pygame.transform.scale(image, imageSize)
        xCor = size*x+((1/8)*size)
        yCor = size*y+((1/8)*size)
        win.blit(image, (xCor, yCor))


    def trapDoors(level):
        numOfDoors = random.randint(8*level-3, 8*level+3)
        doorX = random.randint(0, 8*level)
        doorY = random.randint(0, 8*level)

