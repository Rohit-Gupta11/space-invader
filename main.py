import pygame
pygame.init()

#-------------------------Screen--------------------------------------------------------------------
screen = pygame.display.set_mode((800,600))

#-------------------------Title and icon------------------------------------------------------------
pygame.display.set_caption("Space invader")
icon = pygame.image.load("images/spaceship.png")
pygame.display.set_icon(icon)

#------------------------Global variables-----------------------------------------------------------
running = True

#------------------------Player---------------------------------------------------------------------
player_img = pygame.image.load("images/player.png")
px = 340
py = 480
def player(x,y):
    screen.blit(player_img,(x,p))

#------------------------Game loop------------------------------------------------------------------
while running:

    screen.fill((0,114,114))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player(px,py)
    pygame.display.update()