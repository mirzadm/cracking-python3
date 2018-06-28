"""Chapter 1: Question 2.

Implement a function `void reverse(char* str)` in C or C++ which reverses
a null- terminated string.

The solution is pythonic. String is not null terminated.
"""


def reverse(s):
    n = len(s)
    rev_s = ''

    for i in range(n - 1, -1, -1):
        rev_s += s[i]

    return rev_s


def reverse_shortcut(s):
    return s[::-1]
