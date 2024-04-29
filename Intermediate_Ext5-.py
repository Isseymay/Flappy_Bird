# Base intermediate + Highscore extension (first part)

# start modules
import pgzrun
import sys
from random import *

# create constants
WIDTH = 800
HEIGHT = 600
gap = 210
score = 0
gameOver = False
outText = ""

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

genY1 = randint(155,445)
topPipe1 = Actor("top")
topPipe1.x = 266
topPipe1.y = genY1 - (300+(gap//2))
pipes.append(topPipe1)
bottomPipe1 = Actor("bottom")
bottomPipe1.x = 266
bottomPipe1.y = genY1 + 300 + (gap//2)
pipes.append(bottomPipe1)

genY2 = randint(155,445)
topPipe2 = Actor("top")
topPipe2.x = 532
topPipe2.y = genY2 - (300+(gap//2))
pipes.append(topPipe2)
bottomPipe2 = Actor("bottom")
bottomPipe2.x = 532
bottomPipe2.y = genY2 + 300 + (gap//2)
pipes.append(bottomPipe2)

genY3 = randint(155,445)
topPipe3 = Actor("top")
topPipe3.x = 798
topPipe3.y = genY3 - (300+(gap//2))
pipes.append(topPipe3)
bottomPipe3 = Actor("bottom")
bottomPipe3.x = 798
bottomPipe3.y = genY3 + 300 + (gap//2)
pipes.append(bottomPipe3)

# draw everything to screen
def draw():
    global score, gameOver
    if gameOver:
        screen.fill((0,0,0))
        screen.draw.text(f"Game Over\n{outText}",center=(400,300),align="left",color=(255,255,255), fontsize = 60, width = 600)
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
    if gameOver == False:
        # update bird
        bird.y = bird.y + 1

        # update pipes
        genY = randint(155,445)
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
            scoring()
            
        # bird hits pipes
        for pipe in pipes:
            if bird.colliderect(pipe):
                gameOver=True
                scoring()

# moving
def on_mouse_down():
    bird.y = bird.y - 50
    
def scoring():
    global score,outText
    highscore = 0
    with open("Highscore.txt","r") as f:
        line = f.readline()
        if line != "":
            line = line.strip("\n")
            highscore = int(line)
    with open("Highscore.txt","w") as file:
        if score > highscore:
            outText = f"Congratulations you beat the high score!\nYour score was: {score}"  
            file.write(f"{score}\n")
        else:
            outText = f"Your score was {score}\nThe current highscore is: {highscore}"
            file.write(f"{highscore}\n")
    file.close()

# makes everything run
pgzrun.go()
