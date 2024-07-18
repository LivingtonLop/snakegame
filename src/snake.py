import pygame

from config import YELLOW, SNAKE_BODY, SIZE_CUBE
class Snake:
    
    def __init__(self) -> None:
        
        self.color : tuple = YELLOW
        self.body = SNAKE_BODY
        self.direction = pygame.K_RIGHT
        

    def render (self, screen:pygame):
        for segment in self.body:
            pygame.draw.rect(screen,self.color,(*segment,SIZE_CUBE,SIZE_CUBE))

    def move(self):
        new_head : tuple

        x, y = self.body[0]

        if self.direction == pygame.K_UP:
            new_head = (x, y - SIZE_CUBE)
        elif self.direction == pygame.K_DOWN:
            new_head = (x, y + SIZE_CUBE)
        elif self.direction == pygame.K_LEFT:
            new_head = (x - SIZE_CUBE, y)
        elif self.direction == pygame.K_RIGHT:
            new_head = (x + SIZE_CUBE, y)

        self.body.appendleft(new_head)
        self.body.pop()

    def grow(self):
        tail_end_x, tail_end_y = self.body[-1]
        tail_second_last_x, tail_second_last_y = self.body[-2]

        # Calculate the direction of growth
        if tail_end_x == tail_second_last_x:
            # Growing vertically
            if tail_end_y > tail_second_last_y:
                new_segment = (tail_end_x, tail_end_y + SIZE_CUBE)
            else:
                new_segment = (tail_end_x, tail_end_y - SIZE_CUBE)
        else:
            # Growing horizontally
            if tail_end_x > tail_second_last_x:
                new_segment = (tail_end_x + SIZE_CUBE, tail_end_y)
            else:
                new_segment = (tail_end_x - SIZE_CUBE, tail_end_y)

        self.body.append(new_segment)   
        