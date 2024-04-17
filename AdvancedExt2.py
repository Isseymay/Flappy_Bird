#File and name extension
# Making a simple flappy bird game with Pygame Zero
# flappyBirdV2.1G
# making a pipe class
# timer score instead
# methods for repeated code
# write to file for highscore 
# projictile falling

# initialise Pygame Zero
import pgzrun
from random import *
import math 

# initialize constants
WIDTH = 800
HEIGHT = 600
scrollSpeed = -1
gameOver = False
score = 0
entered = False
won = False
highscore = 0

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
originaly = bird.y
t=0
v0 = 80
minGap = int((bird.height*2.5)+50)
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
    global score,gameOver,t,originaly,v0
    t+=0.1
    velocity = v0 * math.sin(math.radians(0))
    # updating bird
    bird.y = originaly - (velocity*t - (0.5*9.81*(t**2)))

    # updating pipes
    for pipes in pipeList:
        pipes.updatePipes(bird)

    # bird hits bottom of screen
    if bird.y > HEIGHT:
        # reset
        gameOver = True

# moving
def on_mouse_down():
    global t,originaly
    bird.y = bird.y - 50
    originaly = bird.y
    t = 0

def scoring():
    global score,entered,won,highscore
    if not entered:
        with open(".\GPN\Flappy_Bird\Highscore.txt","r") as file:
            temp=file.readline()
            temp=temp.strip("\n")
            print(temp)
            if temp!="":
                highscore = int(temp)
        with open(".\GPN\Flappy_Bird\Highscore.txt","w") as f:
            if score>highscore:
                won = True
                f.write(str(score))
            else:
                f.write(str(highscore))
            entered = True
        f.close()
    if entered and won:
        return(f"You beat the highscore!\n Your score was: {score}")
    else:
        return(f"Your score was: {score}\n The current highscore is: {highscore}")
    



# runs everything
pgzrun.go() 