# Making a simple flappy bird game with Pygame Zero
# flappyBirdV2.1G
# making a pipe class
# timer score instead?
# methods for repeated code
# write to file for highscore (ext?)

# initialise Pygame Zero
import pgzrun
from random import *

# initialize constants
WIDTH = 800
HEIGHT = 600
scrollSpeed = -1
gameOver = False
score = 0
entered = False

class pipeGroup():
    def __init__(self,x):
        self.top = Actor("top")
        self.top.x = x
        self.top.y = randint(int(-(self.top.height*0.3)),int(self.top.height*0.1))
        self.bottom = Actor("bottom")
        self.bottom.x = x
        self.bottom.y = (self.top.height+self.top.y) + randint(minGap,maxGap)

    def updatePipes(self,bird):
        global gameOver,score
        if bird.colliderect(self.top) or bird.colliderect(self.bottom):
            gameOver = True
        self.top.x = self.top.x-2
        self.bottom.x = self.bottom.x-2
        if self.top.x < (0-(self.top.width//2)):
            self.top.x = WIDTH
            self.bottom.x = WIDTH
            self.top.y = randint(int(-(self.top.height*0.3)),int(self.top.height*0.1))
            self.bottom.y = (self.top.height+self.top.y) + randint(minGap,maxGap)
            if not gameOver:
                score = score+1

    
    def drawPipes(self):
        self.top.draw()
        self.bottom.draw()



# make bird
bird = Actor("bird")
bird.x = WIDTH*0.15
bird.y = HEIGHT*0.5
minGap = int((bird.height*1.5)+50)
maxGap = int((bird.height*3.5)+50)

pipes1 = pipeGroup(WIDTH*0.4)
pipes2 = pipeGroup(WIDTH*0.75)
pipes3 = pipeGroup(WIDTH*1.1)
pipeList=[pipes1,pipes2,pipes3]

# draw everything to screen
def draw():
    global entered
    if gameOver:
        screen.clear()
        screen.fill((0,0,0))
        outtext = scoring()
        screen.draw.text(f"Game Over\n{outtext}",center=(WIDTH*0.5,HEIGHT*0.5),align="left",color=(255,255,255), fontsize = 60)
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
    # updating bird
    bird.y = bird.y + 1

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

def scoring():
    global score,entered
    highscore = 0
    for line in open("Highscore.txt","r"):
        line = line.strip()
        if int(line)> highscore:
            highscore = int(line)
    if score > highscore:
        file = open("Highscore.txt","a")
        if not entered:
            file.writelines(str(score)+"\n")
            entered  = True
        file.close()
        return(f"You beat the highscore!\n Your score was: {score}")

    else:
        return(f"Your score was: {score}\n The current highscore is: {highscore}")



# runs everything
pgzrun.go() 
