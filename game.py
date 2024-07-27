import numpy as np

class game_of_life:
    def __init__(self, grid_size=20, start_alive=15):
        self.grid_size = grid_size
        self.start_alive = start_alive
        self.grid = self.initialize_grid()
        self.previous_grids = []
        self.max_history = 6  # Number of previous states to check for oscillation (this is equivalent to a "Pulsar")

    def initialize_grid(self):
        grid = np.zeros((self.grid_size, self.grid_size), dtype=int)
        alive_cells = np.random.choice(self.grid_size * self.grid_size, self.start_alive, replace=False)
        for cell in alive_cells:
            row = cell // self.grid_size
            column = cell % self.grid_size
            grid[row, column] = 1
        return grid
        
    def update_grid(self):
        new_grid = self.grid.copy()
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                alive_neighbors = np.sum(self.grid[max(0, i-1):min(self.grid_size, i+2),
                                          max(0, j-1):min(self.grid_size, j+2)]) - self.grid[i, j]
                if self.grid[i, j] == 1:
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        new_grid[i, j] = 0
                else:
                    if alive_neighbors == 3:
                        new_grid[i, j] = 1

        self.previous_grids.append(self.grid.tolist())
        if len(self.previous_grids) > self.max_history:
            self.previous_grids.pop(0)

        self.grid = new_grid
        return self.grid

    def get_grid(self):
        return self.grid.tolist()
    
    def toggle_cell(self, row, col):
        self.grid[row, col] = 1 if self.grid[row, col] == 0 else 0

    def check_termination(self):
        return np.sum(self.grid) == 0

    def check_still_life(self):
        return len(self.previous_grids) > 0 and self.previous_grids[-1] == self.grid.tolist()

    def check_oscillator(self):
        if len(self.previous_grids) < 3:
            return False
        return self.grid.tolist() in self.previous_grids[-6:]
    
    def detect_end_condition(self):
        if self.check_termination():
            return "Termination: All cells are dead."
        elif self.check_still_life():
            return "Still Life: No changes between steps."
        elif self.check_oscillator():
            return "Oscillator Convergence: Grid matches a previous state."
        return None