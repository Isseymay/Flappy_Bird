# Base beginners + Game over extension + Highscore file extension (both parts)

# start modules
import pgzrun
import sys

# create constants
WIDTH = 800
HEIGHT = 600
score = 0
gameOver = False
outText = ""
name = ""
keyUp = True
entered = False

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
topPipe1 = Actor("top")
topPipe1.x = 266
topPipe1.y = -10

bottomPipe1 = Actor("bottom")
bottomPipe1.x = 266
bottomPipe1.y = 800

topPipe2 = Actor("top")
topPipe2.x = 532
topPipe2.y = -200

bottomPipe2 = Actor("bottom")
bottomPipe2.x = 532
bottomPipe2.y = 560

topPipe3 = Actor("top")
topPipe3.x = 798
topPipe3.y = -120

bottomPipe3 = Actor("bottom")
bottomPipe3.x = 798
bottomPipe3.y = 710

# draw everything to screen
def draw():
    if gameOver == True:
        screen.fill((0,0,0))
        get_name()
        screen.draw.text(("Game Over!\n"+outText),center = (400,300), fontsize = 60, width = 600)
    else:
        # draw background
        background.draw()
        # draw all characters
        bird.draw()
        topPipe1.draw()
        bottomPipe1.draw()
        topPipe2.draw()
        bottomPipe2.draw()
        topPipe3.draw()
        bottomPipe3.draw()

# updates everything
def update():
    global score, gameOver
    if gameOver == False:
        # updating bird
        bird.y = bird.y + 1

        # updating pipes 
        topPipe1.x = topPipe1.x - 1
        if topPipe1.x < -44:
            topPipe1.x = WIDTH
            score = score + 1
            
        bottomPipe1.x = bottomPipe1.x - 1
        if bottomPipe1.x < -44:
            bottomPipe1.x = WIDTH
    
        topPipe2.x = topPipe2.x - 1
        if topPipe2.x < -44:
            topPipe2.x = WIDTH
            score = score + 1
            
        bottomPipe2.x = bottomPipe2.x - 1
        if bottomPipe2.x < -44:
            bottomPipe2.x = WIDTH

        topPipe3.x = topPipe3.x - 1
        if topPipe3.x < -44:
            topPipe3.x = WIDTH
            score = score + 1
            
        bottomPipe3.x = bottomPipe3.x - 1
        if bottomPipe3.x < -44:
            bottomPipe3.x = WIDTH

        # bird hits bottom of screen
        if bird.y > HEIGHT:
            print("Game Over!")
            gameOver = True
        
        # bird hits pipes
        if bird.colliderect(topPipe1):
            print("Game Over!")
            gameOver = True
        
        if bird.colliderect(bottomPipe1):
            print("Game Over!")
            gameOver = True
        
        if bird.colliderect(topPipe2):
            print("Game Over!")
            gameOver = True
        
        if bird.colliderect(bottomPipe2):
            print("Game Over!")
            gameOver = True
        
        if bird.colliderect(topPipe3):
            print("Game Over!")
            gameOver = True
        
        if bird.colliderect(bottomPipe3):
            print("Game Over!")
            gameOver = True

# moving
def on_mouse_down():
    bird.y = bird.y - 50

def scoring():
    global score,outText,name
    scores={}
    won = False
    highscore = 0
    with open(".\GPN\Flappy_Bird\Highscore_3.txt","r") as file:
        nextLine = file.readline()
        while nextLine:
            if nextLine != "":
                nextLine = nextLine.strip("\n")
                hsName,hscore = nextLine.split(": ")
                scores[hsName] = hscore
            nextLine = file.readline()
    with open(".\GPN\Flappy_Bird\Highscore_3.txt","w") as f:
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
        outText = f"Your score was {score}\nYour current highscore is: {highscore}"

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
