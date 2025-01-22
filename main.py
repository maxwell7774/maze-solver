from maze import Maze
from window import Window


def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - margin * 2) / num_cols
    cell_size_y = (screen_y - margin * 2) / num_rows

    win = Window(screen_x, screen_y)

    Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)

    win.wait_for_close()


if __name__ == "__main__":
    main()
