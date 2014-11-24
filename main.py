import pygame
from pygame.locals import *
from gamelib import SimpleGame
from elements import *

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
        self.Player = Player(pos = 100,
                             color = SquashGame.GREEN)

    def init(self):
        super(SquashGame, self).init()

    def update(self):
        self.Ball.move(1./self.fps, self.surface)

        if pygame.key.get_pressed()[K_UP]:
            self.Player.move_up()
        elif pygame.key.get_pressed()[K_DOWN]:
            self.Player.move_down()

    def render(self, surface):
        self.Ball.render(surface)
        self.Player.render(surface)

    
    
def main():
    game = SquashGame()
    game.run()
 
if __name__ == '__main__':
    main()
