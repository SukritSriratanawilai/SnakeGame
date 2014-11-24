import pygame
from pygame.locals import *

class Ball(object):

    def __init__(self,radius,color,pos, speed=(100,0)):
        (self.x, self.y) = pos
        (self.vx, self.vy) = speed
        self.radius = radius
        self.color = color

    def render(self, surface):
        pos = (int(self.x),int(self.y))
        pygame.draw.circle(surface, self.color, pos, self.radius, 0)