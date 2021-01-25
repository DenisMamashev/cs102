import pygame
from pygame.locals import *

from life import GameOfLife
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)
        self.cell_size = cell_size
        self.speed = speed
        self.screen = pygame.display.set_mode(
            (self.life.cols * self.cell_size, self.life.rows * self.cell_size)
        )

    def draw_lines(self) -> None:
        for x in range(0, self.cell_size * self.life.cols, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.cell_size * self.life.rows))
        for y in range(0, self.cell_size * self.life.rows, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.cell_size * self.life.cols, y))

    def draw_grid(self) -> None:
        for row in range(self.life.rows):
            for col in range(self.life.cols):
                if self.life.curr_generation[row][col] == 1:
                    pygame.draw.rect(self.screen,pygame.Color("green"),
                        (
                            self.cell_size * col + 1,
                            self.cell_size * row + 1,
                            self.cell_size - 1,
                            self.cell_size - 1,
                        ),
                    )
                else:
                    pygame.draw.rect(self.screen,pygame.Color("white"),
                        (
                            self.cell_size * col + 1,
                            self.cell_size * row + 1,
                            self.cell_size - 1,
                            self.cell_size - 1,
                        ),
                    )

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))
        running = True
        stop = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    stop = True
            self.draw_lines()
            if stop:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                        stop = False
                    elif event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        col = pos[0] // self.cell_size
                        row = pos[1] // self.cell_size
                        if self.life.curr_generation[row][col] == 1:
                            self.life.curr_generation[row][col] = 0
                        else:
                            self.life.curr_generation[row][col] = 1
                        self.draw_grid()
                        pygame.display.flip()
            else:
                self.life.step()
                self.draw_grid()
                pygame.display.flip()
                clock.tick(self.speed)
        pygame.quit()


if __name__ == "__main__":
    game = GUI(life=GameOfLife((24, 80), max_generations=50))
    game.run()
