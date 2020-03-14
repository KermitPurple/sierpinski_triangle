import pygame

class Triangle:
    def __init__(self, screen, points):
        self.screen = screen
        self.points = points
    
    def draw(self):
        pygame.draw.polygon(self.screen, (255,255,255), self.points, 1)
        xdist = abs(self.points[0][0] - self.points[1][0])
        ydist = abs(self.points[0][1] - self.points[1][1])
        if (xdist + ydist) / 2 > 1:
            new_points = [0,0,0]
            new_points[0] = (int((self.points[0][0] + self.points[1][0]) / 2), int((self.points[0][1] + self.points[1][1]) / 2))
            new_points[1] = (int((self.points[1][0] + self.points[2][0]) / 2), int((self.points[1][1] + self.points[2][1]) / 2))
            new_points[2] = (int((self.points[2][0] + self.points[0][0]) / 2), int((self.points[2][1] + self.points[0][1]) / 2))
            Triangle(self.screen, new_points).draw()
