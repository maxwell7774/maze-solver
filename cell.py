from constants import BACKGROUND_COLOR
from window import Window
from point import Point
from line import Line


class Cell:

    def __init__(self, win: Window | None = None) -> None:
        self.has_left_wall: bool = True
        self.has_right_wall: bool = True
        self.has_top_wall: bool = True
        self.has_bottom_wall: bool = True
        self.visited: bool = False
        self._x1: int | None = None
        self._x2: int | None = None
        self._y1: int | None = None
        self._y2: int | None = None
        self._win: Window | None = win

    def draw(self, x1, y1, x2, y2) -> None:
        if self._win == None:
            return

        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        left_wall = Line(Point(x1, y1), Point(x1, y2))
        top_wall = Line(Point(x1, y1), Point(x2, y1))
        right_wall = Line(Point(x2, y1), Point(x2, y2))
        bottom_wall = Line(Point(x1, y2), Point(x2, y2))

        if self.has_left_wall:
            self._win.draw_line(left_wall)
        else:
            self._win.draw_line(left_wall, BACKGROUND_COLOR)

        if self.has_top_wall:
            self._win.draw_line(top_wall)
        else:
            self._win.draw_line(top_wall, BACKGROUND_COLOR)

        if self.has_right_wall:
            self._win.draw_line(right_wall)
        else:
            self._win.draw_line(right_wall, BACKGROUND_COLOR)

        if self.has_bottom_wall:
            self._win.draw_line(bottom_wall)
        else:
            self._win.draw_line(bottom_wall, BACKGROUND_COLOR)


    def draw_move(self, to_cell: 'Cell', undo: bool=False) -> None:
        if self._win == None:
            return
        if to_cell._x1 == None or to_cell._x2 == None or to_cell._y1 == None or to_cell._y2 == None:
            raise Exception("Cell must be drawn first")
        if self._x1 == None or self._x2 == None or self._y1 == None or self._y2 == None:
            raise Exception("Cell must be drawn first")

        half_length = abs(self._x2 - self._x1) // 2
        x_center = half_length + self._x1
        y_center = half_length + self._y1

        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = half_length2 + to_cell._x1
        y_center2 = half_length2 + to_cell._y1
        
        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self._win.draw_line(line, fill_color)

