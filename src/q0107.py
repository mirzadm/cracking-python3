"""Chapter 1: Question 7.

In a given matrix, set every row and column with at least one 0 to all 0s.
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
