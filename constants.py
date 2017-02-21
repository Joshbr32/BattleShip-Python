import pygame, random
#ColourS      R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (245,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
LIGHTBLUE= ( 52, 204, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
BLACK    = (  0,   0,   0)
STORMGRAY= (125, 152, 181)
DARKRED  = (189,   0,   0)

#CONSTANTS
GAMENAME = 'BattleShip'
DISPLAYWIDTH = 750
DISPLAYHEIGHT = 500
DISPLAYCAPTION = GAMENAME
UIBACKGROUNDCOLOR = NAVYBLUE
GRIDCOLOR= WHITE
GRIDWIDTH = 450
GRIDHEIGHT = 450
GRIDSPACING = 45
GAMEFONT = 'impact'
GRIDFONTSIZE = 30


#FUNCTIONS
def random_colour():
    '''
    Returns a random colour.
    '''
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

def get_text(surface, text, textFont, fontSize, antiAliasing, textColour, backgroundColour, coords):
    '''
    Draws: A string of text to the surface.
    text: String - The text you want to print to the surface.
    textFont: String - Font of the text.
    fontSize: Int - Size of the text.
    antiAliasing: Boolean - True if you want text to be unaliased, False if you want text to be aliased.
    textColour: Tuple (Look at the list of colours above) - Colour of text.
    backgroundColour: Tuple (Look at the list of colours above) - Colour of background rect.
    coords: Tuple: Coordinates of the center of the text.
    '''
    text_font = pygame.font.SysFont(textFont, fontSize)
    textSurfaceObj = text_font.render(text, antiAliasing, textColour, backgroundColour)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = coords
    surface.blit(textSurfaceObj, textRectObj)

#FUNCTIONS
def make_button(surface, leftX,rightX,topY,bottomY, colour, highlightColour, text, textSize, textColour):
    '''
    Makes a rectangular button
    leftX: x coordinate of the left side
    rightX: x coordinate of the right side
    topY: y coordinate of the top side
    bottomY: y coordinate of the bottom side
    colour: colour of the button
    highlightColour: colour of the button when highlighted
    text: text on the button
    textSize: Size of the text on the button
    action: What should be returned.
    '''
    mousePos = pygame.mouse.get_pos()
    mouseClicked = pygame.mouse.get_pressed()
    #print mouseClicked
    #print mousePos
    width = rightX - leftX
    height = bottomY - topY
    if leftX-1 < mousePos[0] < rightX+1 and topY-1 < mousePos[1] < bottomY+1:
        pygame.draw.rect(surface, BLACK, (leftX, topY, width, height))
        pygame.draw.rect(surface, highlightColour, (leftX,topY,width,height))
        get_text(surface, text, 'impact', textSize, True, textColour, highlightColour, ((leftX + rightX) / 2, (topY + bottomY) / 2))
        if mouseClicked[0] == 1:
            return True
    else:
        pygame.draw.rect(surface, BLACK, (leftX, topY, width , height))
        pygame.draw.rect(surface, colour, (leftX,topY,width,height))
        get_text(surface, text, 'impact', textSize, True, textColour, colour, ((leftX+rightX)/2, (topY+bottomY)/2))