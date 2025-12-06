import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))  # width x height
pygame.display.set_caption("Blue Sky")

blue = (135, 206, 235)  # sky blue

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(blue)

    pygame.display.flip()

pygame.quit()
sys.exit()
