# Node representation
import pygame
from colors import *
from dimensions import *

class Cell(object):
    def __init__(self, pos, color, parent=None):
        self.row, self.col = pos
        self.parent = parent
        self.color = color
        self.rect = None
        self.g = 0
        self.h = 0
        self.f = 0

    def is_clicked(self):
        self.click = False
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            self.click = True
        return self.click

    def change_color(self, current_color):
        if current_color == self.color:
            self.color = WHITE
        else:
            self.color = current_color

class Grid(object):
    def __init__(self, num_rows, num_cols):
        self.grid = []
        self.linear_grid = [] # to reference easily in one dimension
        self.origin = None
        self.goal = None

        for i in range(num_rows):
            rows = []
            for j in range(num_cols):
                _cell = Cell((i, j), WHITE)
                rows.append(_cell)
                self.linear_grid.append(_cell)
            self.grid.append(rows)

    def draw_grid(self, window):
        for row in self.grid:
            for cell in row:
                pos_rec_x = cell.row * (CELL_WIDTH + CELLS_MARGIN) + MARGIN
                pos_rec_y = cell.col * (CELL_HEIGHT + CELLS_MARGIN) + MARGIN
                cell.rect = pygame.Rect((pos_rec_x, pos_rec_y, CELL_WIDTH, CELL_HEIGHT))
                pygame.draw.rect(window, cell.color, cell.rect)
                if cell == self.origin:
                    pygame.draw.rect(window, BLUE, cell.rect, 5)
                if cell == self.goal:
                    pygame.draw.rect(window, RED, cell.rect, 5)

    def fill_grid(self, current_color):
        for cell in self.linear_grid:
            if cell.is_clicked():
                if current_color == BLUE:
                    if self.origin == None:
                        cell.change_color(current_color)
                    else:
                        self.origin.change_color(WHITE)
                        cell.change_color(current_color)
                        
                    self.origin = cell
                
                elif current_color == RED:
                    if self.goal == None:
                        cell.change_color(current_color)
                    else:
                        self.goal.change_color(WHITE)
                        cell.change_color(current_color)
                    self.goal = cell    

                else:
                    if cell.color == current_color:
                        cell.change_color(WHITE)
                    else:
                        if cell.color == BLUE:
                            self.origin = None
                        if cell.color == RED:
                            self.goal = None
                        cell.change_color(current_color)

    def clean_grid(self):
        for cell in self.linear_grid:
            if cell.color != WHITE:
                cell.color = WHITE
        self.origin = None
        self.goal = None

    def delete_path(self):
        for cell in self.linear_grid:
            if cell.color != BLACK:
                cell.color = WHITE
        
        self.origin.color = BLUE
        self.goal.color = RED