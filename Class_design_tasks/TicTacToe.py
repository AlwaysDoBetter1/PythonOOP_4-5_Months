'''
Implement a TicTacToe class for playing Tic-Tac-Toe. An instance of the TicTacToe class should be a three-row,
three-column game board on which players can take turns marking empty squares. The first move is made by the player
placing crosses:

tictactoe = TicTacToe()

tictactoe.mark(1, 1) # mark the cell with coordinates (1; 1) with a cross
tictactoe.mark(3, 1) # mark the cell with coordinates (3, 1) with a zero
You cannot mark already marked cells. When you try to do this, the text Inaccessible cell should be displayed:

tictactoe.mark(1, 1) # Inaccessible cell

tictactoe.mark(1, 3) # mark the cell with coordinates (1; 3) with a cross
tictactoe.mark(1, 2) # mark the cell with coordinates (1; 2) with a zero
tictactoe.mark(3, 3) # mark the cell with coordinates (3; 3) with a cross
tictactoe.mark(2, 2) # mark the cell with coordinates (2; 2) with a zero
tictactoe.mark(2, 3) # mark the cell with coordinates (2; 3) with a cross
Using the winner() method it should be possible to find out the winner of the game. The method should return:

X symbol if the player placing crosses wins
O symbol if the player betting zeros wins
line Draw, if there is a draw
None if the winner has not yet been determined
print(tictactoe.winner()) # X
You cannot mark cells after finishing the game. When you try to do this, the text Game over should be displayed:

tictactoe.mark(2, 1) # Game over
Using the show() method it should be possible to view the current state of the playing field. It must be constructed
from the symbols | and -, as well as X and O if any moves were made by the players. For the tictactoe field above,
calling tictactoe.show() should output the following:

X|O|X
-----
 |O|X
-----
O| |X
'''

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner_symbol = None
        self.game_over = False

    def mark(self, row, col):
        if self.game_over:
            print("Game over")
            return

        if self.board[row - 1][col - 1] != ' ':
            print("Inaccessible cell")
            return

        self.board[row - 1][col - 1] = self.current_player

        if self.check_winner():
            self.game_over = True

        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        for row in self.board:
            if row.count(row[0]) == len(row) and row[0] != ' ':
                self.winner_symbol = row[0]
                return True

        for col in range(len(self.board)):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != ' ':
                self.winner_symbol = self.board[0][col]
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            self.winner_symbol = self.board[0][0]
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
            self.winner_symbol = self.board[0][2]
            return True

        if all([cell != ' ' for row in self.board for cell in row]):
            self.winner_symbol = 'Draw'
            return True

        return False

    def winner(self):
        if self.game_over:
            return self.winner_symbol
        else:
            return None

    def show(self):
        for row in range(3):
            print("|".join(self.board[row]))
            if row < 2:
                print("-" * 5)

# Example
tictactoe = TicTacToe()

tictactoe.mark(1, 1)
tictactoe.mark(3, 1)
tictactoe.mark(1, 1)

tictactoe.mark(1, 3)
tictactoe.mark(1, 2)
tictactoe.mark(3, 3)
tictactoe.mark(2, 2)
tictactoe.mark(2, 3)

print(tictactoe.winner())
tictactoe.mark(2, 1)
tictactoe.show()

# Inaccessible cell
# X
# Game over
# X|O|X
# -----
#   |O|X
# -----
# O| |X