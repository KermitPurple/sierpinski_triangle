import pygame
import os
from Triangle import Triangle
os.environ["SDL_VIDEO_WINDOW_POS"] = "15,30"

pygame.display.init()
size = (600,600)
screen = pygame.display.set_mode(size)
triangle = Triangle(screen, ((size[0]/2,5), (size[0]-5,size[1]-5), (5,size[1]-5)))
triangle.draw()
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
