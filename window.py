from tkinter import Tk, BOTH, Canvas

from constants import BACKGROUND_COLOR, FOREGROUND_COLOR
from line import Line


class Window:

    def __init__(self, width: int, height: int) -> None:
        self.__root: Tk = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas: Canvas = Canvas(width=width, height=height, bg=BACKGROUND_COLOR)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running: bool = False
        

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self) -> None:
        self.__running = False

    def draw_line(self, line: Line, fill_color: str=FOREGROUND_COLOR) -> None:
        line.draw(self.__canvas, fill_color)

