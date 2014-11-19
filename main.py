import pygame
from pygame.locals import *
from gamelib import SimpleGame
 
class SquashGame(SimpleGame):
    WHITE = pygame.Color('white')
    def __init__(self):
        super(SquashGame, self).__init__("SquashGame")

    def init(self):
        super(SquashGame, self).init()

    def render(self):
        super(SquashGame, self).render()
        print "render"
        #pygame.draw.circle(surface, WHITE,(self.x, 100), self.radius, 0)

    def update(self):
        super(SquashGame, self).update()
        print "update" 
    

def main():
    game = SquashGame()
    game.run()
 
if __name__ == '__main__':
    main()
