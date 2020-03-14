import pygame
import os
from Triangle import Triangle
os.environ["SDL_VIDEO_WINDOW_POS"] = "15,30"

pygame.display.init()
size = (700,700)
screen = pygame.display.set_mode(size)
triangle = Triangle(((size[0]/2,0), (size[0],size[1]), (0,size[1])))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    pygame.display.update()
