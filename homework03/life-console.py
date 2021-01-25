import curses
import pygame
import argparse

from pathlib import Path
from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """ Отобразить рамку. """
        screen.border()

    def draw_grid(self, screen) -> None:
        """ Отобразить состояние клеток. """
        for numcol, col in enumerate(self.life.curr_generation):
            for numrow, row in enumerate(col):
                if row == 1:
                    screen.addstr(numcol + 1, numrow + 1, "*")
                else:
                    screen.addstr(numcol + 1, numrow + 1, " ")

    def run(self) -> None:
        screen = curses.initscr()
        screen = curses.newwin(self.life.rows + 2, self.life.cols + 2, 0, 0)
        curses.noecho()
        screen.nodelay(True)
        curses.curs_set(0)
        running = True
        is_paused = False
        while running:
            if (self.life.is_changing == False or self.life.is_max_generations_exceeded == True):
                running = False
            button = screen.getch()
            if button == ord("q"):
                running = False
            elif button == ord(" "):
                is_paused = True if not is_paused else False
            elif button == ord("s"):
                self.life.save(Path("save.txt"))
            if is_paused == False:
                curses.delay_output(30)
                self.draw_grid(screen)
                self.life.step()
                self.draw_borders(screen)
        curses.endwin()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GameOfLife")
    parser.add_argument("--rows", type=int, default=10, help="Number of rows in grid")
    parser.add_argument(
        "--cols", type=int, default=30, help="Number of columns in grid"
    )
    parser.add_argument(
        "--generations", type=int, default=100, help="Number of generations"
    )
    arguments = parser.parse_args()
    game = Console(
        life=GameOfLife((arguments.rows, arguments.cols), True, arguments.generations)
    )
    game.run()
