import pygame

from config import YELLOW, SIZE_CUBE

class Snake:
    
    def __init__(self) -> None:
        
        self.color : tuple = YELLOW

    def render (self, screen:pygame):
        pass        

    def move(self):
        pass

    def eat(self) ->bool:
        eat : bool = True
        return eat 
        