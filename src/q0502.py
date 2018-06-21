"""Convert a real number in [0, 1] to binary in 32 bits."""


def to_binary(n):
    bit_array = []
    k = 0
    while n != 0 and k < 32:
        n *= 2
        if n >= 1:
            bit_array.append(1)
            n -= 1
        else:
            bit_array.append(0)

        k += 1

    if n == 0:
        return ('Accurate', bit_array)
    else:
        return ('Inaccurate', bit_array)


def test():
    for k in range(10, 91, 10):
        for i in range(10):
            n = (k + i) / 100
            print('Value: {}\t Representation: {}'.format(n, to_binary(n)))


if __name__ == '__main__':
    test()

