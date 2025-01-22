from cell import Cell
from window import Window


def main():
    win = Window(800, 600)
    cell = Cell(win)
    cell.has_left_wall = False
    cell.draw(10,10, 110, 110)
    cell = Cell(win)
    cell.has_top_wall = False
    cell.draw(125,125, 225, 225)
    cell = Cell(win)
    cell.has_right_wall = False
    cell.draw(230, 230, 325, 325)
    cell = Cell(win)
    cell.has_bottom_wall = False
    cell.draw(300, 300, 500, 500)
    win.wait_for_close()


if __name__ == "__main__":
    main()
