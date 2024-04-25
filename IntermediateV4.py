# pipes' y value decided based on a set gap and a central x value

# initialise Pygame Zero
import pgzrun
from random import *

# initialize constants
WIDTH = 800
HEIGHT = 600
# this should be from between 160 and 260 
gap = 210
# these values can be given
minX = 300-250+(gap//2)
maxX = 850-(300+gap//2)
scrollSpeed = -1
gameOver = False
score = 0

    
# make bird
bird = Actor("bird")
bird.x = 160
bird.y = 300

xs=[]
pipes=[]

x1 = randint(minX,maxX)
xs.append(x1)
topPipe1 = Actor("top")
topPipe1.x = 280
topPipe1.y = x1-(300+(gap//2))
pipes.append(topPipe1)
bottomPipe1 = Actor("bottom")
bottomPipe1.x = 280
bottomPipe1.y = x1 + 300 + (gap//2)
pipes.append(bottomPipe1)

x2 = randint(minX,maxX)
xs.append(x2)
topPipe2 = Actor("top")
topPipe2.x = 545
topPipe2.y = x2-(300+(gap//2))
pipes.append(topPipe2)
bottomPipe2 = Actor("bottom")
bottomPipe2.x = 545
bottomPipe2.y = x2 + 300 + (gap//2)
pipes.append(bottomPipe2)

x3 = randint(minX,maxX)
xs.append(x3)
topPipe3 = Actor("top")
topPipe3.x = 810
topPipe3.y = x3-(300+(gap//2))
pipes.append(topPipe3)
bottomPipe3 = Actor("bottom")
bottomPipe3.x = 810
bottomPipe3.y = x3 + 300 + (gap//2)
pipes.append(bottomPipe3)


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

        for pipe in pipes:
            pipe.draw()
        screen.draw.text(f"Score: {score}",topleft=(10,10),color=(0,0,0), fontsize = 30)


# updates everything
def update():
    global score,gameOver
    # updating bird
    bird.y = bird.y + 1

    # updating pipes
    for i in range(len(xs)):
        top = 2*i
        bottom = (2*i)+1
        pipes[top].x = pipes[top].x + scrollSpeed
        pipes[bottom].x = pipes[bottom].x + scrollSpeed
        if pipes[top].x < -44:
            pipes[top].x = WIDTH
            pipes[bottom].x = WIDTH
            xs[i] = randint(minX,maxX)
            pipes[top].y = xs[i]-(300+(gap//2))
            pipes[bottom].y = xs[i] + 300 + (gap//2)
            if not gameOver:
                score+=1
    

    # bird hits bottom of screen
    if bird.y > HEIGHT:
        # reset
        gameOver = True

    for pipe in pipes:
        if bird.colliderect(pipe):
            gameOver = True
    
    
# moving
def on_mouse_down():
    bird.y = bird.y - 50

# runs everything
pgzrun.go() 
