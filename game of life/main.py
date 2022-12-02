import pygame


class Board():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for i in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                pygame.draw.rect(screen, (255, 255, 255),
                                 pygame.Rect(self.left + self.cell_size * (j + 1), self.top + self.cell_size * (i + 1),
                                             self.cell_size, self.cell_size), 1)

    def on_click(self, cell):
        pass

    def get_cell(self, pos):
        def clamp(minn, maxx, value):
            return min(max(value, minn), maxx)
        return tuple([clamp(0, self.width, ((pos[0] - self.left) // self.cell_size)) - 1, clamp(0, self.height, ((pos[1] - self.top) // self.cell_size)) - 1])

    def get_click(self, pos):
        cell = self.get_cell(pos)
        print(self.get_cell(pos))
        self.on_click(cell)


class Life(Board):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.rules = {'B': '3', 'S': '23'}

    def on_click(self, cell):
        if self.board[cell[1]][cell[0]] == 0:
            self.board[cell[1]][cell[0]] = 1
        elif self.board[cell[1]][cell[0]] == 1:
            self.board[cell[1]][cell[0]] = 0

    def next_move(self):
        temp = [[j for j in i] for i in self.board]
        for x in range(self.width):
            for y in range(self.height):
                s = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            pass
                        else:
                            s += self.board[(i + y) % self.height][(j + x) % self.width]
                if self.board[y][x] == 0 and str(s) in self.rules['B']:
                    temp[y][x] = 1
                elif self.board[y][x] == 1 and str(s) not in self.rules['S']:
                    temp[y][x] = 0
        self.board = temp

                


    def render(self, screen):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 1:

                    pygame.draw.rect(screen, (255, 255, 255),
                                     pygame.Rect(self.left + self.cell_size * (j + 1), self.top + self.cell_size * (i + 1),
                                                 self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(screen, (255, 255, 255),
                                     pygame.Rect(self.left + self.cell_size * (j + 1), self.top + self.cell_size * (i + 1),
                                                 self.cell_size, self.cell_size), 1)

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Клетчатое поле')
    screen = pygame.display.set_mode((800, 600))
    board = Life(20, 15)
    running = True
    fps = 1
    k = 0
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                board.get_click(event.pos)
            if event.type == pygame.KEYUP:
                k = (k + 1) % 2 
            if event.type == pygame.MOUSEWHEEL:
                if event.y == -1:
                    fps -= 0.05
                elif event.y == 1:
                    fps += 0.01
                print(fps)
        screen.fill((0, 0, 0))
        board.render(screen)
        if k:
            board.next_move()
            clock.tick(fps)
        else:
            clock.tick(60)
        pygame.display.flip()
