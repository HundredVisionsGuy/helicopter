import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
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

# Game Loop
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pygame.display.flip()

# We're done, close window
pygame.quit()
# this assures that the size of the screen will always be 400x400 ...

screen.setup(stageWidth, stageHeight)

# ... which is the same size as our image
# now set the background to our space image
screen.bgpic("desert.png")

# Or, set the shape of a turtle
screen.addshape("helicopter.gif")
turtle.shape("helicopter.gif")



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
