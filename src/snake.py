from config import (
                    YELLOW,
                    SNAKE_BODY,
                    SIZE_CUBE,
                    deque,
                    pygame)
class Snake:
    
    def __init__(self) -> None:
        
        self.color : tuple = YELLOW
        self.body = deque(SNAKE_BODY)
        self.direction = pygame.K_RIGHT

    def render (self, screen:pygame):
        for segment in self.body:
            pygame.draw.rect(screen,self.color,(*segment,SIZE_CUBE,SIZE_CUBE))

    def move(self):
        
        x, y = self.body[0]

        dict_dir : dict = {
            pygame.K_UP : (x, y - SIZE_CUBE) ,
            pygame.K_DOWN : (x, y + SIZE_CUBE),
            pygame.K_RIGHT: (x + SIZE_CUBE, y),
            pygame.K_LEFT :(x - SIZE_CUBE, y)
       }

        self.body.appendleft(dict_dir.get(self.direction))
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
    
    def reset(self):
        self.body = deque(SNAKE_BODY)
        self.direction = pygame.K_RIGHT