# Making a simple flappy bird game with Pygame Zero
# flappyBirdV2.1G
# took away scoring, and game over. code quits. Took away pipe groups

# initialise Pygame Zero
import pgzrun
import sys

# initialize constants
WIDTH = 800
HEIGHT = 600
gap = 200
scrollSpeed = -1


    
# make bird
bird = Actor("bird")
bird.x = 160
bird.y = 300

# make pipes
topPipe1 = Actor("top")
topPipe1.x = 280
topPipe1.y = 0

bottomPipe1 = Actor("bottom")
bottomPipe1.x = 280
bottomPipe1.y = 800


topPipe2 = Actor("top")
topPipe2.x = 545
topPipe2.y = -200

bottomPipe2 = Actor("bottom")
bottomPipe2.x = 545
bottomPipe2.y = 560


topPipe3 = Actor("top")
topPipe3.x = 810
topPipe3.y = -120

bottomPipe3 = Actor("bottom")
bottomPipe3.x = 810
bottomPipe3.y = 710

# draw everything to screen
def draw():
    # set background image
    screen.blit("bg",(0,0))
    bird.draw()
    topPipe1.draw()
    bottomPipe1.draw()
    topPipe2.draw()
    bottomPipe2.draw()
    topPipe3.draw()
    bottomPipe3.draw()

# updates everything
def update():
    # updating bird
    bird.y = bird.y + 1

    # updating 1st pipe 
    topPipe1.x = topPipe1.x + scrollSpeed
    if topPipe1.x < -87:
        topPipe1.x = WIDTH
        
    # updating 2nd pipe 
    bottomPipe1.x = bottomPipe1.x + scrollSpeed
    if bottomPipe1.x < -87:
        bottomPipe1.x = WIDTH

    # updating 3rd pipe 
    topPipe2.x = topPipe2.x + scrollSpeed
    if topPipe2.x < -87:
        topPipe2.x = WIDTH
        
    # updating 4th pipe 
    bottomPipe2.x = bottomPipe2.x + scrollSpeed
    if bottomPipe2.x < -87:
        bottomPipe2.x = WIDTH

    # updating 5th pipe 
    topPipe3.x = topPipe3.x + scrollSpeed
    if topPipe3.x < -87:
        topPipe3.x = WIDTH
        
    # updating 6th pipe 
    bottomPipe3.x = bottomPipe3.x + scrollSpeed
    if bottomPipe3.x < -87:
        bottomPipe3.x = WIDTH

    # bird hits bottom of screen
    if bird.y > HEIGHT:
        # reset
        print("Reset!")
        reset()
    elif bird.colliderect(topPipe1):
        # reset
        print("Reset!")
        reset()
    elif bird.colliderect(bottomPipe1):
        # reset
        print("Reset!")
        reset()
    elif bird.colliderect(topPipe2):
        # reset
        print("Reset!")
        reset()
    elif bird.colliderect(bottomPipe2):
        # reset
        print("Reset!")
        reset()
    elif bird.colliderect(topPipe3):
        # reset
        print("Reset!")
        reset()
    elif bird.colliderect(bottomPipe3):
        # reset
        print("Reset!")
        reset()

# moving
def on_mouse_down():
    bird.y = bird.y - 50

def reset():
    # reset
    bird.x = 160
    bird.y = 300
    topPipe1.x = 280
    bottomPipe1.x = 280
    topPipe2.x = 545
    bottomPipe2.x = 545
    topPipe3.x = 810
    bottomPipe3.x = 810

# runs everything
pgzrun.go() 
