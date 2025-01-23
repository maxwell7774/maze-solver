import time
import random

from cell import Cell
from window import Window


class Maze:

    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int | float,
        cell_size_y: int | float,
        win: Window | None = None,
        seed: int | None = None,
    ):
        self._x1: int = x1
        self._y1: int = y1
        self._num_rows: int = num_rows
        self._num_cols: int = num_cols
        self._cell_size_x: int | float = cell_size_x
        self._cell_size_y: int | float = cell_size_y
        self._cells_list: list[list[Cell]] = []
        self._win: Window | None = win
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(num_rows // 2, num_cols // 2)

    def _create_cells(self) -> None:
        for i in range(self._num_cols):
            self._cells_list.append([])
            for j in range(self._num_rows):
                cell = Cell(self._win)
                self._cells_list[i].append(cell)
                self._draw_cell(i, j)

    def _draw_cell(self, i: int, j: int) -> None:
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells_list[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self) -> None:
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.0005)

    def _break_entrance_and_exit(self) -> None:
        self._cells_list[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells_list[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i: int, j: int) -> None:
        self._cells_list[i][j].visited = True

        while(True):
            possible_directions: list[str] = []

            if i > 0 and not self._cells_list[i-1][j].visited:
                possible_directions.append("left")

            if j > 0 and not self._cells_list[i][j-1].visited:
                possible_directions.append("top")

            if i < self._num_cols - 1 and not self._cells_list[i+1][j].visited:
                possible_directions.append("right")

            if j < self._num_rows - 1 and not self._cells_list[i][j+1].visited:
                possible_directions.append("bottom")

            if len(possible_directions) == 0:
                self._draw_cell(i, j)
                return

            direction = random.randrange(0, len(possible_directions))

            if possible_directions[direction] == "left":
                self._cells_list[i][j].has_left_wall = False
                self._cells_list[i-1][j].has_right_wall = False
                self._break_walls_r(i-1, j)
            elif possible_directions[direction] == "top":
                self._cells_list[i][j].has_top_wall = False
                self._cells_list[i][j-1].has_bottom_wall = False
                self._break_walls_r(i, j-1)
            elif possible_directions[direction] == "right":
                self._cells_list[i][j].has_right_wall = False
                self._cells_list[i+1][j].has_left_wall = False
                self._break_walls_r(i+1, j)
            elif possible_directions[direction] == "bottom":
                self._cells_list[i][j].has_bottom_wall = False
                self._cells_list[i][j+1].has_top_wall = False
                self._break_walls_r(i, j+1)
