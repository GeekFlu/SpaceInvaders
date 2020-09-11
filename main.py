import math
import random

import pygame

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load("assets/background-800x600.png")

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

# Enemy
enemyImg = pygame.image.load("assets/64/012-ufo-4.png")
enemyX = random.randint(0, 735)
enemyY = random.randint(50, 150)
enemyX_change = 2.5
enemyY_change = 30

# Bullet
bulletImg = pygame.image.load("assets/001-bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 4
bullet_state = "ready"

score = 0


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    if distance < 27:
        return True
    return False


running = True
while running:
    # RGB
    screen.fill((0, 0, 0))

    # Background
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 2.5
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -2.5
        enemyY += enemyY_change

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Collision
    collision = is_collision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)
        print(score)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
