import pygame

class Triangle:
    def __init__(self, screen, points):
        self.screen = screen
        self.points = points
    
    def draw(self):
        pygame.draw.polygon(self.screen, (255,255,255), self.points, 1)
