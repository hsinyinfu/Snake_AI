import pygame
from pygame.locals import *
#from PIL import Image
import sys

size = weight, height = (800, 800)

#redcircle = pygame.image.load("redcircle.png") #every circle 50*50 pix
#blackcircle = pygame.image.load("blackcircle.png")
candy = pygame.image.load("candy.png")
rock = pygame.image.load("rock.png")
snakeHead = pygame.image.load("snake_head.png")
snakeBody = pygame.image.load("snake_body.png")

step = weight/8
screen = None

def init():
    global screen
    pygame.init() #pygame init
    screen = pygame.display.set_mode(size) #pygame size setting
    screen.fill( (255,255,255) )

def draw( mapArray, headIndex ):
    #screen.fill( (255,255,255) )
    for y in range(len(mapArray)):
        for x in range(len(mapArray[y])):
            if (x,y) == headIndex :
                screen.blit(snakeHead, (x*step, y*step))
            elif mapArray[y][x] == 1:
                screen.blit(snakeBody, (x*step, y*step))
            elif mapArray[y][x] == 2:
                screen.blit(candy, (x*step, y*step))
            elif mapArray[y][x] == -1:
                screen.blit(rock, (x*step, y*step))
    pygame.display.update()
    #pygame.time.delay(1000)
