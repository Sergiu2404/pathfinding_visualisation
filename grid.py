import pygame
from node import Node

GRID_COLOR = (169, 169, 169)
BACKGROUND_COLOR = (255, 255, 255)
BUTTON_COLOR = (50, 150, 50)
BUTTON_HOVER_COLOR = (70, 170, 70)
BUTTON_TEXT_COLOR = (255, 255, 255)


class Grid:
    def __init__(self, rows, width):
        self.rows = rows
        self.width = width
        self.grid = self.set_grid()
        self.reset_button_rect = pygame.Rect(width - 100, 10, 90, 30)
        self.start = None
        self.end = None
        self.drawing = False

    def set_grid(self):
        grid = []
        gap = self.width // self.rows
        for row in range(self.rows):
            grid.append([])
            for column in range(self.rows):
                node = Node(row, column, gap, self.rows)
                grid[row].append(node)
        return grid

    def draw_grid(self, window):
        gap = self.width // self.rows
        for row in range(self.rows):
            pygame.draw.line(window, GRID_COLOR, (0, row * gap), (self.width, row * gap))
            for column in range(self.rows):
                pygame.draw.line(window, GRID_COLOR, (row * gap, 0), (row * gap, self.width))

    def draw(self, window):
        window.fill(BACKGROUND_COLOR)
        for row in self.grid:
            for node in row:
                node.draw(window)
        self.draw_grid(window)
        self.draw_reset_button(window)
        pygame.display.update()

    def draw_reset_button(self, window):
        pygame.draw.rect(window, BUTTON_COLOR, self.reset_button_rect)
        font = pygame.font.SysFont(None, 24)
        text = font.render("Reset", True, BUTTON_TEXT_COLOR)
        window.blit(text, (self.reset_button_rect.x + 10, self.reset_button_rect.y + 5))

    def get_clicked_position(self, position):
        gap = self.width // self.rows
        y, x = position
        row = y // gap
        column = x // gap
        return row, column

    def reset(self):
        for row in self.grid:
            for node in row:
                node.reset()
        self.start = None
        self.end = None

    def reset_button_clicked(self, position):
        return self.reset_button_rect.collidepoint(position)

    def handle_mouse_events(self, event):
        position = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.reset_button_clicked(position):
                self.reset()
                return

            if pygame.mouse.get_pressed()[0]:  # Left click
                if self.is_within_bounds(position):
                    row, column = self.get_clicked_position(position)
                    node = self.grid[row][column]
                    if not self.start and node != self.end:
                        self.start = node
                        self.start.set_start()
                    elif not self.end and node != self.start:
                        self.end = node
                        self.end.set_end()
                    elif node != self.end and node != self.start:
                        node.set_barrier()
                    self.drawing = True

            elif pygame.mouse.get_pressed()[2]:  # Right click
                if self.is_within_bounds(position):
                    row, column = self.get_clicked_position(position)
                    node = self.grid[row][column]
                    if node.is_barrier():
                        node.reset()

        elif event.type == pygame.MOUSEBUTTONUP:
            self.drawing = False

        elif event.type == pygame.MOUSEMOTION:
            if self.drawing and pygame.mouse.get_pressed()[0]:  # Left click and dragging
                if self.is_within_bounds(position):
                    row, column = self.get_clicked_position(position)
                    node = self.grid[row][column]
                    if not self.start and node != self.end:
                        self.start = node
                        self.start.set_start()
                    elif not self.end and node != self.start:
                        self.end = node
                        self.end.set_end()
                    elif node != self.end and node != self.start:
                        node.set_barrier()

    def is_within_bounds(self, position):
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.width
