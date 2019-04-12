import pygame
import os


letterX = pygame.image.load(os.path.join('Images', 'x.png'))
letter0 = pygame.image.load(os.path.join('Images', '0.png'))


class Grid:
    def __init__(self):
        pygame.init()
        self.gridLines = [((0, 200), (600, 200)), ((0, 400), (600, 400)),
                          ((200, 0), (200, 600)), ((400, 0), (400, 600))]
        self.grid = [['-' for x in range(3)] for y in range(3)]
        self.game_over = False

    def draw(self, surface):
        for line in self.gridLines:
            pygame.draw.line(surface, (200, 200, 200), line[0], line[1], 5)
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.get_cell_value(x, y) == 'x':
                    surface.blit(letterX, (x*200+10, y*200+10))
                elif self.get_cell_value(x, y) == '0':
                    surface.blit(letter0, (x*200+10, y*200+10))

    def print_grid(self):
        for row in self.grid:
            print(row)

    def get_cell_value(self, x, y):
        return self.grid[y][x]

    def set_cell_value(self, x, y, value):
        self.grid[y][x] = value

    def on_click(self, x, y, player):
        if self.get_cell_value(x, y) == '-':
            self.set_cell_value(x, y, player)
        return player

    def is_game_over(self):
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2]:
                if self.grid[i][0] == 'x':
                    self.game_over = True
                    return 'x'
                elif self.grid[i][0] == '0':
                    self.game_over = True
                    return '0'
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i]:
                if self.grid[0][i] == 'x':
                    self.game_over = True
                    return 'x'
                elif self.grid[0][i] == '0':
                    self.game_over = True
                    return '0'
        if self.grid[1][1] == self.grid[2][2] == self.grid[0][0]\
                or self.grid[0][2] == self.grid[1][1] == self.grid[2][0]:
            if self.grid[1][1] == 'x':
                self.game_over = True
                return 'x'
            elif self.grid[1][1] == '0':
                self.game_over = True
                return '0'
        c = True
        for i in range(3):
            if '-' in self.grid[i]:
                c = False
                break
        if c:
            self.game_over = True
            return "DRAW"
        return self.game_over

    def checkWin(self, surface, player):
        win = self.is_game_over()
        if win:
            if win == player:
                win = "You WIN"
            elif win != "DRAW":
                win = "You LOSE"
            surface.fill((0,0,0))   # black
            font = pygame.font.Font('freesansbold.ttf', 32)
            text_win = font.render(win, True, (255, 255, 255))
            font = pygame.font.Font('freesansbold.ttf', 25)
            text1 = font.render("Space to play again", True, (255, 255, 255))
            text2 = font.render("Escape to Exit", True, (255, 255, 255))
            win_rect = text_win.get_rect()
            text1_rect = text1.get_rect()
            text2_rect = text2.get_rect()
            win_rect.center = (600//2, 600/2-60)
            text1_rect.center = (600//2, 600/2+30)
            text2_rect.center = (600//2, 600/2+65)
            surface.blit(text_win, win_rect)
            surface.blit(text1, text1_rect)
            surface.blit(text2, text2_rect)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed()[pygame.K_SPACE]:
                        print("Space")
                        self.reInit()
                        return True
                    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                        return False 
        return True

    def reInit(self):
        for x in range(3):
            for y in range(3):
                self.grid[x][y] = '-'
        self.game_over = False
g = Grid()
g.print_grid()
