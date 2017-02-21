import pygame, sys
from pygame.locals import *
from constants import *


#SETUP
FPS = 60

FPSCLOCK = pygame.time.Clock()

pygame.init()
DISPLAYSURF = pygame.display.set_mode((DISPLAYWIDTH,DISPLAYHEIGHT))
pygame.display.set_caption(GAMENAME)

#MAIN GAME LOOP


def makeGrid(display, width, height, spacing):
    for x in range(0, width, spacing):
        pygame.draw.line(display, GRIDCOLOR, (x, 0), (x, height))

    for y in range(0, height, spacing):
        pygame.draw.line(display, GRIDCOLOR, (0, y), (width, y))


def makeButtons(display, width, height, color1, color2):
    for x in range(0, width, GRIDSPACING):
        for y in range(0, height, GRIDSPACING):
            make_button(display, x+1, x + GRIDSPACING - 1, y + 1, y + GRIDSPACING - 1, color1, color2, "", 12, WHITE)


def makeCoordLabels(display):
    get_text(display,  'A', GAMEFONT, GRIDFONTSIZE, False, GRIDCOLOR, UIBACKGROUNDCOLOR, ( 20, 475))
    get_text(display,  'B', GAMEFONT, GRIDFONTSIZE, False, GRIDCOLOR, UIBACKGROUNDCOLOR, ( 66, 475))
    get_text(display,  'C', GAMEFONT, GRIDFONTSIZE, False, GRIDCOLOR, UIBACKGROUNDCOLOR, (111, 475))
    get_text(display,  'D', GAMEFONT, GRIDFONTSIZE, False, GRIDCOLOR, UIBACKGROUNDCOLOR, (156, 475))
    get_text(display,  'E', GAMEFONT, GRIDFONTSIZE, False, GRIDCOLOR, UIBACKGROUNDCOLOR, (201, 475))
    get_text(display,  'F', GAMEFONT, GRIDFONTSIZE, False, GRIDCOLOR, UIBACKGROUNDCOLOR, (246, 475))
    get_text(display,  'H', GAMEFONT, GRIDFONTSIZE, False, GRIDCOLOR, UIBACKGROUNDCOLOR, (336, 475))
    get_text(display,  'G', GAMEFONT, GRIDFONTSIZE, False, GRIDCOLOR, UIBACKGROUNDCOLOR, (291, 475))
    get_text(display,  'I', GAMEFONT, GRIDFONTSIZE, False, GRIDCOLOR, UIBACKGROUNDCOLOR, (381, 475))
    get_text(display,  'J', GAMEFONT, GRIDFONTSIZE, False, GRIDCOLOR, UIBACKGROUNDCOLOR, (426, 475))
    # -----------------------------------------------------------------------------------------------
    get_text(display,  '1', GAMEFONT, GRIDFONTSIZE, False, GRIDCOLOR, UIBACKGROUNDCOLOR, (476,  25))
    get_text(display,  '2', GAMEFONT, GRIDFONTSIZE, False, GRIDCOLOR, UIBACKGROUNDCOLOR, (476,  70))
    get_text(display,  '3', GAMEFONT, GRIDFONTSIZE, False, GRIDCOLOR, UIBACKGROUNDCOLOR, (476, 115))
    get_text(display,  '4', GAMEFONT, GRIDFONTSIZE, False, GRIDCOLOR, UIBACKGROUNDCOLOR, (476, 160))
    get_text(display,  '5', GAMEFONT, GRIDFONTSIZE, False, GRIDCOLOR, UIBACKGROUNDCOLOR, (476, 205))
    get_text(display,  '6', GAMEFONT, GRIDFONTSIZE, False, GRIDCOLOR, UIBACKGROUNDCOLOR, (476, 250))
    get_text(display,  '7', GAMEFONT, GRIDFONTSIZE, False, GRIDCOLOR, UIBACKGROUNDCOLOR, (476, 295))
    get_text(display,  '8', GAMEFONT, GRIDFONTSIZE, False, GRIDCOLOR, UIBACKGROUNDCOLOR, (476, 340))
    get_text(display,  '9', GAMEFONT, GRIDFONTSIZE, False, GRIDCOLOR, UIBACKGROUNDCOLOR, (476, 385))
    get_text(display, '10', GAMEFONT, GRIDFONTSIZE, False, GRIDCOLOR, UIBACKGROUNDCOLOR, (476, 430))


def drawGUI(display):
    makeGrid(display, GRIDWIDTH, GRIDHEIGHT, GRIDSPACING)
    makeCoordLabels(display)
    makeButtons(display, GRIDWIDTH, GRIDHEIGHT, UIBACKGROUNDCOLOR, GREEN)

    pygame.draw.line(display, GRIDCOLOR, (451, 0), (451, 451))
    pygame.draw.line(display, GRIDCOLOR, (0, 451), (451, 451))

    pygame.draw.line(display, GRIDCOLOR, (500, 0), (500, DISPLAYHEIGHT))
    pygame.draw.line(display, GRIDCOLOR, (501, 0), (501, DISPLAYHEIGHT))
    pygame.draw.line(display, GRIDCOLOR, (502, 0), (502, DISPLAYHEIGHT))


def main():
    DISPLAYSURF.fill(UIBACKGROUNDCOLOR)
    while True:
        mouseClicked = pygame.mouse.get_pressed()
        mousePos = pygame.mouse.get_pos()
        drawGUI(DISPLAYSURF)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        FPSCLOCK.tick(FPS)
        pygame.display.update()

main()