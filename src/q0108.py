"""Are two strings rotations of one another?"""


def is_rotation_slicing(s1, s2):
    n = len(s1)
    if n != len(s2):
        return False
    
    for i in range(0, n):
        if s1[i:n] + s1[0:i] == s2:
            return True

    return False


def is_rotation_substring(s1, s2):
    n = len(s1)
    if n != len(s2):
        return False

    s = s1 + s1
    return s2 in s


# print(is_rotation_slicing('happy', 'ppyha'))

