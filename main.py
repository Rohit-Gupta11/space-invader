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

#------------------------Game loop------------------------------------------------------------------
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False