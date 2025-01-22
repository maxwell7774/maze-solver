from line import Line
from point import Point
from window import Window


def main():
    win = Window(800, 600)
    line_1 = Line(Point(20, 20), Point(100, 100))
    line_2 = Line(Point(40, 140), Point(100, 100))
    win.draw_line(line_1, "black")
    win.draw_line(line_2, "red")
    win.wait_for_close()


if __name__ == "__main__":
    main()
