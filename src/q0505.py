"""Chapter 5: Question 5.

Given two numbers, count number of bits that are not equal between them.
Example: 2 and 3 have one bit that is differnt between them.
"""


def count_unequal_bits(a, b):
    """Counts number of bits that are different between them a and b.

    Args:
        a, b: Non-negative integers.
    Returns:
        Number of bits different between a and b.
    Raises:
        ValueError: If either of the arguments is negative.
    """
    if a < 0 or b < 0:
        raise ValueError('Input arguments must be >= 0.')
    
    c = a ^ b
    count = 0
    while  c != 0:
        c = c & (c - 1)
        count += 1
    # A easier way to do is
        # if c & 1 == 1:
        #     count += 1
        # c = c >> 1
    return count
