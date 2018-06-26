"""Determines if two strings are permutaitons of each other."""


def is_permutation_sort(s1, s2):
    """Uses sorting."""
    s1_list = list(s1)
    s2_list = list(s2)
    s1_list.sort()
    s2_list.sort()

    return s1_list == s2_list


def is_permutation_dict(s1, s2):
    """Uses a dictionary to store character counts."""
    n1 = len(s1)
    n2 = len(s2)

    if n1 != n2:
        return False

    if s1 == s2:
        return True

    ch_count = {}
    for ch in s1:
        if ch_count.get(ch, 0) == 0:
            ch_count[ch] = 1
        else:
            ch_count[ch] += 1

    for ch in s2:
        if ch_count.get(ch, 0) == 0:
            return False
        else:
            ch_count[ch] -= 1

    return True
