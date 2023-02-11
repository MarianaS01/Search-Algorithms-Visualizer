from math import sqrt
from grid import *
from colors import *
from dijkstra_algorithm import DijkstraAlgorithm

class AStar(DijkstraAlgorithm):
    def __init__(self, grid, window, delay=10):
        super().__init__(grid, window, delay=delay)

    def get_lowest_f(self):
        cell_lower_f = self.to_visit[0]
        for cell in self.to_visit:
            if cell.f < cell_lower_f.f:
                cell_lower_f = cell
        cell_lower_f_ind = self.to_visit.index(cell_lower_f)
        current_cell = self.to_visit.pop(cell_lower_f_ind)
        return current_cell
        
    def manhattan_distance(self, cell):
        d = abs(cell.row - self.grid.goal.row) + abs(cell.col - self.grid.goal.col)
        return d

    def euclidian_distance(self, cell):
        d = int(sqrt(abs(cell.row - self.grid.goal.row)**2 + abs(cell.col - self.grid.goal.col)**2))
        return d

    def chebyshev_distance(self, cell):
        d = abs(cell.row - self.grid.goal.row)
        return d

    def expand(self, current_cell, cell, heuristic): 
        new_h = 0
        new_g = current_cell.g + self.step_cost
        if heuristic == 'Manhattan distance': 
            new_h = self.manhattan_distance(cell)
        if heuristic == 'Euclidian distance': 
            new_h = self.euclidian_distance(cell)
        if heuristic == 'Chebyshev distance': 
            new_h = self.chebyshev_distance(cell)
        new_f = new_g + new_h  

        if cell in self.to_visit: 
            if new_f < cell.f:
                cell.g = new_g
                cell.h = new_h
                cell.f = new_f
                cell.parent = current_cell
                self.update_color_state(cell, self.REPLACE)
        
        elif cell not in self.to_visit:           
            cell.g = new_g
            cell.h = new_h
            cell.f = new_f
            cell.parent = current_cell
            
            self.update_color_state(cell, self.TO_VISIT)
            self.to_visit.append(cell)    

    def search(self, heuristic): 
        if self.safe_to_start(): 
            self.visited = [False for cell in self.grid.linear_grid]
            current_cell = self.grid.origin
            self.to_visit.append(current_cell)

            found = False
            while len(self.to_visit) != 0:
                # search for lowest f
                current_cell = self.get_lowest_f()

                # add to visited
                self.update_color_state(current_cell, self.VISITED)
                
                i = self.grid.linear_grid.index(current_cell)
                self.visited[i] = True

                if current_cell == self.grid.goal:
                    self.get_path() 
                    found = True
                    break
                # else: check adjacent cells
                # RIGHT
                r = current_cell.row + 1
                c = current_cell.col                
                if r < len(self.grid.grid):
                    cell = self.grid.grid[r][c]
                    if cell.color != BLACK:
                        self.add_neighbours(cell)
                    
                # LEFT
                r = current_cell.row - 1
                c = current_cell.col
                if r >= 0:
                    cell = self.grid.grid[r][c]
                    if cell.color != BLACK:
                        self.add_neighbours(cell)
                    
                # UP
                r = current_cell.row
                c = current_cell.col + 1
                if c < len(self.grid.grid[0]):
                    cell = self.grid.grid[r][c]
                    if cell.color != BLACK:
                        self.add_neighbours(cell)
                    
                # DOWN
                r = current_cell.row
                c = current_cell.col - 1
                if c >= 0:
                    cell = self.grid.grid[r][c]
                    if cell.color != BLACK:
                        self.add_neighbours(cell)

                for cell in self.neighbours:
                    self.expand(current_cell, cell, heuristic)
                # clean neighbours
                self.neighbours.clear()

            if not found:
                return "PATH NOT FOUND"

        else:
            return "NO ORIGIN OR GOAL"