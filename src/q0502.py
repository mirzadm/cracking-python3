"""Chapter 5: Problem 2.

Convert a real number  0 <= n <=1 to binary in 32 bits.
Return 'Error' if 32-bit length is not enough.
"""


def fraction_to_binary_digits(n):
    if n <= 0 or n >= 1:
        return 'Error'
    binary_digits = []
    k = 0
    while n > 0 and k < 32:
        n *= 2
        if n >= 1:
            binary_digits.append(1)
            n -= 1
        else:
            binary_digits.append(0)
        k += 1

    if n == 0:
        return binary_digits
    else:
        return 'Error'
