"""Chapter 9: Problem 1.

How many ways to run up n stairs. If you could hop 1, 2, or 3 steps.
"""


def run_up_stairs_rec(n):
    """Counts number of ways to run up stairs.
    
    Inefficient solution with O(3^n) time.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    return run_up_stairs_rec(n-1) + run_up_stairs_rec(n-2) + run_up_stairs_rec(n-3)


def run_up_stairs_iter(n):
    """Counts number of ways to run up stairs.
    
    More efficient solution with O(n) time.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    k_1 = 4
    k_2 = 2
    k_3 = 1
    i = 4
    while i <= n:
        ith_sum = k_1 + k_2 + k_3
        k_3 = k_2
        k_2 = k_1
        k_1 = ith_sum
        i += 1

    return ith_sum
