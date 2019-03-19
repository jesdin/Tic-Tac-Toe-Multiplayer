import pygame
from Board import Grid

surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Tic Tac Toe")

grid = Grid()
running = True

while running:
    surface.fill((0, 0, 0))     # black
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    grid.draw(surface)
    pygame.display.flip()       # Update the full display Surface to the scree

