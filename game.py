import pygame
from Board import Grid

surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Tic Tac Toe")

grid = Grid()
running = True
player = 'x'

while running:
    surface.fill((0, 0, 0))     # black
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:       # left click
                pos = pygame.mouse.get_pos()
                x = pos[0]//200
                y = pos[1]//200
                grid.set_cell_value(x, y, player)
                if player == 'x':
                    player = '0'
                else:
                    player = 'x'
                grid.print_grid()
    grid.draw(surface)
    pygame.display.flip()       # Update the full display Surface to the scree

