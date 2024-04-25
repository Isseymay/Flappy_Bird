# only one pipe due to phone screen size

# initialise Pygame Zero
import pgzrun
from random import *

# initialize constants
WIDTH = 360
HEIGHT = 600
minGap = 160
maxGap = 260
scrollSpeed = -1
gameOver = False
score = 0

    
# make bird
bird = Actor("bird")
bird.x = 160
bird.y = 300


# make pipes
# pipe 1
gap1 = randint(minGap,maxGap)
topPipe1 = Actor("top")
topPipe1.x = 280
topPipe1.y = randint(-250,(200-gap1))
bottomPipe1 = Actor("bottom")
bottomPipe1.x = 280
bottomPipe1.y = 600 + gap1 + topPipe1.y
pipes=[topPipe1,bottomPipe1]


# draw everything to screen
def draw():
    if gameOver:
        screen.clear()
        screen.fill((0,0,0))
        screen.draw.text(f"Game Over\nYour score was {score}",center=(WIDTH*0.5,HEIGHT*0.5),align="left",color=(255,255,255), fontsize = 60, width=(WIDTH*0.8))
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
    gap=randint(minGap,maxGap)
    top = True
    for pipe in pipes:
        pipe.x = pipe.x + scrollSpeed
        if pipe.x <= -44:
            pipe.x = WIDTH
            if top==True:
                top=False
                pipe.y = randint(-250,(200-gap))
            else:
                pipe.y = pipes[0].y + 600 + gap
                if not gameOver:
                    score = score + 1
        
    

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
