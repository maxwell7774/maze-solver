import time
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
        win: Window
    ):
        self._x1: int = x1
        self._y1: int = y1
        self._num_rows: int = num_rows
        self._num_cols: int = num_cols
        self._cell_size_x: int | float = cell_size_x
        self._cell_size_y: int | float = cell_size_y
        self._cells_list: list[list[Cell]] = []
        self._win: Window = win
        self._create_cells()

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
        time.sleep(0.025)
