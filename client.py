import pygame
from Board import Grid
import socket
import threading


def create_thread(my_target):
    thread = threading.Thread(target=my_target)
    thread.daemon = True        # kill thread when main program quits
    thread.start()


host = '192.168.0.103'
port = 65432
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect((host, port))


def receive_data():
    global turn
    while True:
        data_recv = str(my_socket.recv(1024).decode()).split("-")
        x, y = int(data_recv[0]), int(data_recv[1])
        if data_recv[2] == 'yourturn':
            turn = True
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
    win = False
    surface.fill((0, 0, 0))     # black
    grid.draw(surface)
    if not turn:
        font = pygame.font.Font('freesansbold.ttf', 15)
        text = font.render("waiting for player 1", True, (0, 255, 255))
        surface.blit(text, (15, 600-25))
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
                    data = "{}-{}-{}".format(x, y, 'yourturn').encode()
                    my_socket.send(bytes(data))
                    turn = False
    running = grid.checkWin(surface, player)
    pygame.display.flip()       # Update the full display Surface to the scree
    