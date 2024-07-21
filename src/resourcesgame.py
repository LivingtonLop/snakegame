from table import Table
from snake import Snake
from button import Button
from notif import Notif

from config import (
                    BLACK, 
                    COOR_SCORE,
                    TITLE_LOS,
                    MESSAGE_LOS,
                    DIRIMAGE_BUTTON_PAUSE,
                    DIRIMAGE_BUTTON_CONTINUE,
                    DIRIMAGE_BUTTON_RETRY,
                    DIRIMAGE_SKIN_APPLE_SCORE,
                    COOR_IMG_SCORE,
                    pygame
                    )
class ResourcesGame:
    def __init__(self) -> None:

        self.execute : bool = True
        self.pause : bool = False

        self.btn_retry = Button(650,100,DIRIMAGE_BUTTON_RETRY, (100,100))
        self.btn_pause = Button(650,250,DIRIMAGE_BUTTON_PAUSE, (100,100))

        self.notif = Notif()

        self.table = Table()
        self.snake = Snake()
        self.coor_food : tuple = self.table.generateCoor()
        self.score : int = 0

    def collisionBodySnake(self)->None: #collision in body snake
        res : bool = False
        h = self.snake.body[0] #head
        for s in list(self.snake.body)[1:]:
            if h == s:
                res = True
        if res:
            if self.notif.render(res,TITLE_LOS,MESSAGE_LOS):
                self.retryGame()
            else: 
                self.execute = False
    
    def collisionSnakeWithFood(self)->None:
        if self.snake.body[0] == self.coor_food:
            self.snake.grow()
            self.coor_food = self.table.generateCoor()  
            #score
            self.score += 1 

    def showScreenScore(self, screen : pygame):
        font = pygame.font.SysFont('Arial',60)
        text = font.render(f"{self.score}", True,BLACK)

        img = pygame.image.load(DIRIMAGE_SKIN_APPLE_SCORE)
        img = pygame.transform.scale(img,(100,100))

        screen.blit(text, COOR_SCORE)
        screen.blit(img, COOR_IMG_SCORE)

    def pauseGame(self):
        self.pause = not self.pause
        
        if self.pause:
            self.btn_pause.img = pygame.image.load(DIRIMAGE_BUTTON_CONTINUE)
        else:
            self.btn_pause.img = pygame.image.load(DIRIMAGE_BUTTON_PAUSE)
        
        self.btn_pause.img = pygame.transform.scale(self.btn_pause.img,self.btn_pause.scale)
            
    def retryGame(self):
        #remove food
        self.snake.reset()
        self.score = 0
        
        self.execute = True
        self.pauseGame()
