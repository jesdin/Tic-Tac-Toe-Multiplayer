import pygame
from Board import Grid
import socket
import threading


def create_thread(my_target):
    thread = threading.Thread(target=my_target)
    thread.daemon = True        # kill thread when main program quits
    thread.start()


host = '192.168.0.106'
port = 65432
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect((host, port))


def receive_data():
    pass


create_thread(receive_data())
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

