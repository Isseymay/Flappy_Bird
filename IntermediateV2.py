# pipes determined from three separate lists

# initialise Pygame Zero
import pgzrun
from random import *

# initialize constants
WIDTH = 800
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

topPipes=[]
gaps=[]
bottomPipes=[]
# make pipes
# pipe 1
gap1 = randint(minGap,maxGap)
topPipe1 = Actor("top")
topPipe1.x = 280
topPipe1.y = randint(-250,(200-gap1))
bottomPipe1 = Actor("bottom")
bottomPipe1.x = 280
bottomPipe1.y = 600 + gap1 + topPipe1.y
topPipes.append(topPipe1)
gaps.append(gap1)
bottomPipes.append(bottomPipe1)

gap2 = randint(minGap,maxGap)
topPipe2 = Actor("top")
topPipe2.x = 545
topPipe2.y = randint(-250,(200-gap2))
bottomPipe2 = Actor("bottom")
bottomPipe2.x = 545
bottomPipe2.y = 600 + gap2 + topPipe2.y
topPipes.append(topPipe2)
gaps.append(gap2)
bottomPipes.append(bottomPipe2)

gap3 = randint(minGap,maxGap)
topPipe3 = Actor("top")
topPipe3.x = 810
topPipe3.y = randint(-250,(200-gap3))
bottomPipe3 = Actor("bottom")
bottomPipe3.x = 810
bottomPipe3.y = 600 + gap3 + topPipe3.y
topPipes.append(topPipe3)
gaps.append(gap3)
bottomPipes.append(bottomPipe3)

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

        for pipe in topPipes:
            pipe.draw()

        for pipe in bottomPipes:
            pipe.draw()
        screen.draw.text(f"Score: {score}",topleft=(10,10),color=(0,0,0), fontsize = 30)


# updates everything
def update():
    global score,gameOver
    # updating bird
    bird.y = bird.y + 1

    # updating pipes
    for i in range(len(topPipes)):
        topPipes[i].x = topPipes[i].x + scrollSpeed
        bottomPipes[i].x = bottomPipes[i].x + scrollSpeed
        if topPipes[i].x <= -44:
            topPipes[i].x = WIDTH
            bottomPipes[i].x = WIDTH
            gap = randint(minGap,maxGap)
            gaps[i] = gap
            topPipes[i].y = randint(-250,(200-gap))
            bottomPipes[i].y = 600 + gap3 + topPipes[i].y
    

    # bird hits bottom of screen
    if bird.y > HEIGHT:
        # reset
        gameOver = True

    for pipe in topPipes:
        if bird.colliderect(pipe):
            gameOver = True
    
    for pipe in bottomPipes:
        if bird.colliderect(pipe):
            gameOver = True
    
# moving
def on_mouse_down():
    bird.y = bird.y - 50

# runs everything
pgzrun.go() 
