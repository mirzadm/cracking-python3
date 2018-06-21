"""Zero-fill rows and cols having at least one zero."""


def zero_matrix(matrix, n, m):

    zero_rows = set()
    zero_cols = set()

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                zero_rows |= {i}
                zero_cols |= {j}

    for row in zero_rows:
        matrix[row] = [0] * m

    for col in zero_cols:
        for row in range(n):
            matrix[row][col] = 0

    return matrix


matrix = [[1, 0, 2], [3, 0, 4], [5, 6, 7]]

print(zero_matrix(matrix, 3, 3))