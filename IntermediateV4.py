import pgzrun
import sys
from random import *

# initialize constants
WIDTH = 800
HEIGHT = 600
score = 0
gap = 210
    
# make bird
bird = Actor("bird")
bird.x = 160
bird.y = 300

pipes=[]

y1 = randint(155,445)
topPipe1 = Actor("top")
topPipe1.x = 280
topPipe1.y = y1 - (300+(gap//2))
pipes.append(topPipe1)
bottomPipe1 = Actor("bottom")
bottomPipe1.x = 280
bottomPipe1.y = y1 + 300 + (gap//2)
pipes.append(bottomPipe1)

y2 = randint(155,445)
topPipe2 = Actor("top")
topPipe2.x = 545
topPipe2.y = y2 - (300+(gap//2))
pipes.append(topPipe2)
bottomPipe2 = Actor("bottom")
bottomPipe2.x = 545
bottomPipe2.y = y2 + 300 + (gap//2)
pipes.append(bottomPipe2)

y3 = randint(155,445)
topPipe3 = Actor("top")
topPipe3.x = 810
topPipe3.y = y3 - (300+(gap//2))
pipes.append(topPipe3)
bottomPipe3 = Actor("bottom")
bottomPipe3.x = 810
bottomPipe3.y = y3 + 300 + (gap//2)
pipes.append(bottomPipe3)

def draw():
    global score
    screen.blit("bg",(0,0))
    bird.draw()

    for pipe in pipes:
        pipe.draw()
    screen.draw.text(f"Score: {score}",topleft=(10,10),color=(0,0,0), fontsize = 30)
       
def update():
    global score
    bird.y = bird.y + 1

    for i in range((len(pipes)//2)):
        top = 2*i
        bottom = (2*i)+1
        pipes[top].x = pipes[top].x -1
        pipes[bottom].x = pipes[bottom].x -1
        if pipes[top].x < - 44:
            pipes[top].x = WIDTH
            pipes[bottom].x = WIDTH
            score = score + 1
            tempy = randint(155,445)
            pipes[top].y = tempy - (300 + (gap//2))
            pipes[bottom].y = tempy + 300 + (gap//2)


    if bird.y > HEIGHT:
        print(score)
        sys.exit()
        
    for pipe in pipes:
        if bird.colliderect(pipe):
            print(score)
            sys.exit()

def on_mouse_down():
    bird.y = bird.y - 50

pgzrun.go()
