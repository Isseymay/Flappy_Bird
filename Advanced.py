# initialise Pygame Zero
import pgzrun
import sys
from random import *

# initialize constants
WIDTH = 800
HEIGHT = 600
gameOver = False
score = 0

# make bird
bird = Actor("bird")
bird.x = WIDTH*0.15
bird.y = HEIGHT*0.5

# make pipes
class pipes():
    def __init__(self,x):
        gap = randint(160,260)
        genY = randint(50+(gap//2),250-(gap//2))
        self.top = Actor("top")
        self.top.x = x
        self.top.y = genY - (300+(gap//2))
        self.bottom = Actor("bottom")
        self.bottom.x = x
        self.bottom.y = genY + 300+(gap//2)

    def updatePipes(self,bird):
        global gameOver,score
        if bird.colliderect(self.top) or bird.colliderect(self.bottom):
            gameOver = True
        self.top.x = self.top.x-1
        self.bottom.x = self.bottom.x-1
        if self.top.x < (0-(self.top.width//2)):
            self.top.x = WIDTH
            self.bottom.x = WIDTH
            gap = randint(160,260)
            genY = randint(50+(gap//2),250-(gap//2))
            self.top.y = genY - (300+(gap//2))
            self.bottom.y = genY + 300+(gap//2)
            if not gameOver:
                score = score+1

    
    def drawPipes(self):
        self.top.draw()
        self.bottom.draw()

pipes1 = pipes(WIDTH*0.4)
pipes2 = pipes(WIDTH*0.75)
pipes3 = pipes(WIDTH*1.1)
pipeList=[pipes1,pipes2,pipes3]

# draw everything to screen
def draw():
    global entered,gameOver
    
    if gameOver:
        screen.clear()
        screen.fill((0,0,0))
        outdraw = scoring()
        screen.draw.text(f"Game Over\n{outdraw}",center=(WIDTH*0.5,HEIGHT*0.5),align="left",color=(255,255,255), fontsize = 60,width=WIDTH*0.8)
    else:
        # set background image
        screen.blit("bg",(0,0))
        bird.draw()

        for pipes in pipeList:
            pipes.drawPipes()
        screen.draw.text(f"Score: {score}",topleft=(10,10),color=(0,0,0), fontsize = 30)


# updates everything
def update():
    global score,gameOver
    
    bird.y = bird.y - 1

    # updating pipes
    for pipes in pipeList:
        pipes.updatePipes(bird)

    # bird hits bottom of screen
    if bird.y > HEIGHT:
        # reset
        gameOver = True

# moving
def on_mouse_down():
    bird.y = bird.y - 50

# runs everything
pgzrun.go() 
