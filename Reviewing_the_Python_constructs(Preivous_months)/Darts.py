'''
Let us assume that the darts playing field is a square matrix filled with natural numbers, arranged in ascending
order from the edges to the center. The side of the playing field will be the side of the square matrix
that this field represents.

Write a program that creates a dart board of a certain size.

Input format
The program is given a single natural number as input—the side of the playing field.

Output format
The program must create and display a playing field with a given side.
'''

def generate_pattern_matrix(n):
    matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i, n - i):
            matrix[i][j] = matrix[n - i - 1][j] = matrix[j][i] = matrix[j][n - i - 1] = i + 1

    return matrix

n = int(input())
pattern_matrix = generate_pattern_matrix(n)

for row in pattern_matrix:
    print(" ".join(map(str, row)))

# Example
# Input
# 5

# Output:
# 1 1 1 1 1
# 1 2 2 2 1
# 1 2 3 2 1
# 1 2 2 2 1
# 1 1 1 1 1