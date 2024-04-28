'''
Implement a Knight class that describes a chess knight. When instantiated, the class must take three arguments in the
following order:

horizontal — coordinate of the knight along the horizontal axis, represented by a Latin letter from a to h
vertical — coordinate of the knight along the vertical axis, represented by an integer from 1 to 8 inclusive
color — horse color (black or white)
An instance of the Knight class must have three attributes:

horizontal — coordinate of the knight on the chessboard along the horizontal axis
vertical — coordinate of the knight on the chessboard along the vertical axis
color — horse color
The Knight class must have four instance methods:

get_char() - method that returns the character N
can_move() - a method that takes as arguments the coordinates of a cell along the horizontal and vertical axes and
returns True if the knight can move to a cell with these coordinates, or False otherwise
move_to() is a method that takes the coordinates of a cell along the horizontal and vertical axes as arguments and
replaces the current coordinates of the knight with the transmitted ones. If a knight from the current square cannot
move to a square with the specified coordinates, its coordinates must remain unchanged draw_board() is a
method that prints a chess board, marking the knight on this board and the squares to which the knight can move.
Empty squares should be displayed with the symbol ., a knight with the symbol N, squares to which the knight
can move with the symbol *
'''


class Knight:
    def __init__(self, horizontal, vertical, color):
        self.color = color
        self.horizontal = horizontal
        self.vertical = vertical
        self.converter = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
        self.num = self.converter[self.horizontal]
        self.activate()

    def activate(self):
        self.vert = self.vertical - 1
        self.num = self.converter[self.horizontal]
        self.possmove = [*filter(lambda x: -1 < x[0] < 8 and -1 < x[1] < 8,
                                 [(self.num + 2, self.vert + 1), (self.num + 2, self.vert - 1),
                                  (self.num - 2, self.vert - 1), (self.num - 2, self.vert + 1),
                                  (self.num - 1, self.vert + 2), (self.num - 1, self.vert - 2),
                                  (self.num + 1, self.vert + 2), (self.num + 1, self.vert - 2)])]

    def get_char(self):
        return "N"

    def draw_board(self):
        self.lis = []
        for i in range(8):
            self.lis.append(["."] * 8)
        self.lis[self.vertical - 1][self.converter[self.horizontal]] = "N"
        for i, j in self.possmove:
            self.lis[j][i] = "*"
        for i in reversed(self.lis): print(*i, sep="")

    def move_to(self, hori, ver):
        if (self.converter[hori], ver - 1) in self.possmove:
            self.horizontal = hori
            self.vertical = ver
            self.activate()

    def can_move(self, hor, ver):
        if (self.converter[hor], ver - 1) in self.possmove:
            return True
        return False

# Example
knight = Knight('c', 3, 'white')

print(knight.horizontal, knight.vertical)
print(knight.can_move('e', 5))
print(knight.can_move('e', 4))

knight.move_to('e', 4)
print(knight.horizontal, knight.vertical)

# output
# c 3
# False
# True
# e 4
