"""Chapter 1: Question 4.

Write a method to replace all spaces in a string with'%20'.
"""


def replace_spaces(s):
    """Creates a new copy to replace spaces."""
    c = '%20'
    t = ''
    for ch in s:
        if ch == ' ':
            t += c
        else:
            t += ch
    return t


def replace_spaces_list(s):
    """In-place replacement using a list."""
    n = len(s)
    if n == 0:
        return s

    s_list = list(s)
    old = ' '
    new = list('%20')

    i = 0
    while i < n:
        if s_list[i] == old:
            # Shift right two characters
            s_list.extend(['', ''])
            for j in range(n-1, i, -1):
                s_list[j+2] = s_list[j]

            s_list[i: i+3] = new
            i += 3
            n += 2
        else:
            i += 1

    return ''.join(s_list)
