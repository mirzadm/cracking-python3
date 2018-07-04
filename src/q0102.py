"""Chapter 1: Question 2.

Reverse a string.
"""


def reverse(s):
    n = len(s)
    rev_s = ''

    for i in range(n - 1, -1, -1):
        rev_s += s[i]

    return rev_s


def reverse_shortcut(s):
    return s[::-1]
