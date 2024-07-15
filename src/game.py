import pygame
from resourcesgame import ResourcesGame

class Game (ResourcesGame):
    def __init__(self) -> None:\
    
        super().__init__()
    
        self.clock = pygame.time.Clock()
    
    def run (self):

        while self.execute:
    
            # self.events()
            # self.update()
            self.render()
            self.clock.tick(60)
    
        pygame.quit()

    def render(self):
        pass