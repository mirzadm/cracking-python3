""" Determine if a string has all unique characters. """


# Use dictionary
def is_all_unique_dict(str):
    count = {}

    for ch in str:
        count[ch] = 0

    for ch in str:
        count[ch] += 1
        if count[ch] > 1:
            return False

    return True


# Use sets
def is_all_unique_set(str):
    str_set = set()

    for ch in str:
        if ch in str_set:
            return False
        else:
            str_set |= {ch}

    return True


# Use in operand in strings. More time instead of more space.
def is_all_unique_str(str):
    for i in range(len(str)):
        if str[i] in str[i+1:]:
            return False

    return True
