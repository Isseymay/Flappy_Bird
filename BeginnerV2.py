# phone sized 

# initialise Pygame Zero
import pgzrun
import sys

# initialize constants
WIDTH = 380
HEIGHT = 600
scrollSpeed = -1
gameOver = False
score = 0

    
# make bird
bird = Actor("bird")
bird.x = 120
bird.y = 300


# make pipes
# pipe 1
topPipe1 = Actor("top")
topPipe1.x = 240
topPipe1.y = 0
bottomPipe1 = Actor("bottom")
bottomPipe1.x = 240
bottomPipe1.y = 800



# draw everything to screen
def draw():
    screen.blit("bg",(0,0))
    bird.draw()

    topPipe1.draw()
    bottomPipe1.draw()

    
    screen.draw.text(f"Score: {score}",topleft=(10,10),color=(0,0,0), fontsize = 30)


# updates everything
def update():
    global score
    # updating bird
    bird.y = bird.y + 1

    # updating pipes
    topPipe1.x = topPipe1.x + scrollSpeed
    bottomPipe1.x = bottomPipe1.x + scrollSpeed
    if topPipe1.x <= -44:
        topPipe1.x = WIDTH
        bottomPipe1.x = WIDTH
    
        
    

    # bird hits bottom of screen
    if bird.y > HEIGHT:
        # reset
        print("Game Over!")
        sys.exit()

    if bird.colliderect(topPipe1):
        print("Game Over!")
        sys.exit()

    if bird.colliderect(bottomPipe1):
        print("Game Over!")
        sys.exit()
    
# moving
def on_mouse_down():
    bird.y = bird.y - 50

# runs everything
pgzrun.go() 
