'''
In this task, you need to implement a field for playing Minesweeper in the form of two classes Game and Cell.
An instance of the first class will describe the playing field itself, an instance of the Cell class will describe
one of its cells. An instance of the Game class must be created based on three values: the number of rows (field length),
the number of columns (field width) and the total number of mines on the field:

game = Game(14, 18, 40) # 14 rows, 18 columns and 40 minutes
The number of rows and columns, as well as the total number of mines, should be available under the corresponding attributes:

print(game.rows) #14
print(game.cols) #18
print(game.mines) #40
Also, an instance of the Game class must have a board attribute that represents the playing field as a two-dimensional
list. The number of sublists in this list must match the number of rows, and the number of elements in the sublists must
match the number of columns. Each sublist element must be an instance of the Cell class and have the appropriate set
of attributes:

cell = game.board[0][0]

print(cell.row) #0; cell string
print(cell.col) #0; cell column
print(cell.mine) # True or False depending on whether the cell contains a mine or not
print(cell.neighbors) # number from 0 to 8, number of mines in neighboring cells
When created, the playing field should be filled with mines randomly.
'''

import random

class Cell:
    def __init__(self, row, col, mine=False):
        self.row = row
        self.col = col
        self.mine = mine
        self.neighbours = 0

class Game:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = self.create_board()

    def create_board(self):
        board = [[Cell(row, col) for col in range(self.cols)] for row in range(self.rows)]
        self.place_mines(board)
        self.count_neighbours(board)
        return board

    def place_mines(self, board):
        mines_to_place = self.mines
        while mines_to_place > 0:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if not board[row][col].mine:
                board[row][col].mine = True
                mines_to_place -= 1

    def count_neighbours(self, board):
        for row in range(self.rows):
            for col in range(self.cols):
                cell = board[row][col]
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if (dr != 0 or dc != 0) and 0 <= row + dr < self.rows and 0 <= col + dc < self.cols:
                            cell.neighbours += board[row + dr][col + dc].mine

# Example
game = Game(14, 18, 40)
print(game.rows)
print(game.cols)
print(game.mines)

cell = game.board[0][0]

print(cell.row)
print(cell.col)
print(0 <= cell.neighbours <= 3)

# Output:
# 14
# 18
# 40
# 0
# 0
# True