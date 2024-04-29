# Base beginners + Game over extension + Highscore file extension (first part)

# start modules
import pgzrun
import sys

# create constants
WIDTH = 800
HEIGHT = 600
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
            scoring()
        
        # bird hits pipes
        if bird.colliderect(topPipe1):
            print("Game Over!")
            gameOver = True
            scoring()
        
        if bird.colliderect(bottomPipe1):
            print("Game Over!")
            gameOver = True
            scoring()
        
        if bird.colliderect(topPipe2):
            print("Game Over!")
            gameOver = True
            scoring()
        
        if bird.colliderect(bottomPipe2):
            print("Game Over!")
            gameOver = True
            scoring()
        
        if bird.colliderect(topPipe3):
            print("Game Over!")
            gameOver = True
            scoring()
        
        if bird.colliderect(bottomPipe3):
            print("Game Over!")
            gameOver = True
            scoring()

# moving
def on_mouse_down():
    bird.y = bird.y - 50

def scoring():
    global score, outText
    highscore = 0
    with open(".\GPN\Flappy_Bird\Highscore.txt","r") as f:
        line = f.readline()
        line = line.strip("\n")
        if line !="":
            highscore = int(line)
    with open(".\GPN\Flappy_Bird\Highscore.txt","w") as file:
        if score > highscore:
            outText = f"Congratulations you beat the high score!\nYour score was: {score}"
            file.write(f"{score}\n")
        else:
            outText = f"Your score was {score}\nThe current highscore is: {highscore}"
            file.write(f"{highscore}\n")
    file.close()

# runs everything
pgzrun.go() 
