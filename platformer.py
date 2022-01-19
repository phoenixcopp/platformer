import pygame
pygame.init()

win = pygame.display.set_mode((1344, 756))

pygame.display.set_caption("platformer game")

walkRight = [pygame.image.load('sprites/Rrun1.png'),pygame.image.load('sprites/Rrun2.png'),pygame.image.load('sprites/Rrun3.png'),pygame.image.load('sprites/Rrun4.png'),pygame.image.load('sprites/Rrun5.png'),pygame.image.load('sprites/Rrun6.png'),pygame.image.load('sprites/Rrun7.png'),pygame.image.load('sprites/Rrun8.png')]
walkLeft = [pygame.image.load('sprites/Lrun1.png'),pygame.image.load('sprites/Lrun2.png'),pygame.image.load('sprites/Lrun3.png'),pygame.image.load('sprites/Lrun4.png'),pygame.image.load('sprites/Lrun5.png'),pygame.image.load('sprites/Lrun6.png'),pygame.image.load('sprites/Lrun7.png'),pygame.image.load('sprites/Lrun8.png')]
char = pygame.image.load('sprites/idle1.png')
bg = pygame.image.load('sprites/snow.png')

clock = pygame.time.Clock()

x = 50
y = 425
width = 128
height = 128
vel = 5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

run = True

def redrawGameWindow():
    global walkCount
    win.blit(bg, (0,0))

    if walkCount + 1 > 24:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x,y))

    pygame.display.update()


while run:
    clock.tick(24)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0

    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

    redrawGameWindow()

pygame.quit()