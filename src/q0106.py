"""90 degree rotation of a pixel matrix.

Rotates a pixel matrix 90 degress clockwise.
"""


def rotate_matrix_90_clk(matrix):
    """Creates a new rotated matrix.

    Deos not change the input matrix.
    Args:
        A square 2-dim matrix.
    Returns:
        Rotated matrix.
    """
    if not matrix:
        return []

    n = len(matrix)
    if n == 1:
        return [matrix[0]]

    rotated_matrix = [[0] * n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            rotated_matrix[col][n - 1 - row] = matrix[row][col]

    return rotated_matrix


def rotate_matrix__90_clk_inplace(matrix):
    """In-place rotation. Changes the input matrix.

    Args:
        A square 2-dim matrix.
    Returns:
        Rotated matrix (in-place)
    """
    n = len(matrix)
    if n <= 1:
        return matrix

    for i in range(n//2):
        for j in range(i, n - i - 1):
            row = i
            col = j
            current = matrix[row][col]
            for k in range(4):
                next_row = col
                next_col = n - 1 - row
                backup = matrix[next_row][next_col]
                matrix[next_row][next_col] = current
                row = next_row
                col = next_col
                current = backup

    return matrix
