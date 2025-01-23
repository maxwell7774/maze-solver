from maze import Maze
from window import Window


def main():
    num_rows: int = 12 
    num_cols: int = 16
    margin: int = 50
    screen_x: int = 800
    screen_y: int = 600
    cell_size_x: float = (screen_x - margin * 2) / num_cols
    cell_size_y: float = (screen_y - margin * 2) / num_rows

    win: Window = Window(screen_x, screen_y)

    Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)

    win.wait_for_close()


if __name__ == "__main__":
    main()
