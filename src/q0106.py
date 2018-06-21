"""90 degree rotation of a pixel matrix."""


def rotate_matrix(matrix, n):
    rotated = [[0]*n for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            rotated[row][col] = matrix[n-1-col][row]
    
    return rotated


# Rotate in-place.
def rotate_matrix_inplace(matrix, n):
    for j in range(n-1):
        row = 0
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



#   1   2   3
#   4   5   6
#   7   8   9
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate_matrix_inplace(matrix, 3))