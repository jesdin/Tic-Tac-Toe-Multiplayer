import pygame
import os


letterX = pygame.image.load(os.path.join('Images', 'x.png'))
letter0 = pygame.image.load(os.path.join('Images', '0.png'))


class Grid:
    def __init__(self):
        self.gridLines = [((0, 200), (600, 200)), ((0, 400), (600, 400)),
                          ((200, 0), (200, 600)), ((400, 0), (400, 600))]
        self.grid = [['-' for x in range(3)] for y in range(3)]

    def draw(self, surface):
        for line in self.gridLines:
            pygame.draw.line(surface, (200, 200, 200), line[0], line[1], 2)
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.get_cell_value(x, y) == 'x':
                    surface.blit(letterX, (x*200, y*200))
                elif self.get_cell_value(x, y) == '0':
                    surface.blit(letter0, (x*200, y*200))

    def print_grid(self):
        for row in self.grid:
            print(row)

    def get_cell_value(self, x, y):
        return self.grid[y][x]

    def set_cell_value(self, x, y, value):
        self.grid[y][x] = value

    def on_click(self, x, y, player):
        if self.get_cell_value(x, y) == '-':
            if player == 'x':
                self.set_cell_value(x, y, 'x')
                player = '0'
            else:
                self.set_cell_value(x, y, '0')
                player = 'x'
        return player


g = Grid()
g.print_grid()
