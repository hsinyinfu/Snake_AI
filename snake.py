import pygame
from pygame.locals import *
import sys

size = width, height = (800, 800)

step = width/8
screen = None

def init():
    global screen
    pygame.init() #pygame init
    screen = pygame.display.set_mode(size) #pygame size setting
    #screen.fill( (255, 255, 255) )

def draw( mapArray, score, isOver):
    global screen
    screen.fill( (255,255,255) )
 
    for y in range(len(mapArray)):
        for x in range(len(mapArray[y])):
            if mapArray[y][x] == 1:
                pygame.draw.rect(screen, (0, 0, 0), Rect(x*step, y*step,
                    step,step))
            elif mapArray[y][x] == 2:
                pygame.draw.rect(screen, (255, 0, 0), Rect(x*step, y*step,
                     step,step))
            elif mapArray[y][x] == -1:
                pygame.draw.rect(screen, (150, 150, 150), Rect(x*step,
                    y*step, step,step))
    drawScore(score)
    if isOver:
        gameOver(screen)
    pygame.display.update()
    pygame.time.delay(300)

def drawScore(score):
    global width, screen
    scoreFont = pygame.font.SysFont("comicsansms", 100)
    scoreSurf = scoreFont.render('Score: %s' % (score), True, (0,0,0))
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (width/2, 10)
    screen.blit(scoreSurf, scoreRect)

def gameOver(screen):
    global width, height
    gameOverFont = pygame.font.SysFont("comicsansms", 100)
    gameOverSurf = gameOverFont.render('Game Over!', True, (255,0,0))
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.center = ((width/2),(height/3))
    screen.blit(gameOverSurf, gameOverRect)
