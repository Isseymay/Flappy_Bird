# pipe groups removed pipe' coordinates generated separately makeing max and min not pass halfway


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
bird.x = 160
bird.y = 300

# make pipes
# pipe 1
topPipe1 = Actor("top")
topPipe1.x = 280
topPipe1.y = randint(-250,-70)

# pipe 2
bottomPipe1 = Actor("bottom")
bottomPipe1.x = 280
bottomPipe1.y = randint(670,850)

# pipe 3
topPipe2 = Actor("top")
topPipe2.x = 545
topPipe2.y = randint(-250,-70)

# pipe 4
bottomPipe2 = Actor("bottom")
bottomPipe2.x = 545
bottomPipe2.y = randint(670,850)

# pipe 5
topPipe3 = Actor("top")
topPipe3.x = 810
topPipe3.y = randint(-250,-70)

# pipe 6
bottomPipe3 = Actor("bottom")
bottomPipe3.x = 810
bottomPipe3.y = randint(670,850)

#vall pipes
pipeList = [topPipe1,bottomPipe1,topPipe2,bottomPipe2,topPipe3,bottomPipe3]

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

        for pipe in pipeList:
            pipe.draw()
        screen.draw.text(f"Score: {score}",topleft=(10,10),color=(0,0,0), fontsize = 30)


# updates everything
def update():
    global score,gameOver
    # updating bird
    bird.y = bird.y + 1

    # updating pipes
    top = True
    for pipe in pipeList:
        pipe.x = pipe.x + scrollSpeed
        if pipe.x < -44:
            pipe.x = WIDTH
            if top == True:
                pipe.y = randint(-250,-70)
                top=False  
            else:
                pipe.y = randint(670,850)
                top = True
                if not gameOver:
                    score = score + 1
    

    # bird hits bottom of screen
    if bird.y > HEIGHT:
        # reset
        gameOver = True

    for pipe in pipeList:
        if bird.colliderect(pipe):
            gameOver = True
    
# moving
def on_mouse_down():
    bird.y = bird.y - 50

# runs everything
pgzrun.go() 
