# Making a simple flappy bird game with Pygame Zero
# flappyBirdV2.1G
# storing the pipes to change easier
# added a game over and scoring
# added random

# initialise Pygame Zero
import pgzrun
from random import *

# initialize constants
WIDTH = 800
HEIGHT = 600
scrollSpeed = -1
gameOver = False
score = 0

    
# make bird
bird = Actor("bird")
bird.x = WIDTH*0.15
bird.y = HEIGHT*0.5
minGap = int((bird.height*1.5)+50)
# is this too small?
maxGap = int((bird.height*3.5)+50)

# make pipes
# pipe group 1
topPipe1 = Actor("top")
topPipe1.x = int(WIDTH*0.4)
topPipe1.y = randint(int(-(topPipe1.height*0.3)),int(topPipe1.height*0.05))
bottomPipe1 = Actor("bottom")
bottomPipe1.x = int(WIDTH*0.4)
bottomPipe1.y = (topPipe1.height+topPipe1.y) + randint(minGap,maxGap)
pipes1 = (topPipe1,bottomPipe1)

# pipe group 2
topPipe2 = Actor("top")
topPipe2.x = int(WIDTH*0.75)
topPipe2.y = randint(int(-(topPipe2.height*0.3)),int(topPipe2.height*0.05))
bottomPipe2 = Actor("bottom")
bottomPipe2.x = int(WIDTH*0.75)
bottomPipe2.y = (topPipe2.height+topPipe2.y) + randint(minGap,maxGap)
pipes2 = (topPipe2,bottomPipe2)

# pipe group 3
topPipe3 = Actor("top")
topPipe3.x = int(WIDTH*1.1)
topPipe3.y = randint(int(-(topPipe3.height*0.3)),int(topPipe3.height*0.05))
bottomPipe3 = Actor("bottom")
bottomPipe3.x = int(WIDTH*1.1)
bottomPipe3.y = (topPipe3.height+topPipe3.y) + randint(minGap,maxGap)
pipes3 = (topPipe3,bottomPipe3)

# pipe group 4


pipeList=[pipes1,pipes2,pipes3]

# draw everything to screen
def draw():
    if gameOver:
        screen.clear()
        screen.fill((0,0,0))
        screen.draw.text(f"Game Over\nYour score was {score}",center=(WIDTH*0.5,HEIGHT*0.5),align="left",color=(255,255,255), fontsize = 60)
    else:
        # set background image
        screen.blit("bg",(0,0))
        bird.draw()

        for pipes in pipeList:
            pipes[0].draw()
            pipes[1].draw()
        screen.draw.text(f"Score: {score}",topleft=(10,10),color=(0,0,0), fontsize = 30)


# updates everything
def update():
    global score,gameOver
    # updating bird
    bird.y = bird.y + 1

    # updating pipes
    for n,pipes in enumerate(pipeList):
        top = pipes[0]
        bottom = pipes[1]
        top.x = top.x + scrollSpeed
        bottom.x = bottom.x + scrollSpeed
        if top.x < (0-(top.width*0.5)):
            top.x = WIDTH
            bottom.x = WIDTH
            top.y = randint(int(-(top.height*0.3)),int(top.height*0.05))
            bottom.y = (top.height+top.y) + randint(minGap,maxGap)
            if not gameOver:
                score = score + 1
        pipeList[n] = (top,bottom)
    

    # bird hits bottom of screen
    if bird.y > HEIGHT:
        # reset
        gameOver = True

    for pipes in pipeList:
        if bird.colliderect(pipes[0]) or bird.colliderect(pipes[1]):
            gameOver = True
    
# moving
def on_mouse_down():
    bird.y = bird.y - 50

# runs everything
pgzrun.go() 
