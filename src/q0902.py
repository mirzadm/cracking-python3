"""Find a path from (0, 0) to (x, y)."""


def find_path(src_x, src_y, dest_x, dest_y, matrix):
    if src_x > dest_x or src_y > dest_y:
        return None

    if (src_x, src_y) == (dest_x, dest_y):
        return [(dest_x, dest_y)]

    if src_x < dest_x:
        if matrix[src_x + 1][src_y] != -1:
            p = find_path(src_x + 1, src_y, dest_x, dest_y, matrix)
            if p is not None:
                return [(src_x, src_y)] + p

    if src_y < dest_y:
        if matrix[src_x][src_y + 1] != -1:
            p = find_path(src_x, src_y + 1, dest_x, dest_y, matrix)
            if p is not None:
                return [(src_x, src_y)] + p

    return None



def test():
    matrix = [[0, -1, -1], [0, 0, 0]]
    print(find_path(0, 0, 0, 0, matrix))
    print(find_path(0, 0, 0, 1, matrix))
    print(find_path(0, 0, 1, 0, matrix))
    print(find_path(0, 0, 1, 1, matrix))
    print(find_path(0, 0, 1, 2, matrix))


if __name__ == '__main__':
    test()
