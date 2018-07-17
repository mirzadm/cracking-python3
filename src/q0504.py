"""Chapter 5: Question 4.

A simple condition to check if a number is power of 2:    n & (n-1) == 0
Example:
    n = 1000
    1000 & (1000 - 1)) = 1000 & 0111 = 0000 = 0
"""


def is_power_of_two(n):
    """Checks if n is a power of 2.

    Args:
        n: Non-negative integer.
    """
    if n < 0:
        raise ValueError('Input argument must be >= 0.')
    
    return n & (n-1) == 0
