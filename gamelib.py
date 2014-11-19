import pygame
from pygame.locals import *
 
class SimpleGame(object):
 
    def __init__(self, title, window_size = (640,480), fps=60):
        self.title = title
        self.window_size = window_size
        self.fps = fps
        self.is_terminated = False
    
    def terminated(self):
            self.is_terminated = True

    def __handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.terminate()
            #if pygame.key.get_pressed()[K_UP]:
            #    self.on_key_up(KEYUP)
            #if pygame.key.get_pressed()[K_DOWN]:
            #    self.on_key_down(KEYDOWN)
            #if pygame.key.get_pressed()[K_LEFT]:
            #    self.on_key_left(KEYLEFT)
            #if pygame.key.get_pressed()[K_RIGHT]:
            #    self.on_key_right(KEYRIGHT)        

    def run(self):
        self.init()
        while not self.is_terminated:
            self.update()
            self.render()
            self.clock.tick(self.fps)
            self.__handle_events()
    
    def __game_init(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(self.title)
        self.font = pygame.font.SysFont("monospace", 20)

    def init(self):
        self.__game_init()
 
    def update(self):
        pass
 
    def render(self):
        pass

    def on_key_up(self, key):
        pass
 
    def on_key_down(self, key):
        pass

    def on_key_left(self, key):
        pass
 
    def on_key_right(self, key):
        pass