import pygame

# Color definitions
START_COLOR = (50, 205, 50)
END_COLOR = (255, 69, 0)
BARRIER_COLOR = (0, 0, 0)
PATH_COLOR = (30, 144, 255)
OPEN_COLOR = (173, 216, 230)
CLOSED_COLOR = (255, 0, 255)
BACKGROUND_COLOR = (255, 255, 255)

class Node:
    def __init__(self, row, column, width, total_rows):
        self.row = row
        self.column = column
        self.x = row * width
        self.y = column * width
        self.color = BACKGROUND_COLOR
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows

    def get_position(self):
        return self.row, self.column

    def is_closed(self):
        return self.color == CLOSED_COLOR

    def is_open(self):
        return self.color == OPEN_COLOR

    def is_barrier(self):
        return self.color == BARRIER_COLOR

    def is_start(self):
        return self.color == START_COLOR

    def is_end(self):
        return self.color == END_COLOR

    def reset(self):
        self.color = BACKGROUND_COLOR

    def set_closed(self):
        self.color = CLOSED_COLOR

    def set_opened(self):
        self.color = OPEN_COLOR

    def set_barrier(self):
        self.color = BARRIER_COLOR

    def set_end(self):
        self.color = END_COLOR

    def set_start(self):
        self.color = START_COLOR

    def set_path(self):
        self.color = PATH_COLOR

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))

    def set_neighbors(self, grid):
        self.neighbours = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.column].is_barrier():
            self.neighbours.append(grid[self.row + 1][self.column])
        if self.row > 0 and not grid[self.row - 1][self.column].is_barrier():
            self.neighbours.append(grid[self.row - 1][self.column])
        if self.column < self.total_rows - 1 and not grid[self.row][self.column + 1].is_barrier():
            self.neighbours.append(grid[self.row][self.column + 1])
        if self.column > 0 and not grid[self.row][self.column - 1].is_barrier():
            self.neighbours.append(grid[self.row][self.column - 1])

    def __lt__(self, other):
        return False
