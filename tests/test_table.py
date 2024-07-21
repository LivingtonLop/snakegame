import unittest
import pygame
import random

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from table import Table
from config import SIZE_CUBE, BLACK, COLUMN_TABLE, ROW_TABLE, WIDTH_TABLE, HEIGHT_TABLE, RED

class TestTable(unittest.TestCase):
    
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH_TABLE, HEIGHT_TABLE))
        self.table = Table()

    def test_generateCoor(self):
        for _ in range(100):  # Ejecutar varias veces para asegurar diferentes resultados
            x, y = self.table.generateCoor()
            self.assertTrue(0 <= x < WIDTH_TABLE)
            self.assertTrue(0 <= y < HEIGHT_TABLE)
            self.assertEqual(x % SIZE_CUBE, 0)
            self.assertEqual(y % SIZE_CUBE, 0)

    def test_generateFood(self):
        coor_food = self.table.generateCoor()
        self.table.generateFood(self.screen, coor_food)
        
        # Capturar el color del pixel en la posición de la comida
        x, y = coor_food
        pixel_color = self.screen.get_at((x + SIZE_CUBE // 2, y + SIZE_CUBE // 2))
        
        self.assertEqual(pixel_color, RED)

    def test_render(self):
        self.table.render(self.screen)
        
        for y in range(ROW_TABLE):
            for x in range(COLUMN_TABLE):
                rect = (x * SIZE_CUBE, y * SIZE_CUBE, SIZE_CUBE, SIZE_CUBE)
                
                # Capturar el color del pixel en el centro de cada celda
                pixel_color = self.screen.get_at((x * SIZE_CUBE + SIZE_CUBE // 2, y * SIZE_CUBE + SIZE_CUBE // 2))
                
                self.assertEqual(pixel_color, BLACK)

if __name__ == '__main__':
    unittest.main()
