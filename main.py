import pygame
import random

pygame.init()

#-------------------------Screen--------------------------------------------------------------------
screen = pygame.display.set_mode((800,600))
bg = pygame.image.load("images/bg11.jpg")

#-------------------------Title and icon------------------------------------------------------------
pygame.display.set_caption("Space invader")
icon = pygame.image.load("images/spaceship.png")
pygame.display.set_icon(icon)

#------------------------Global variables-----------------------------------------------------------
running = True

#------------------------Player---------------------------------------------------------------------
player_img = pygame.image.load("images/game.png")
px = 340
py = 480
px_move = 0
def player(x,y):
    screen.blit(player_img,(x,y))

#------------------------Enemy----------------------------------------------------------------------
enemy_img = pygame.image.load("images/miscellaneous.png")
ex = random.randint(0,736)
ey = 50
ex_move = 4
ey_move = 40
def enemy(x,y):
    screen.blit(enemy_img,(x,y))

#------------------------Game loop------------------------------------------------------------------
while running:

    screen.fill((0,0,0))
    screen.blit(bg,(0,0))

    #Events and keystrokes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                px_move = 4
            elif event.key == pygame.K_LEFT:
                px_move = -4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                px_move = 0
    
    #Checking boundary for player
    px += px_move
    if px<=0:
        px=0
    elif px>=736:
        px=736

    #Checking boundary for enemy
    ex += ex_move
    if ex<=0:
        ex_move = 4
        ey += ey_move
    elif ex>=736:
        ex_move = -4
        ey += ey_move

    player(px,py)
    enemy(ex,ey)

    pygame.display.update()