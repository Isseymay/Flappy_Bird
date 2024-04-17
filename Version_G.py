# Making a simple flappy bird game with Pygame Zero
# flappyBirdV2.1G
# took away scoring, and game over. Positions just reset

# initialise Pygame Zero
import pgzrun

# initialize constants
WIDTH = 800
HEIGHT = 600
gap = 200
scrollSpeed = -1


    
# make bird
bird = Actor("bird")
bird.x = WIDTH*0.18
bird.y = HEIGHT*0.5

# make pipes
# pipe group 1
topPipe1 = Actor("top")
topPipe1.x = WIDTH*0.33
topPipe1.y = 0
bottomPipe1 = Actor("bottom")
bottomPipe1.x = WIDTH*0.33
bottomPipe1.y = topPipe1.height + gap

# pipe group 2
topPipe2 = Actor("top")
topPipe2.x = WIDTH*0.66
topPipe2.y = -(topPipe2.height*0.2)
bottomPipe2 = Actor("bottom")
bottomPipe2.x = WIDTH*0.66
bottomPipe2.y = (topPipe2.height + topPipe2.y) + gap


# pipe group 3
topPipe3 = Actor("top")
topPipe3.x = WIDTH
topPipe3.y = -(topPipe3.height*0.4)
bottomPipe3 = Actor("bottom")
bottomPipe3.x = WIDTH
bottomPipe3.y = (topPipe3.height + topPipe3.y) + gap

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

    # updating 1st pipe group
    topPipe1.x = topPipe1.x + scrollSpeed
    bottomPipe1.x = bottomPipe1.x + scrollSpeed
    if topPipe1.x < (0-topPipe1.width):
        topPipe1.x = WIDTH
        bottomPipe1.x = WIDTH

    # updating 2nd pipe group
    topPipe2.x = topPipe2.x + scrollSpeed
    bottomPipe2.x = bottomPipe2.x + scrollSpeed
    if topPipe2.x < (0-topPipe2.width):
        topPipe2.x = WIDTH
        bottomPipe2.x = WIDTH

    # updating 3rd pipe group
    topPipe3.x = topPipe3.x + scrollSpeed
    bottomPipe3.x = bottomPipe3.x + scrollSpeed
    if topPipe3.x < (0-topPipe3.width):
        topPipe3.x = WIDTH
        bottomPipe3.x = WIDTH

    # bird hits bottom of screen
    if bird.y > HEIGHT:
        # reset
        print("Game Restarting")
        bird.x = WIDTH*0.18
        bird.y = HEIGHT*0.5
        topPipe1.x = WIDTH*0.33
        topPipe1.y = 0
        bottomPipe1.x = WIDTH*0.33
        bottomPipe1.y = topPipe1.height + gap
        topPipe2.x = WIDTH*0.66
        topPipe2.y = -(topPipe2.height*0.2)
        bottomPipe2.x = WIDTH*0.66
        bottomPipe2.y = (topPipe2.height + topPipe2.y) + gap
        topPipe3.x = WIDTH
        topPipe3.y = -(topPipe3.height*0.4)
        bottomPipe3.x = WIDTH
        bottomPipe3.y = (topPipe3.height + topPipe3.y) + gap

    # bird hits 1st pipe group
    if bird.colliderect(topPipe1) or bird.colliderect(bottomPipe1):
        print("Game Restarting")
        bird.x = WIDTH*0.18
        bird.y = HEIGHT*0.5
        topPipe1.x = WIDTH*0.33
        topPipe1.y = 0
        bottomPipe1.x = WIDTH*0.33
        bottomPipe1.y = topPipe1.height + gap
        topPipe2.x = WIDTH*0.66
        topPipe2.y = -(topPipe2.height*0.2)
        bottomPipe2.x = WIDTH*0.66
        bottomPipe2.y = (topPipe2.height + topPipe2.y) + gap
        topPipe3.x = WIDTH
        topPipe3.y = -(topPipe3.height*0.4)
        bottomPipe3.x = WIDTH
        bottomPipe3.y = (topPipe3.height + topPipe3.y) + gap

    # bird hits 2nd pipe group
    if bird.colliderect(topPipe2) or bird.colliderect(bottomPipe2):
        print("Game Restarting")
        bird.x = WIDTH*0.18
        bird.y = HEIGHT*0.5
        topPipe1.x = WIDTH*0.33
        topPipe1.y = 0
        bottomPipe1.x = WIDTH*0.33
        bottomPipe1.y = topPipe1.height + gap
        topPipe2.x = WIDTH*0.66
        topPipe2.y = -(topPipe2.height*0.2)
        bottomPipe2.x = WIDTH*0.66
        bottomPipe2.y = (topPipe2.height + topPipe2.y) + gap
        topPipe3.x = WIDTH
        topPipe3.y = -(topPipe3.height*0.4)
        bottomPipe3.x = WIDTH
        bottomPipe3.y = (topPipe3.height + topPipe3.y) + gap

    # bird hits 3rd pipe group
    if bird.colliderect(topPipe3) or bird.colliderect(bottomPipe3):
        print("Game Restarting")
        bird.x = WIDTH*0.18
        bird.y = HEIGHT*0.5
        topPipe1.x = WIDTH*0.33
        topPipe1.y = 0
        bottomPipe1.x = WIDTH*0.33
        bottomPipe1.y = topPipe1.height + gap
        topPipe2.x = WIDTH*0.66
        topPipe2.y = -(topPipe2.height*0.2)
        bottomPipe2.x = WIDTH*0.66
        bottomPipe2.y = (topPipe2.height + topPipe2.y) + gap
        topPipe3.x = WIDTH
        topPipe3.y = -(topPipe3.height*0.4)
        bottomPipe3.x = WIDTH
        bottomPipe3.y = (topPipe3.height + topPipe3.y) + gap

# moving
def on_mouse_down():
    bird.y = bird.y - 50

# runs everything
pgzrun.go() 
