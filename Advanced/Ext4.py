# Base advanced + Highscore extension (both parts)

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
name = ""
entered = False
keyUp = True


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
        get_name()
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


# moving
def on_mouse_down():
    bird.y = bird.y - 50

def scoring():
    global score,outText,name
    scores={}
    won = False
    highscore = 0
    with open("Highscore.txt","r") as file:
        nextLine = file.readline()
        while nextLine:
            if nextLine != "":
                nextLine = nextLine.strip("\n")
                hsName,hscore = nextLine.split(": ")
                scores[hsName] = hscore
            nextLine = file.readline()
    with open("Highscore3.txt","w") as f:
        if name in scores:
            if score > int(scores[name]):
                won = True
                scores[name]=str(score)
            else:
                highscore = scores[name]
        else:
            won = True
            scores[name] = score
        for person in scores:
            f.write(f"{person}: {scores[person]}\n")        
    f.close()
    if won == True:
        outText = f"Congratulations you beat your high score!\nYour score was: {score}"
    else:
        outText = f"Your score was: {score}\nYour current highscore is: {highscore}"

def get_name():
    global outText,entered
    if entered == False:
        outText = f"What is your name?\n{name}"
    
def on_key_down():
    global keyUp, name, entered
    if gameOver and (entered == False) and keyUp:
        keyUp = False
        if keyboard[keys.RETURN]:
            entered = True
            scoring()
            print(f"Your highscore is saved under {name}")
        else:
            if keyboard[keys.A]:
                name+="a"
            elif keyboard[keys.B]:
                name+="b"
            elif keyboard[keys.C]:
                name+="c"
            elif keyboard[keys.D]:
                name+="d"
            elif keyboard[keys.E]:
                name+="e"
            elif keyboard[keys.F]:
                name+="f"
            elif keyboard[keys.G]:
                name+="g"
            elif keyboard[keys.H]:
                name+="h"
            elif keyboard[keys.I]:
                name+="i"
            elif keyboard[keys.J]:
                name+="j"
            elif keyboard[keys.K]:
                name+="k"
            elif keyboard[keys.L]:
                name+="l"
            elif keyboard[keys.M]:
                name+="m"
            elif keyboard[keys.N]:
                name+="n"
            elif keyboard[keys.O]:
                name+="o"
            elif keyboard[keys.P]:
                name+="p"
            elif keyboard[keys.Q]:
                name+="q"
            elif keyboard[keys.R]:
                name+="r"
            elif keyboard[keys.S]:
                name+="s"
            elif keyboard[keys.T]:
                name+="t"
            elif keyboard[keys.U]:
                name+="u"
            elif keyboard[keys.V]:
                name+="v"
            elif keyboard[keys.W]:
                name+="w"
            elif keyboard[keys.X]:
                name+="x"
            elif keyboard[keys.Y]:
                name+="y"
            elif keyboard[keys.Z]:
                name+="z"
            elif keyboard[keys.SPACE]:
                name+=" "
            elif keyboard[keys.BACKSPACE]:
                if len(name)>=1:
                    name = name[:-1]
            elif keyboard[keys.LSHIFT] or keyboard[keys.RSHIFT]:
                pass
            else:
                print("Only type letters and spaces please")

def on_key_up():
    global keyUp
    if gameOver:
        keyUp = True

# runs everything
pgzrun.go()
