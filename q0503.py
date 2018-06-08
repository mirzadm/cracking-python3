"""Find the next smallest and biggest integers with same number of 1 bits."""


def find_next_same_bits(n):
    k = 0
    m = abs(n)
    seq01 = None
    seq10 = None
    while m > 0 and (seq01 is None or seq10 is None):
        right = m & 1
        next = m & 2
        if seq10 is None:
            if next != 0 and right == 0:
                seq10 = k

        if seq01 is None:
            if next == 0 and right != 0:
                seq01 = k

        k += 1
        m = m >> 1
        
    next_big = None
    next_small = None
    if seq10 is not None:
        next_big = abs(n) ^ (0b11 << seq10)
    if seq01 is not None:
        next_small = abs(n) ^ (0b11 << seq01)

    if n > 0: 
        return (next_big, next_small)
    else:
        return (-next_small, -next_big)


def test():
    n = -0b10
    next_biggest, next_smallest = find_next_same_bits(n)

    print('n: {0:b}'.format(n))
 
    if next_biggest is not None:
        print('next biggest: {0:b}'.format(next_biggest))

    if next_smallest is not None:
        print('next smallest: {0:b}'.format(next_smallest))


if __name__ == '__main__':
    test()
