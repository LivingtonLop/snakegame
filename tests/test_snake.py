import unittest
import pygame
from collections import deque

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from snake import Snake
from config import SIZE_CUBE, YELLOW

class TestSnake(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.screen = pygame.Surface((800, 600))  # Tamaño de pantalla ficticio para pruebas
        self.snake = Snake()

    def test_initial_state(self):
        # Valor esperado de SNAKE_BODY
        expected_body = deque([(3*SIZE_CUBE, 3*SIZE_CUBE), (2*SIZE_CUBE, 3*SIZE_CUBE), (1*SIZE_CUBE, 3*SIZE_CUBE)])
        self.assertEqual(self.snake.body, expected_body)
        self.assertEqual(self.snake.direction, pygame.K_RIGHT)
        self.assertEqual(self.snake.color, YELLOW)

    def test_move(self):
        self.snake.move()
        expected_body = deque([(4*SIZE_CUBE, 3*SIZE_CUBE), (3*SIZE_CUBE, 3*SIZE_CUBE), (2*SIZE_CUBE, 3*SIZE_CUBE)])
        self.assertEqual(self.snake.body, expected_body)
    
    def test_grow(self):
        self.snake.move()  # Mueve la serpiente para modificar la posición
        self.snake.grow()
        expected_body = deque([(4*SIZE_CUBE, 3*SIZE_CUBE), (3*SIZE_CUBE, 3*SIZE_CUBE), (2*SIZE_CUBE, 3*SIZE_CUBE), (1*SIZE_CUBE, 3*SIZE_CUBE)])
        self.assertEqual(self.snake.body, expected_body)
    
    def test_reset(self):
        self.snake.move()
        self.snake.grow()
        self.snake.reset()
        expected_body = deque([(3*SIZE_CUBE, 3*SIZE_CUBE), (2*SIZE_CUBE, 3*SIZE_CUBE), (1*SIZE_CUBE, 3*SIZE_CUBE)])
        self.assertEqual(self.snake.body, expected_body)
        self.assertEqual(self.snake.direction, pygame.K_RIGHT)

    def test_render(self):
        # Renderizar la serpiente
        self.snake.render(self.screen)

        for segment in self.snake.body:
            x, y = segment
            for dx in range(SIZE_CUBE):
                for dy in range(SIZE_CUBE):
                    pixel_color = self.screen.get_at((x + dx, y + dy))
                    self.assertEqual(pixel_color, YELLOW)

if __name__ == '__main__':
    unittest.main()
