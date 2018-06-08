"""Number of ways to run up a staircase."""

def count_ways_rec(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    return count_ways_rec(n-1) + count_ways_rec(n-2) + count_ways_rec(n-3)


def count_ways_iter(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    p = [4, 2, 1]
    i = 4
    while i <= n:
        temp = p[0] + p[1] + p[2]
        p[2] = p[1]
        p[1] = p[0]
        p[0] = temp
        i += 1

    return p[0]


# n = 100 # too high for recursion
# print('Number of ways for {} stairs with iteration and recursion:')
# print(count_ways_iter(n))
