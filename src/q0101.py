"""Chapter 1: Question 1.

Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""


def is_all_unique_dict(s):
    """Uses dictionary."""
    count = {}

    for ch in s:
        count[ch] = 0

    for ch in s:
        count[ch] += 1
        if count[ch] > 1:
            return False

    return True


def is_all_unique_set(s):
    """Uses set."""
    str_set = set()

    for ch in s:
        if ch in str_set:
            return False
        else:
            str_set |= {ch}

    return True


def is_all_unique_str(s):
    """Uses no extra space at the expense of time."""
    for i in range(len(s)):
        if s[i] in s[i+1 :]:
            return False

    return True
