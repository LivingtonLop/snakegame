import pygame

from config import SIZE_CUBE, BLACK,COLUMN_TABLE, ROW_TABLE

class Table:
    
    def __init__(self) -> None :

        self.map: list = [
            [   # "_" -> var no use
                BLACK for _ in range (COLUMN_TABLE)
            ]
            for _ in range (ROW_TABLE)
        ]

    def render(self, screen : pygame) -> None:
        for x in range(ROW_TABLE):
            for y in range(COLUMN_TABLE):
                rect : tuple = (y*SIZE_CUBE, x*SIZE_CUBE, SIZE_CUBE, SIZE_CUBE)
                pygame.draw.rect(
                                    surface= screen,
                                    color= BLACK,
                                    rect= rect,
                                    width=1
                                )
                if self.map[x][y] != BLACK:
                    pygame.draw.rect(
                                    surface= screen,
                                    color= self.map[x][y],
                                    rect= rect,
                                    width=1
                                )
    
    def confirmEat(self)->int:
        food = 0
        #logic

        return food * 10