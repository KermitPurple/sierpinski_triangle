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
            new_points = []
            for i in range(3):
                new_points.append(
                        (self.points[i],
                        ((self.points[i][0] + self.points[(i + 1) % 3][0])/2,(self.points[i][1] + self.points[(i + 1) % 3][1])/2),
                        ((self.points[i][0] + self.points[(i + 2) % 3][0])/2,(self.points[i][1] + self.points[(i + 2) % 3][1])/2),
                        ))
            for points in new_points:
                Triangle(self.screen, points).draw()
