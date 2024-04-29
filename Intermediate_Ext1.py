# Base intermediate + Random gaps extension

# start modules
import pgzrun
import sys
from random import *

# create constants
WIDTH = 800
HEIGHT = 600
score = 0
gameOver = False

# print welcome
print("The game is about to start!")
print('Click the mouse to "flap" upwards')
print("Dodge the pipes and the floor")
print("Good luck and have fun!")

# make background
background = Actor("bg")
background.x = 400
background.y = 300

# make bird
bird = Actor("bird")
bird.x = 160
bird.y = 300

# make pipes
pipes=[]

gap1 = randint(160,260)
y1 = randint((300+(gap1//2)-250),(850-(gap1//2)-300))
topPipe1 = Actor("top")
topPipe1.x = 266
topPipe1.y = y1 - (300+(gap1//2))
pipes.append(topPipe1)
bottomPipe1 = Actor("bottom")
bottomPipe1.x = 266
bottomPipe1.y = y1 + 300 + (gap1//2)
pipes.append(bottomPipe1)

gap2 = randint(160,260)
y2 = randint((300+(gap2//2)-250),(850-(gap2//2)-300))
topPipe2 = Actor("top")
topPipe2.x = 545
topPipe2.y = y2 - (300+(gap2//2))
pipes.append(topPipe2)
bottomPipe2 = Actor("bottom")
bottomPipe2.x = 545
bottomPipe2.y = y2 + 300 + (gap2//2)
pipes.append(bottomPipe2)

gap3 = randint(160,260)
y3 = randint((300+(gap3//2)-250),(850-(gap3//2)-300))
topPipe3 = Actor("top")
topPipe3.x = 810
topPipe3.y = y3 - (300+(gap3//2))
pipes.append(topPipe3)
bottomPipe3 = Actor("bottom")
bottomPipe3.x = 810
bottomPipe3.y = y3 + 300 + (gap3//2)
pipes.append(bottomPipe3)

# draw everything to screen
def draw():
    global score, gameOver
    if gameOver:
        screen.fill((0,0,0))
        screen.draw.text(f"Game Over\nYour score was {score}",center=(400,300),align="left",color=(255,255,255), fontsize = 60)
    else:
        # draw background
        background.draw()
        
        # draw actors
        bird.draw()

        for pipe in pipes:
            pipe.draw()
       
# update everything
def update():
    global score, gameOver
    # update bird
    bird.y = bird.y + 1

    # update pipes
    gap = randint(160,260)
    genY = randint((300+(gap//2)-250),(850-(gap//2)-300))
    for pipe in pipes:
        pipe.x = pipe.x - 1
        if pipe.x < -44:
            pipe.x = WIDTH
            if pipe.image == "top":
                score = score + 1
                pipe.y = genY - (300 + (gap//2))
            else:
                pipe.y = genY + 300 + (gap//2)
        

    # bird hits bottom of screen
    if bird.y > HEIGHT:
        gameOver=True
        
    # bird hits pipes
    for pipe in pipes:
        if bird.colliderect(pipe):
            gameOver=True

# moving
def on_mouse_down():
    bird.y = bird.y - 50
    
# makes everything run
pgzrun.go()
