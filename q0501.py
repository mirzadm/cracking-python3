"""Insert m in n, starting at j.
For i and j, value 0 represents the rightmost bit.
"""

def insert_bits(n, m, i, j):
    mask = 1 << j
    for k in range(i-j):
        mask |= mask << 1
    mask = ~mask
    n_masked = n & mask
    return n_masked | (m << j)
