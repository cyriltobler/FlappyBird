import pygame
import random

pygame.init()


screen = pygame.display.set_mode([400, 400])
pygame.display.set_caption("Flappy Bird")

spacebtw = 100
score = 0


#creat obstacles
obstacles = []
obstaclecount = 100
for x in range(obstaclecount):
    class Test:
        x = 400 + x * 170
        y = random.randrange(50,350 - spacebtw)
    obstacles.insert(x, Test())

birdY = 200
isJump = False
jumpCount = 10


def update():
    global score
    score += 1
    for x in range(obstaclecount):
        obstacles[x].x -= 1

def draw():
    pygame.draw.circle(screen, (255, 255, 0), (50, birdY), 15)
    for x in range(obstaclecount):
        pygame.draw.rect(screen, (255, 40, 0), (obstacles[x].x, 0, 20, obstacles[x].y))
        pygame.draw.rect(screen, (255, 40, 0), (obstacles[x].x, obstacles[x].y + spacebtw, 20, 400 - obstacles[x].y - spacebtw))

def collision():
    collision = False
    if birdY < 400 and birdY > 0:
        for x in range(obstaclecount):
            if obstacles[x].x > 43 and obstacles[x].x < 57:
                if birdY >  obstacles[x].y + spacebtw + 8 or birdY < obstacles[x].y - 8:
                    collision = True
    else:
        collision = True

    if collision:
        global score
        score = (score - 400) / 100
        print(score)
        global run
        run = False





run = True

while run:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if keys[pygame.K_SPACE]:
            isJump = True
            
    if isJump:
        if jumpCount >= 0:
            birdY -= (jumpCount * abs(jumpCount)) * 0.15
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False
    else:
        birdY += 1

    update()
    collision()




    screen.fill((0, 0, 0))
    draw()
    pygame.display.update() 
    pygame.time.wait(5)

pygame.time.delay(1000)
pygame.quit()
