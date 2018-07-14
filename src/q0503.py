"""Chapter 5: Question 3.

Find the next smallest and biggest integers with same number of 1 bits.
Solution given for next biggest. Next smallest follows the same logic.
"""


def find_next_biggest_with_same_1s(n):
    """Finds the next biggest number with the same number of 1 bits.

    - Flips the rightmost 0 that has ones on its right (increases the value)
    - Rearrange 1s on its right to lowest positions and flips highest of them
      (decreases the value and creates same number of 1s)

    Example:
    xxxx_0_111_0000 --> xxxx_1_111_0000 --> xxxx_1_000_0011

    Args:
        n: A positive integer.
    Raises:
        ValueError on non-positive input.
    Returns:
        Next biggest number with same number of 1s.
    """

    if n <= 0:
        raise ValueError('Input argument has to be positive.')

    temp = n

    # Count number rightmost 0s 
    num_of_zeros = 0
    while temp & 1 == 0:
        temp >>= 1
        num_of_zeros += 1

    # Count number of 1s to the left of 0s
    num_of_ones = 0
    while temp & 1 == 1:
        temp >>= 1
        num_of_ones += 1

    # Flip next 0 to 1
    n = n ^ (1 << (num_of_ones + num_of_zeros))

    # Create a 0...01...1 mask, then invert it to get 1...10...0
    mask = ~((1 << (num_of_ones + num_of_zeros)) - 1)
    n = n & mask

    # Create a 0...01...1 mask with number of 1s = (num_of_ones - 1)
    mask = (1 << (num_of_ones - 1)) - 1
    n = n | mask

    return n
