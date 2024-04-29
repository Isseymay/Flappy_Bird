# Base advanced + Highscore extension (first part)

# start modules
import pgzrun
import sys
from random import *


# create constants
WIDTH = 800
HEIGHT = 600
score = 0
gameOver = False
outText = ""


# print welcome
print('''The game is about to start!
Click the mouse to "flap" upwards
Dodge the pipes and the floor
Good luck and have fun!''')


# make background
background = Actor("bg")
background.x = 400
background.y = 300


# make bird
bird = Actor("bird")
bird.x = 160
bird.y = 300


# make pipes
class Pipes():
    def __init__(self, x):
        gap = randint(160,260)
        y = randint((300-250+(gap//2)),(850-300-(gap//2)))

        self.top = Actor("top")
        self.top.x = x
        self.top.y = y - (300 + (gap // 2))
        self.bottom = Actor("bottom")
        self.bottom.x = x
        self.bottom.y = y + 300 + (gap // 2)

    def updatePipes(self, bird):
        global score, gameOver
        self.top.x = self.top.x - 1
        self.bottom.x = self.bottom.x - 1
        if self.top.x < -44:
            self.top.x = 844
            self.bottom.x = 844
            gap = randint(160,260)
            y = randint((300-250+(gap//2)),(850-300-(gap//2)))
            self.top.y = y - (300 + (gap//2))
            self.bottom.y = y + 300 + (gap//2)
            score = score + 1

        if bird.colliderect(self.top) or bird.colliderect(self.bottom):
            print("Game Over!")
            print(f"Your score was {score}")
            gameOver = True
            scoring()
            


    def drawPipes(self):
        self.top.draw()
        self.bottom.draw()



pipes1 = Pipes(266)
pipes2 = Pipes(532)
pipes3 = Pipes(798)
pipes = [pipes1,pipes2,pipes3]

# draw everything to screen
def draw():
    if gameOver == True:
        screen.fill((0,0,0))
        screen.draw.text(f"Game Over!\n {outText}", center = (400,300), fontsize = 60)
    else:
        # draw background
        background.draw()


        # draw characters
        bird.draw()
        for pipe in pipes:
            pipe.drawPipes()


# update everything
def update():
    global score, gameOver
    if gameOver == False:
        # update bird
        bird.y = bird.y + 1


        # update pipes
        for pipe in pipes:
            pipe.updatePipes(bird)
        # bird hits bottom of screen
        if bird.y > HEIGHT:
            print("Game Over!")
            print(f"Your score was: {score}")
            gameOver = True
            scoring()


# moving
def on_mouse_down():
    bird.y = bird.y - 50

def scoring():
    global score,outText,name
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


# runs everything
pgzrun.go()
