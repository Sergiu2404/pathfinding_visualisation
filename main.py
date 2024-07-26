import pygame
from grid import Grid
from algorithm.a_star import a_star



WIDTH = 800
WINDOW = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Algorithm Visualization")

def main(window, width):
    pygame.font.init()  # Explicitly initialize the font module
    ROWS = 50
    grid = Grid(ROWS, width)
    run_condition = True
    started = False

    while run_condition:
        grid.draw(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_condition = False
                continue

            grid.handle_mouse_events(event)  # Handle mouse events

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    for row in grid.grid:
                        for node in row:
                            node.set_neighbors(grid.grid)

                    if grid.start and grid.end:
                        a_star(lambda: grid.draw(window), grid, grid.start, grid.end)
                        started = True

    pygame.quit()



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    main(WINDOW, WIDTH)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
