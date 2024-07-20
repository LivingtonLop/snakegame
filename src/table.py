import random

from config import (
                    SIZE_CUBE,
                    BLACK,
                    COLUMN_TABLE,
                    ROW_TABLE,
                    WIDTH_TABLE,
                    HEIGHT_TABLE,
                    RED,
                    pygame)

class Table:
    
    def __init__(self) -> None :

        self.map: list = [
            [   # "_" -> var no use
                BLACK for _ in range (COLUMN_TABLE)
            ]
            for _ in range (ROW_TABLE)
        ]


    def render(self, screen : pygame) -> None:
        for y in range(ROW_TABLE):
            for x in range(COLUMN_TABLE):

                rect : tuple = (x*SIZE_CUBE, y*SIZE_CUBE, SIZE_CUBE, SIZE_CUBE)
                
                pygame.draw.rect(
                                    screen,
                                    BLACK,
                                    rect,
                                    1
                                )
                if self.map[y][x] != BLACK:
                    pygame.draw.rect(
                                    screen,
                                    self.map[y][x],
                                    rect
                                )
    
    def generateCoor(self)->tuple:

        x = random.randint(0,WIDTH_TABLE//SIZE_CUBE-1) * SIZE_CUBE
        y = random.randint(0,HEIGHT_TABLE//SIZE_CUBE-1) * SIZE_CUBE

        return (x,y)
    
    def generateFood(self,screen : pygame, coor_food : tuple):
        
        pygame.draw.rect(screen,RED,(*coor_food,SIZE_CUBE,SIZE_CUBE))
        
        