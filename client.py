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
                player = grid.on_click(x, y, player)
                grid.print_grid()
                grid.is_game_over()
    grid.draw(surface)
    win = grid.is_game_over()
    if win:
        print(win)
        running = False
    pygame.display.flip()       # Update the full display Surface to the scree

