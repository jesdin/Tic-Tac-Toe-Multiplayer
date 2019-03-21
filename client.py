import pygame
from Board import Grid
import socket
import threading


def create_thread(my_target):
    thread = threading.Thread(target=my_target)
    thread.daemon = True        # kill thread when main program quits
    thread.start()


host = '192.168.0.106'
port = 5432
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect((host, port))


def receive_data():
    global turn
    while True:
        data_recv = str(my_socket.recv(1024).decode()).split("-")
        x, y = int(data_recv[0]), int(data_recv[1])
        if data_recv[2] == 'yourturn':
            turn = True
        if data_recv[3] == 'False':
            grid.game_over = True
        if grid.get_cell_value(x, y == '-'):
            grid.set_cell_value(x, y, 'x')

create_thread(receive_data)
surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Tic Tac Toe")

grid = Grid()
running = True
player = '0'
turn = False
playing = 'True'

while running:
    surface.fill((0, 0, 0))     # black
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:       # left click
                if turn and not grid.is_game_over():
                    pos = pygame.mouse.get_pos()
                    x = pos[0]//200
                    y = pos[1]//200
                    grid.on_click(x, y, player)
                    win = grid.is_game_over()
                    if win:
                        playing = 'False'
                    data = "{}-{}-{}-{}".format(x, y, 'yourturn', playing).encode()
                    my_socket.send(bytes(data))
                    turn = False
    grid.draw(surface)
    if win:
        print(win)
        running = False
    pygame.display.flip()       # Update the full display Surface to the scree

