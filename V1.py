import pygame

pygame.init()

win = pygame.display.set_mode((800, 600))

pygame.mixer.music.load('music.mp3')  # adiciona musica
pygame.mixer.music.play(-1)  # tempo da musica

walkRight = [pygame.image.load('R1.png'),
             pygame.image.load('R2.png'),
             pygame.image.load('R3.png')]
walkLeft = [pygame.image.load('L1.png'),
            pygame.image.load('L2.png'),
            pygame.image.load('L3.png')]
bg = pygame.image.load('bg.png')
char = pygame.image.load('standing.png')


clock = pygame.time.Clock()

x = 620  # 620
y = 440  # 440
width = 64
height = 64
vel = 10
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0


def redrawGameWindow():
    global walkCount

    win.blit(bg, (0, 0))
    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))

    pygame.display.update()


# Loop principal
run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
# controles

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 750 - width - vel:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
    walkCount = 0

    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 1 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    redrawGameWindow()

pygame.quit()
