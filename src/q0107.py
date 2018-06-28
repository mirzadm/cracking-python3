"""Chapter 1: Question 7.

Write an algorithm such that if an element in an MxN matrix is 0,
its entire row and column are set to 0.
"""


def zero_fill_matrix(matrix, n, m):
    """Zero-fill matrix.
    
    In-place zero-fill.
    Args:
        matrix: 2-dim list.
        n: number of rows.
        m: number of columns.
    Returns:
        Zero-filled matrix
    """
    if not matrix:
        return matrix

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
