"""Chapter 1: Question 8.

Check if string 1 is a rotation of string 2.
"""


def is_rotation_slicing(s1, s2):
    """Uses slicing."""
    if not s1:
        return False

    n = len(s1)
    if n != len(s2):
        return False

    for i in range(n):
        if s1[i:n] + s1[0:i] == s2:
            return True

    return False


def is_rotation_substring(s1, s2):
    """Uses substring method."""
    if not s1:
        return False

    n = len(s1)
    if n != len(s2):
        return False

    s = s1 + s1
    return s2 in s
