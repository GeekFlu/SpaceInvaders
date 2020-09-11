import pygame

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Tittle and icon
pygame.display.set_caption("Invasores del Espacio")
icon = pygame.image.load('assets/001-ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("assets/64/016-space-invaders-64.png")
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Player
enemyImg = pygame.image.load("assets/64/012-ufo-4.png")
enemyX = 370
enemyY = 50
enemyX_change = 0
enemyY_change = 0


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


running = True
while running:
    # RGB
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.15
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.15

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
