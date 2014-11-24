import pygame
from pygame.locals import *
from gamelib import SimpleGame
from elements import Ball

class SquashGame(SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')

    def __init__(self):
        super(SquashGame, self).__init__("SquashGame",SquashGame.BLACK)
        self.Ball = Ball(radius=10,
                         color = SquashGame.WHITE,
                         pos=(self.window_size[0]/2,
                              self.window_size[1]/2), 
                         speed=(200,50))

    def init(self):
        super(SquashGame, self).init()

    def update(self):
        super(SquashGame, self).update() 

    def render(self, surface):
        #super(SquashGame).render()
        self.Ball.render(surface)

    
    
def main():
    game = SquashGame()
    game.run()
 
if __name__ == '__main__':
    main()
