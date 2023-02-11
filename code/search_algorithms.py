import pygame
from grid import *

class SearchAlgorithms(object):
    def __init__(self, grid, window, delay=10):
        self.grid = grid
        self.delay = delay
        self.window = window

    def update_color_state(self, cell, color):
        cell.color = color 
        pygame.draw.rect(self.window, color, cell.rect)
        if cell == self.grid.origin:
            pygame.draw.rect(self.window, BLUE, cell.rect, 5)
        if cell == self.grid.goal:
            pygame.draw.rect(self.window, RED, cell.rect, 5)

        pygame.display.update(cell.rect)
        pygame.time.delay(self.delay)  

    def get_path(self): 
        path = []
        path.append(self.grid.goal)
        parent = self.grid.goal.parent
        while parent != None:
            path.append(parent)
            parent = parent.parent
        
        reversed_path = list(reversed(path))

        for cell in reversed_path:
            self.update_color_state(cell, GREEN) 

    def safe_to_start(self): 
        its_ok = False
        if self.grid.origin != None and self.grid.goal != None:
            its_ok = True
        return its_ok
