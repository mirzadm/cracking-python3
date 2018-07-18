"""Chapter 9: Question 2.

Starting from upper left corner of a grid, moving only right or down, 
find a path from (0, 0) to (x, y).
With one condition: Some points on the grid are blocked and paths cannot use
them.
"""


def find_path(src_x, src_y, dest_x, dest_y, blocked_points, no_path_to_dest):
    """Finds a path on the grid from source to destination.

    Args:
        src_x, src_y: Source coordinates. Integer >= 0.
        dest_x, dest_y: Destination coordinates. Integer >= 0.
        blocked_points: A set representing all block coordinates on the gridl
        no_path_to_dest: Set of points with no path to destination. 
                         Caller must provide and empty set as the argument.
    Returns:
        A list of point coordinates from source to destination if a path was
        found. None otherwise.
    """
    if src_x > dest_x or src_y > dest_y:
        return None

    if (src_x, src_y) == (dest_x, dest_y):
        return [(dest_x, dest_y)]

    if (src_x, src_y) in no_path_to_dest:
        return None

    if src_x < dest_x:
        if (src_x + 1, src_y) not in blocked_points:
            p = find_path(src_x + 1, src_y, dest_x, dest_y, blocked_points,
                          no_path_to_dest)
            if p is not None:
                return [(src_x, src_y)] + p

    if src_y < dest_y:
        if (src_x, src_y + 1) not in blocked_points:
            p = find_path(src_x, src_y + 1, dest_x, dest_y, blocked_points,
                          no_path_to_dest)
            if p is not None:
                return [(src_x, src_y)] + p
    
    no_path_to_dest.add((src_x, src_y))
    return None
