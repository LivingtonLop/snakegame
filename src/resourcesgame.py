import pygame

from table import Table
from snake import Snake
from button import Button
from notif import Notif

from config import BLACK, COOR_SCORE, TITLE_LOS, TITLE_PAS, MESSAGE_LOS,MESSAGE_PAS

class ResourcesGame:
    def __init__(self) -> None:

        self.execute : bool = True
        self.pause : bool = False

        self.buttons = Button()
        self.notif = Notif()

        self.table = Table()
        self.snake = Snake()
        self.coor_food : tuple = self.table.generateCoor()
        self.score : int = 0

    def collision(self) -> bool: #collision in walls
        res : bool = False
        return res

    def collisionBodySnake(self)->None: #collision in body snake
        res : bool = False
        h = self.snake.body[0] #head
        for s in list(self.snake.body)[1:]:
            if h == s:
                res = True
        if res:
            self.notif.render(res,TITLE_LOS,MESSAGE_LOS)
    
    def collisionSnakeWithFood(self)->None:
        if self.snake.body[0] == self.coor_food:
            self.snake.grow()
            self.coor_food = self.table.generateCoor()  
            #score
            self.score += 1 

    def showScreenScore(self, screen : pygame):
        font = pygame.font.SysFont('Arial',24)
        text = font.render(f"Puntuacion: {self.score}", True, BLACK)
        screen.blit(text, COOR_SCORE)

    def renderButtons(self):
        pass

    def pauseGame(self):
        pass

    def retryGame(self):
        pass