"""Chapter 5: Question 1.

Given numbers m and n, insert m in n starting at bit i and ending at bit j. 
Assume we only care about j-i+1 first bits of m.
"""

def insert_bits_in_num(m, n, i, j):
    # Build a mask with all zeros except all ones from i to j
    # Example: i = 2, j = 4, mask = 0b0001_1100 
    # 0b0000_0001 << 3
    # 0b0000_1000 - 1
    # 0b0000_0111 << 2
    # 0b0001_1100
    mask = 1 << (j-i+1) 
    mask -= 1
    mask <<= i
    m <<= i
    m_cleared = m & mask  # Just to sure bits to the left of bit j are zeros 
    mask = ~mask # Create the mask for n
    n_cleared = n & mask
    return m_cleared | n_cleared
