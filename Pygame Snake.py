import pygame, sys, random
pygame.init()

#Sets the size of the window
window = pygame.display.set_mode((600, 600))

#generates random location to start
x = random.randrange(0, 575, 25)
y = random.randrange(0, 575, 25)

# Setup
headXY = [x, y]
width = 25
height = 25
vel = 25
direct = '__'
play = False
end = False
scoreDisplay = True
scoreCount = 0
myfont = pygame.font.SysFont('Impact', 30)

# to define movement, score, and drawing for ease of access
def movement():
    global headXY
    global play
    if direct == 'Left' and headXY[0] > 0 and play != False:
        headXY[0] -= vel
    if direct == 'Right' and headXY[0] < 575 and play != False:
        headXY[0] += vel
    if headXY[1] > 0 and direct == 'Up' and play != False:
        headXY[1] -= vel
    if direct == 'Down' and headXY[1] < 575 and play != False:
        headXY[1] += vel
def draw(x, y):
    global width, height
    pygame.draw.rect(window, (0, 255, 0), (x, y, width, height))
def show_Score():
    global scoreCount
    score = myfont.render(str(scoreCount), True, (255, 255, 255))
    window.blit(score, (10, 10))

#more setup
Quit = False
restartSys = True
run = True
quitting = False

# Puts the entire game in a loop so it can restart
while restartSys:
    #generates random location to start
    x = random.randrange(0, 575, 25)
    y = random.randrange(0, 575, 25)

    # For if it restarts
    scoreCount = 0
    scoreDisplay = True
    play = False
    headXY = [x, y]
    snakeBodyX = []
    snakeBodyY = []
    applesEaten = [0]
    preXY = [headXY[0], headXY[1]]
    direct = '__'

    #Draw first apple
    aX = random.randrange(0, 575, 25)
    aY = random.randrange(0, 575, 25)
    apple = [aX, aY]
    pygame.draw.rect(window, (255, 0, 0), (aX, aY, width, height))

    # The game itself
    while end == False:
        show_Score()
        # Checks if the window is closed
        for event in pygame.event.get():
            # if it is closed, it ends the game and goes to **
            if event.type == pygame.QUIT:
                end = True
                run = False
                quitting = True

        # Gets what keys are being pressed
        keys = pygame.key.get_pressed()

        # Gets it's last location
        preXY = [headXY[0], headXY[1]]

        # Movement
        if keys[pygame.K_LEFT] and direct != 'Right':
            direct = 'Left'
            play = True
        if keys[pygame.K_RIGHT] and direct != 'Left':
            direct = 'Right'
            play = True
        if keys[pygame.K_UP] and direct != 'Down':
            direct = 'Up'
            play = True
        if keys [pygame.K_DOWN] and direct != 'Up':
            direct = 'Down'
            play = True
        movement()

        #Draws the location of the apples, and if the head is ontop of said apple, it grows
        window.fill((0, 0, 0))
        pygame.draw.rect(window, (255, 0, 0), (aX, aY, width, height))
        if apple == headXY:
            aX = random.randrange(0, 575, 25)
            aY = random.randrange(0, 575, 25)
            apple = [aX, aY]
            scoreCount += 2
            applesEaten.append(1)
            applesEaten.append(1)

        #Shows the Score
        
            
        
        # Records the location of the snake head
        tempX = headXY[0]
        tempY = headXY[1]
        snakeBodyX.insert(0, tempX)
        snakeBodyY.insert(0, tempY)

        #To be used to filter from one segment to the next
        i = 0
        
        # Checks if it is in the same place and if it is, it 'ends the game.
        # Can only be in the same place if it against a wall
        if preXY[0] == headXY[0] and preXY[1] == headXY[1] and play == True:
            end = True

        pygame.time.delay(100)

        # for the amount of apples eaten, it draws the snake where it was 1 place ago
        for point in applesEaten:
            x = snakeBodyX[i]
            y = snakeBodyY[i]
            draw(x, y)
            collideXY = [x, y]
            if i > 0 and collideXY == headXY:
                end = True
            i += 1
        pygame.display.update()

    if run == True:
        while scoreDisplay:
            
            # The display window for the Restart Screen
            pygame.draw.rect(window, (0, 51, 8), (100, 200, 400, 200))
            pygame.font.init()
            textsurface = myfont.render('Restart? Press R', False, (255, 255, 255))
            window.blit(textsurface, (190,280))
            pygame.display.update()

            # If window is closed when the game isn't running
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            # Checks if r is pressed, and if it is, it restarts it
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                end = False
                
                scoreDisplay = False
                
    # ** which ends the game.
    if quitting == True:
        pygame.quit()
