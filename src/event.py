from resourcesgame import ResourcesGame
from config import (
                    KEY_OPPOSITE,
                    pygame
                    )
class Event(ResourcesGame):

    def __init__(self) -> None:
        super().__init__()
        self.tuple_keydown : tuple = (pygame.K_DOWN,pygame.K_RIGHT,pygame.K_UP,pygame.K_LEFT)

    def keyboard(self, event:pygame) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key in self.tuple_keydown:
                old = KEY_OPPOSITE.get(self.snake.direction)
                self.snake.direction = event.key if old != event.key else self.snake.direction


    def mouse(self, event:pygame) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                if self.btn_retry.x <= mouse_x <= self.btn_retry.x + self.btn_retry.img.get_width() and self.btn_retry.y <= mouse_y <= self.btn_retry.y + self.btn_retry.img.get_height():
                        
                    if self.notif.render(True,"Reinicio","Usted quiere reiniciar la partida?"):
                        self.retryGame()

                if self.btn_pause.x <= mouse_x <= self.btn_pause.x + self.btn_pause.img.get_width() and self.btn_pause.y <= mouse_y <= self.btn_pause.y + self.btn_pause.img.get_height():    
                    self.notif.render(False,"Pausado","El juego esta pausado, toca nuevamente para seguir con la partida")
                    self.pauseGame()