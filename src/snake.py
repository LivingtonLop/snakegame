import pygame

from config import YELLOW, SIZE_CUBE

class Snake:
    
    def __init__(self) -> None:

        self.rotate : int = 0
        self.color : tuple = YELLOW

    def render (self, screen:pygame):
        pass        
