import pygame
from Board import *
import socket
import threading


def create_thread(my_target):
    thread = threading.Thread(target=my_target)
    thread.daemon = True        # kill thread when main program quits
    thread.start()


host = '192.168.0.103'
port = 65432
connection_established = False
conn = None
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind((host, port))
my_socket.listen(1)


def receive_data():
    global turn
    while True:
        recv_data = str(conn.recv(1024).decode()).split("-")
        x, y = int(recv_data[0]), int(recv_data[1])
        if recv_data[2] == 'yourturn':
            turn = True
        if grid.get_cell_value(x, y == '-'):
            grid.set_cell_value(x, y, '0')

def waiting_for_connection():
    global connection_established, conn
    conn, address = my_socket.accept()        # wait for a connection
    print("Client is Connected")
    connection_established = True
    receive_data()


create_thread(waiting_for_connection)
surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Tic Tac Toe")

grid = Grid()
running = True
player = 'x'
turn = True
playing = 'True'

while running:
    surface.fill((0, 0, 0))     # black
    win = False
    grid.draw(surface)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and connection_established:
            if pygame.mouse.get_pressed()[0]:       # left click
                if turn and not grid.is_game_over():
                    pos = pygame.mouse.get_pos()
                    x = pos[0]//200
                    y = pos[1]//200
                    grid.on_click(x, y, player)
                    data = "{}-{}-{}".format(x, y, 'yourturn').encode()
                    conn.send(bytes(data))
                    turn = False
    running = grid.checkWin(surface, player)
    pygame.display.flip()       # Update the full display Surface to the scree
