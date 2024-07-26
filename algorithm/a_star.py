import pygame
from queue import PriorityQueue

def heuristic(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)

def a_star(draw_function, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    previous = {}

    g_score = {node: float("inf") for row in grid.grid for node in row}
    g_score[start] = 0
    cost = {node: float("inf") for row in grid.grid for node in row}
    cost[start] = heuristic(start.get_position(), end.get_position())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            while current in previous:
                current = previous[current]
                current.set_path()
                draw_function()
            end.set_end()
            return True

        for neighbor in current.neighbours:
            temporary_g_score = g_score[current] + 1

            if temporary_g_score < g_score[neighbor]:
                previous[neighbor] = current
                g_score[neighbor] = temporary_g_score
                cost[neighbor] = temporary_g_score + heuristic(neighbor.get_position(), end.get_position())

                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((cost[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.set_opened()

        draw_function()

        if current != start:
            current.set_closed()

    return False
