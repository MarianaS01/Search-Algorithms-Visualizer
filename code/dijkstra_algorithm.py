from grid import *
from colors import *
from search_algorithms import SearchAlgorithms

class DijkstraAlgorithm(SearchAlgorithms):
    """
    Colors:
    ORANGE -> Add to visit         = to_visit
    YELLOW -> Already visited      = visited
    KHAKI  -> Check adjacent cells = check_adjacents
    PURPLE -> Replace g            = replace
    GREEN  -> Path                 
    """
    TO_VISIT = ORANGE
    VISITED = YELLOW
    CHECK_ADJACENTS = KHAKI
    REPLACE = PURPLE

    def __init__(self, grid, window, delay=10):
        super().__init__(grid, window, delay=delay)
        self.to_visit = [] # open list
        self.visited = [] # close list
        self.step_cost = 1
        self.neighbours = []

    def add_neighbours(self, cell):
        i = self.grid.linear_grid.index(cell)
        if not self.visited[i]:
            if cell not in self.to_visit:
                self.update_color_state(cell, self.CHECK_ADJACENTS)
            self.neighbours.append(cell)

    def expand(self, current_cell, cell):
        if cell in self.to_visit: 
            new_g = current_cell.g + self.step_cost
            if new_g < cell.g:
                cell.g = new_g
                cell.parent = current_cell
                self.update_color_state(cell, self.REPLACE)
        elif cell not in self.to_visit: 
            new_g = current_cell.g + self.step_cost
            cell.g = new_g
            cell.parent = current_cell
            
            self.update_color_state(cell, self.TO_VISIT)
            self.to_visit.append(cell)

    def get_lowest_g(self):
        cell_lower_g = self.to_visit[0]
        for cell in self.to_visit:
            if cell.g < cell_lower_g.g:
                cell_lower_g = cell
        cell_lower_g_ind = self.to_visit.index(cell_lower_g)
        current_cell = self.to_visit.pop(cell_lower_g_ind)
        return current_cell

    def search(self): 
        if self.safe_to_start(): 
            self.visited = [False for cell in self.grid.linear_grid]
            current_cell = self.grid.origin
            self.to_visit.append(current_cell)

            found = False
            while len(self.to_visit) != 0:
                # search for lowest g
                current_cell = self.get_lowest_g()

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
                    self.expand(current_cell, cell)
                # clean neighbours
                self.neighbours.clear()

            if not found:
                return "PATH NOT FOUND"

        else:
            return "NO ORIGIN OR GOAL"