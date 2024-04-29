'''
Implement a Matrix class that describes a two-dimensional matrix. When instantiated, the class must take three
arguments in the following order:
rows — number of rows in the matrix
cols — number of columns in the matrix
value — initial value for matrix elements, default value is 0

An instance of the Matrix class must have two attributes:
rows — number of rows in the matrix
cols — number of columns in the matrix

The Matrix class must have two instance methods:
get_value() - a method that takes row and column col as arguments and returns a matrix element with row row and column col
set_value() - a method that takes a row row, a col column and a value as arguments and sets the value of a matrix
element with a row row and a col column as the value

An instance of the Matrix class must have the following formal string representation:
Matrix(<number of rows in the matrix>, <number of columns in the matrix>)
An informal string representation would be a string that lists all the elements of the matrix. Matrix row elements
must be separated by a space, matrix rows must be separated by the line break character \n.
For example, for a Matrix(2, 3) object, the informal string representation would be the string 0 0 0\n0 0 0,
which would be output as follows:
0 0 0
0 0 0

Also, an instance of the Matrix class must support the unary operators +, - and ~: the result of a unary + must be a
new instance of the Matrix class with the original number of rows and columns and with the original elements
the result of unary - should be a new instance of the Matrix class with the original number of rows and columns and
with elements taken with the opposite sign the result of a unary ~ should be a new instance of the Matrix
class representing the transposed matrix
Finally, passing an instance of the Matrix class to the round() function should return a new instance of the Matrix
class with the original number of rows and columns and with the elements rounded using the round() function.
When passed to the round() function, it must be possible to specify an integer as a second optional argument
that specifies the number of decimal places for rounding.
'''

class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self.value = [[value] * cols for _ in range(rows)]

    def get_value(self, row, col):
        return self.value[row][col]

    def set_value(self, row, col, val):
        self.value[row][col] = val

    def copy(self, func=lambda x: x, transponse=False):
        if transponse:
            matrix = Matrix(self.cols, self.rows)
        else:
            matrix = Matrix(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                value = func(self.get_value(row, col))
                if transponse:
                    matrix.set_value(col, row, value)
                else:
                    matrix.set_value(row, col, value)
        return matrix

    def __repr__(self):
        return f"Matrix({self.rows}, {self.cols})"

    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.value)

    def __pos__(self):
        return self.copy()

    def __neg__(self):
        return self.copy(func=lambda x: -x)

    def __invert__(self):
        return self.copy(transponse=True)

    def __round__(self, n=0):
        return self.copy(func=lambda x: round(x, n))

# Example:
matrix = Matrix(2, 3, 1)

print(+matrix)
print()
print(-matrix)

# Output:
# 1 1 1
# 1 1 1
#
# -1 -1 -1
# -1 -1 -1
