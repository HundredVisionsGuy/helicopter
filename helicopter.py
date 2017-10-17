#!/usr/bin/env python
#
# Hundred Visions Guy's Helicopter Game
# A simple helicopter game with physics and possibly AI
#
# Released under the GNU General Public License

VERSION = "0.1"

try:
    import sys
    import random
    import math
    import os
    import getopt
    import pygame
    from engine import *
    from socket import *
    from pygame.locals import *
except ImportError as err:
    print("couldn't load module. %s" % (err))
    sys.exit(2)
# Initialize variables
stageWidth = 1194
stageHeight = 600
gravity = .4
vy = 0
vx = 0
x = 0
y = 0
maxspeedG = 9
maxspeed = 6
friction = .92
def main():
    pygame.init()
    screen = pygame.display.set_mode((stageWidth, stageHeight))
    pygame.display.set_caption("Helicopter Game")

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((66, 122, 200))

    # Display text
    font = pygame.font.Font(None, 36)
    text = font.render("Yo!", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0,0))
    pygame.display.flip()

    helicopter = engine.load_png("helicopter.png")
    # Game Loop
    done = False
    while not done:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            done = True
            
            pygame.display.flip()

    # We're done, close window
    pygame.quit()
    
if __name__ == '__main__': main()

    ### ... which is the same size as our image
    ### now set the background to our space image
    ##screen.bgpic("desert.png")
    ##
    ### Or, set the shape of a turtle
    ##screen.addshape("helicopter.gif")
    ##turtle.shape("helicopter.gif")



    ##def slow():
    ##    vx *= friction
    ##    return vx
    ##def moveRight():
    ##    vx += .5
    ##    return vx
    ##def moveLeft():
    ##    vx -= .5
    ##    return vx
    ##def moveUp():
    ##    vy += .5
    ##    return vy
    ##def moveDown():
    ##    vy -= .5
    ##    return vy


    ##
    ### Game Loop ALGORITHM - need to convert to Pygame
    ##while True:
    ##    vy += gravity
    ##    x += vx
    ##    y += vy
    ##
    ##    if vy > maxspeedG:
    ##        vy = maxspeedG
    ##    elif vy < -maxspeed:
    ##        vy = -maxspeed
    ##
    ##    if vx > maxspeed:
    ##        vx = maxspeed
    ##    elif vx < -maxspeed:
    ##        vx = -maxspeed
    ##
    ##    if y > stageHeight:
    ##        y = stageHeight
    ##        vy = 0
    ##
    ##    vx = turtle.onkey(moveRight, "Right")
    ##    vx = turtle.onkey(moveLeft, "Left")
    ##    vx = turtle.onkey(slow)
    ##    vy = turtle.onkey(moveUp, "Up")
    ##    vy = turtle.onkey(moveDown, "Down")
    ##    screen.listen()
    ##    turtle.goto(x, y)
