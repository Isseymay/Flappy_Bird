# Full game + tweaking because I wanted it to be fun

# start modules
import pgzrun
from random import *
import math

# screen
WIDTH = 800
HEIGHT = 600
xGap = 266+(2/3) # calculation done to make 4 pipes eqidistant

# proj motion
y0 = 300
g = 9.81
t = 0

# wait to play
start = False

# play again
button = Actor("play_again")
button.x = 400
button.y = 475

# highscore
outText = ""
name = ""
keyUp = True
entered = False

# gameplay
score = 0
gameOver = False

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
print(bird.height)

# pipes class
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

    def updatePipes(self, bird): # update pipes each frame
        global score, gameOver
        self.top.x = self.top.x - 1
        self.bottom.x = self.bottom.x - 1
        if self.top.x < -43.5:
            self.top.x = xGap + (WIDTH-43.5) # calculation done to find where an equidistant pipe would be right as it wraps around
            self.bottom.x = xGap + (WIDTH-43.5)
            gap = randint(160,260) # generates the gap between the two pipes between 2 "flaps" + bird's height and 4 "flaps" + bird's height
            y = randint((300-250+(gap//2)),(850-300-(gap//2))) # generates a point for the middle of the gap ensurinf the top pipe's y is never less than -250 and the bottom pipe's y is never more than 850 so they look significantly on screen at all times
            self.top.y = y - (300 + (gap//2)) # finds the top pipe's y value with a calculations based of the middle of the gap and the gaps height and the distance from the gap to the center of the pipe (half it's height)
            self.bottom.y = y + 300 + (gap//2) # same as above
            score = score + 1

        if bird.colliderect(self.top) or bird.colliderect(self.bottom):
            print("Game Over!")
            print(f"Your score was {score}")
            gameOver = True

    def drawPipes(self):
        self.top.draw()
        self.bottom.draw()

# make pipes
pipes1 = Pipes(2*xGap) # start's at 2 x gap to ensure there's time between starting and needing to "flap"
pipes2 = Pipes(3*xGap)
pipes3 = Pipes(4*xGap)
pipes4 = Pipes(5*xGap)
pipes = [pipes1,pipes2,pipes3,pipes4]

# draw everything frame
def draw():
    if start == False:
        background.draw()
        bird.draw()
        screen.draw.text("Click the screen to play!", center = (470,300), color = (255,255,255), fontsize = 60, width = 310)
    else:
        if gameOver == True:
            screen.fill((0,0,0))
            get_name()
            screen.draw.text(f"Game Over!\n{outText}", center = (400,200), fontsize = 60, width = 600)
            button.draw()
        else:
            # draw background
            background.draw() # background is an actor as it's easier for beginners of pygame zero to understand instead of "blit"

            # draw characters
            bird.draw()
            for pipe in pipes:
                pipe.drawPipes()
            screen.draw.text(f"Score: {score}", topleft = (20,20), color = (0,0,0), fontsize = 30)

# update every frame
def update():
    global score, gameOver, t
    if start == False:
        t = t + ((15*math.pi)/60) # what to step by ( 1 frame is one pi/4 th of a second)
        # loop time
        bird.y = 300 + (math.cos(t/15.0)* 50.0) # bird's y plots a cos line for a smooth "flying" movement
    else:
        if gameOver == False:
            t = t + 0.1 # 1 frame is 1/10 th of a "second"
            # update bird
            bird.y = y0 + (0.5 * g * (t**2)) # uses projectile motion formula but as the bird is falling, it's initial angle is 0 cancelling a section out

            # update pipes
            for pipe in pipes:
                pipe.updatePipes(bird)
            # bird hits bottom of screen
            if bird.y > (HEIGHT+30): # bird is full off screen
                print("Game Over!")
                print(f"Your score was: {score}")
                gameOver = True
            
# mouse clicks
def on_mouse_down(pos):
    global start,t,y0
    if start == False:
        start = True
        bird.y = 300
        t = 0
    else:
        if gameOver:
            if button.collidepoint(pos):
                print("Restarting...")
                restart()
        else:
            bird.y = bird.y - 50 
            t = 0 # needs to restart as the bird is now re-falling
            y0 = bird.y 

# restart values
def restart(): # self explanatory
    global score, gameOver, y0,t, outText, name, keyUp, entered, pipes
    score = 0
    gameOver = False
    outText = ""
    name = ""
    keyUp = True
    entered = False

    bird.y = 300
    y0 = 300
    t = 0

    pipes1 = Pipes(2*xGap)
    pipes2 = Pipes(3*xGap)
    pipes3 = Pipes(4*xGap)
    pipes4 = Pipes(5*xGap)
    pipes = [pipes1,pipes2,pipes3,pipes4]

# saving a personal highscore to a file
def scoring():
    global score,outText,name
    scores={}
    won = False
    highscore = 0
    with open(".\GPN\Flappy_Bird\Highscore.txt","r") as file:
        nextLine = file.readline()
        while nextLine:
            if nextLine != "":
                nextLine = nextLine.strip("\n")
                hsName,hscore = nextLine.split(": ") # store's the name and score in a dictionary as searching a dictionary is faster/easier than a list of names etc
                scores[hsName] = hscore
            nextLine = file.readline()

    if name in scores:
        if score > int(scores[name]):
            won = True
            scores[name]=str(score) # changes score value to easily add correct info back into file
        else:
            highscore = scores[name]
    else:
        won = True
        scores[name] = score

    with open(".\GPN\Flappy_Bird\Highscore.txt","w") as f:
        for person in scores:
            f.write(f"{person}: {scores[person]}\n")        
    f.close()
    if won == True:
        outText = f"Congratulations you beat your high score!\nYour score was: {score}"
    else:
        outText = f"Your score was: {score}\nYour current highscore is: {highscore}"

# re-sends the value of name so it updates on screen when the user types a new letter (re-sends every frame_)
def get_name():
    global outText
    if entered == False:
        outText = f"What is your name?\n{name}"

# key logger part 1 (so no held keys are tracked)    
def on_key_down():
    global keyUp, name, entered
    if gameOver and (entered == False) and keyUp:
        keyUp = False # once a key is pressed it must be un-pressed to be counted again
        if keyboard[keys.RETURN]:
            entered = True
            scoring() # this means that scoring is only run once
            print(f"Your highscore is saved under {name}")
        else:
            if keyboard[keys.A] and (keyboard[keys.LSHIFT] or keyboard[keys.RSHIFT]): # this way is a bit janky but pygame zero doesn't allow for just reading a capital without the use of shift due to some keboard's maufacturing
                name+="A"
            elif keyboard[keys.B] and (keyboard[keys.LSHIFT] or keyboard[keys.RSHIFT]):
                name+="B"
            elif keyboard[keys.C] and (keyboard[keys.LSHIFT] or keyboard[keys.RSHIFT]):
                name+="C"
            elif keyboard[keys.D] and (keyboard[keys.LSHIFT] or keyboard[keys.RSHIFT]):
                name+="D"
            elif keyboard[keys.E] and (keyboard[keys.LSHIFT] or keyboard[keys.RSHIFT]):
                name+="E"
            elif keyboard[keys.F] and (keyboard[keys.LSHIFT] or keyboard[keys.RSHIFT]):
                name+="F"
            elif keyboard[keys.G] and (keyboard[keys.LSHIFT] or keyboard[keys.RSHIFT]):
                name+="G"
            elif keyboard[keys.H] and (keyboard[keys.LSHIFT] or keyboard[keys.RSHIFT]):
                name+="H"
            elif keyboard[keys.I] and (keyboard[keys.LSHIFT] or keyboard[keys.RSHIFT]):
                name+="I"
            elif keyboard[keys.J] and (keyboard[keys.LSHIFT] or keyboard[keys.RSHIFT]):
                name+="J"
            elif keyboard[keys.K] and (keyboard[keys.LSHIFT] or keyboard[keys.RSHIFT]):
                name+="K"
            elif keyboard[keys.L] and (keyboard[keys.LSHIFT] or keyboard[keys.RSHIFT]):
                name+="L"
            elif keyboard[keys.M] and (keyboard[keys.LSHIFT] or keyboard[keys.RSHIFT]):
                name+="M"
            elif keyboard[keys.N] and (keyboard[keys.LSHIFT] or keyboard[keys.RSHIFT]):
                name+="N"
            elif keyboard[keys.O] and (keyboard[keys.LSHIFT] or keyboard[keys.RSHIFT]):
                name+="O"
            elif keyboard[keys.P] and (keyboard[keys.LSHIFT] or keyboard[keys.RSHIFT]):
                name+="P"
            elif keyboard[keys.Q] and (keyboard[keys.LSHIFT] or keyboard[keys.RSHIFT]):
                name+="Q"
            elif keyboard[keys.R] and (keyboard[keys.LSHIFT] or keyboard[keys.RSHIFT]):
                name+="R"
            elif keyboard[keys.S] and (keyboard[keys.LSHIFT] or keyboard[keys.RSHIFT]):
                name+="S"
            elif keyboard[keys.T] and (keyboard[keys.LSHIFT] or keyboard[keys.RSHIFT]):
                name+="T"
            elif keyboard[keys.U] and (keyboard[keys.LSHIFT] or keyboard[keys.RSHIFT]):
                name+="U"
            elif keyboard[keys.V] and (keyboard[keys.LSHIFT] or keyboard[keys.RSHIFT]):
                name+="V"
            elif keyboard[keys.W] and (keyboard[keys.LSHIFT] or keyboard[keys.RSHIFT]):
                name+="W"
            elif keyboard[keys.X] and (keyboard[keys.LSHIFT] or keyboard[keys.RSHIFT]):
                name+="X"
            elif keyboard[keys.Y] and (keyboard[keys.LSHIFT] or keyboard[keys.RSHIFT]):
                name+="Y"
            elif keyboard[keys.Z] and (keyboard[keys.LSHIFT] or keyboard[keys.RSHIFT]):
                name+="Z"
            elif keyboard[keys.A]:
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

# key logger part 2
def on_key_up():
    global keyUp
    if gameOver:
        keyUp = True

# runs everything
pgzrun.go()
