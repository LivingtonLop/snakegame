import pygame

from table import Table
from snake import Snake
class ResourcesGame:
    def __init__(self) -> None:

        self.execute : bool = True
        self.pause : bool = False

        self.table = Table()
        self.snake = Snake()
        self.eatfood : bool
