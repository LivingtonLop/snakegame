import pygame
from resourcesgame import ResourcesGame
class Event(ResourcesGame):

    def __init__(self) -> None:
        super().__init__()
        self.tuple_keydown : tuple = (pygame.K_DOWN,pygame.K_RIGHT,pygame.K_UP,pygame.K_LEFT)

    def keyboard(self, event:pygame) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key in self.tuple_keydown:
                self.snake.direction = event.key

    def mouse(self, event:pygame) -> None:
        pass