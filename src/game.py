import pygame
from config import WHITE, WIDTH, HEIGHT, NAME_GAME
from event import Event

class Game (Event):
    def __init__(self) -> None:
    
        super().__init__()
        
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(NAME_GAME)

        self.clock = pygame.time.Clock()
    
    def run (self):

        while self.execute:
    
            self.events()
            self.update()
            self.render()
            self.clock.tick(60)
    
        pygame.quit()

    #import
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.execute = False
            #events
            self.keyboard(event=event)
            self.mouse(event=event)

    def update(self):
        self.eatfood = self.snake.eat()
        pass

    def render(self):
        self.screen.fill((WHITE))
        
        self.table.render(self.screen)
        self.snake.render(self.screen)
        self.table.generateFood(self.screen,self.eatfood)

        pygame.display.update()