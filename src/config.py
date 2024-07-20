import pygame
from collections import deque

WIDTH  :int = 900
HEIGHT :int = 600
NAME_GAME : str = "Snake" 

WIDTH_TABLE :int = 600
HEIGHT_TABLE :int = 600

SIZE_CUBE :int = 30

COLUMN_TABLE :int = WIDTH_TABLE//SIZE_CUBE
ROW_TABLE :int = HEIGHT_TABLE//SIZE_CUBE

SNAKE_BODY = deque ([(3*SIZE_CUBE, 3*SIZE_CUBE), (2*SIZE_CUBE, 3*SIZE_CUBE), (1*SIZE_CUBE, 3*SIZE_CUBE)])
#logo
ICO_GAME :str = "assets/image/logo/snakegame_logo.ico"
LOGO_GAME :str = "assets/image/logo/snakegame_logo.png"

#buttons
DIRIMAGE_BUTTON_CONTINUE :str = "assets/image/buttons/continue.png"
DIRIMAGE_BUTTON_PAUSE :str = "assets/image/buttons/pause.png"
DIRIMAGE_BUTTON_RETRY :str = "assets/image/buttons/retry.png"

#skins
DIRIMAGE_SKIN_APPLE_SCORE : str = "assets/image/skins/skini_apple_score.png"

BLACK :tuple = (0,0,0)
WHITE :tuple = (255,255,255)
RED : tuple = (0,255,0)
YELLOW : tuple = (255,255,0)

#Coordenas elements

COOR_SCORE :tuple = (800,10)
COOR_IMG_SCORE : tuple = (650, 10)
#message

TITLE_LOS : str = "Game Over"
MESSAGE_LOS : str = "You had Loser, please press 'yes' to retry or 'no' to close the game"

TITLE_PAS : str = "Game Pause"
MESSAGE_PAS : str = "You pause the game, press icon retry to remove the pause"

#oppocite
KEY_OPPOSITE = {
    pygame.K_UP: pygame.K_DOWN,
    pygame.K_DOWN: pygame.K_UP,
    pygame.K_LEFT: pygame.K_RIGHT,
    pygame.K_RIGHT: pygame.K_LEFT
}