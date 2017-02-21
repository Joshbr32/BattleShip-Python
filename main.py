import pygame
import GUI
pygame.init()
clock = pygame.time.Clock()
from Constants import *
from GUI import *

#constants
display_width = 750
display_height = 500
gameDisplay = pygame.display.set_mode((display_width, display_height))
backgroundColour = STORMGRAY
gameState = 'Start Screen'

gameOver = False
titleImg = pygame.image.load('Title.png')
ship1Img = pygame.image.load('Ship1.png')
ship2Img = pygame.image.load('Ship2.png')
ship3Img = pygame.image.load('Ship3.png')
ship4Img = pygame.image.load('Ship4.png')

def startScreen():

    gameDisplay.blit(titleImg, (x, y))
    gameDisplay.blit(ship4Img, (display_width *0.175, display_height *.65))
    make_button(gameDisplay, 125, 225, 250, 300, RED, DARKRED, 'Play', 30, WHITE)
    make_button(gameDisplay, 275, 475, 250, 300, RED, DARKRED, 'Instructions', 30, WHITE)
    make_button(gameDisplay, 525, 625, 250, 300, RED, DARKRED, 'Credits', 30, WHITE)



def Screen(x, y):
    if (gameState == 'Start Screen') :
        startScreen()
    elif (gameState == 'Game Mode'):
        drawGUI()
        makeGrid()
    elif (gameState == 'Instructions'):
        gameDisplay.blit(titleImg, (x, y))
    elif (gameState == 'Credits'):
        gameDisplay.blit(titleImg, (x, y))

x = (display_width *0.225)
y = (display_height *0.005)

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    gameDisplay.fill(backgroundColour)
    Screen(x, y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()