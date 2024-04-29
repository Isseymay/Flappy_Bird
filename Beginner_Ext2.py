# Base beginners + Game over extension + Extra pipes extension

# start modules
import pgzrun
import sys

# create constants
WIDTH = 800
HEIGHT = 600
score = 0
gameOver = False

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

topPipe4 = Actor("top")
topPipe4.x = 1064
topPipe4.y = -70

bottomPipe4 = Actor("bottom")
bottomPipe4.x = 1064
bottomPipe4.y = 790

topPipe5 = Actor("top")
topPipe5.x = 1330
topPipe5.y = -190

bottomPipe5 = Actor("bottom")
bottomPipe5.x = 1330
bottomPipe5.y = 610

topPipe6 = Actor("top")
topPipe6.x = 1596
topPipe6.y = -50

bottomPipe6 = Actor("bottom")
bottomPipe6.x = 1596
bottomPipe6.y = 750


# draw everything to screen
def draw():
    if gameOver == True:
        screen.fill((0,0,0))
        screen.draw.text(("Game Over!\nYour score was: "+str(score)), center = (400,300), color = (255,255,255), fontsize = 60, align = "left")
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
        topPipe4.draw()
        bottomPipe4.draw()
        topPipe5.draw()
        bottomPipe5.draw()
        topPipe6.draw()
        bottomPipe6.draw()

# updates everything
def update():
    global score, gameOver
    if gameOver == False:
        # updating bird
        bird.y = bird.y + 1

        # updating pipes 
        topPipe1.x = topPipe1.x - 1
        if topPipe1.x < -44:
            topPipe1.x = 1552
            score = score + 1

        bottomPipe1.x = bottomPipe1.x - 1
        if bottomPipe1.x < -44:
            bottomPipe1.x = 1552
    
        topPipe2.x = topPipe2.x - 1
        if topPipe2.x < -44:
            topPipe2.x = 1552
            score = score + 1

        bottomPipe2.x = bottomPipe2.x - 1
        if bottomPipe2.x < -44:
            bottomPipe2.x = 1552

        topPipe3.x = topPipe3.x - 1
        if topPipe3.x < -44:
            topPipe3.x = 1552
            score = score + 1

        bottomPipe3.x = bottomPipe3.x - 1
        if bottomPipe3.x < -44:
            bottomPipe3.x = 1552

        topPipe4.x = topPipe4.x - 1
        if topPipe4.x < -44:
            topPipe4.x = 1552
            score = score + 1

        bottomPipe4.x = bottomPipe4.x - 1
        if bottomPipe4.x < -44:
            bottomPipe4.x = 1552
    
        topPipe5.x = topPipe5.x - 1
        if topPipe5.x < -44:
            topPipe5.x = 1552
            score = score + 1

        bottomPipe5.x = bottomPipe5.x - 1
        if bottomPipe5.x < -44:
            bottomPipe5.x = 1552

        topPipe6.x = topPipe6.x - 1
        if topPipe6.x < -44:
            topPipe6.x = 1552
            score = score + 1

        bottomPipe6.x = bottomPipe6.x - 1
        if bottomPipe6.x < -44:
            bottomPipe6.x = 1552

        # bird hits bottom of screen
        if bird.y > HEIGHT:
            gameOver = True

        # bird hits bottom of screen
        if bird.y > HEIGHT:
            print("Game Over!")
            print("Your score was:", score)
            gameOver = True

        # bird hits pipes
        if bird.colliderect(topPipe1):
            print("Game Over!")
            print("Your score was:", score)
            gameOver = True
    
        if bird.colliderect(bottomPipe1):
            print("Game Over!")
            print("Your score was:", score)
            gameOver = True

        if bird.colliderect(topPipe2):
            print("Game Over!")
            print("Your score was:", score)
            gameOver = True
    
        if bird.colliderect(bottomPipe2):
            print("Game Over!")
            print("Your score was:", score)
            gameOver = True
    
        if bird.colliderect(topPipe3):
            print("Game Over!")
            print("Your score was:", score)
            gameOver = True
    
        if bird.colliderect(bottomPipe3):
            print("Game Over!")
            print("Your score was:", score)
            gameOver = True

        if bird.colliderect(topPipe4):
            print("Game Over!")
            print("Your score was:", score)
            gameOver = True
    
        if bird.colliderect(bottomPipe4):
            print("Game Over!")
            print("Your score was:", score)
            gameOver = True

        if bird.colliderect(topPipe5):
            print("Game Over!")
            print("Your score was:", score)
            gameOver = True
    
        if bird.colliderect(bottomPipe5):
            print("Game Over!")
            print("Your score was:", score)
            gameOver = True
    
        if bird.colliderect(topPipe6):
            print("Game Over!")
            print("Your score was:", score)
            gameOver = True
    
        if bird.colliderect(bottomPipe6):
            print("Game Over!")
            print("Your score was:", score)
            gameOver = True


# moving
def on_mouse_down():
    bird.y = bird.y - 50

# runs everything
pgzrun.go() 
