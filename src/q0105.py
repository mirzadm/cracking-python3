"""Chapter 1: Question 5:

Implement a method to perform basic string compression using the counts
of repeated characters. 

Examples:
abc         --> a1b1c1      return:     abc
aabcccccaaa --> a2b1c5a3    return:     a2b1c5a3
"""


def compress_string_with_counts(s):
    n = len(s)
    compressed = ''
    if not s:
        return compressed

    current_char = s[0]
    count = 1
    for i in range(1, n):
        if s[i] == current_char:
            count += 1
        else:
            compressed += current_char
            compressed += str(count)
            current_char = s[i]
            count = 1
    # Append the last char and count
    compressed += current_char
    compressed += str(count)

    if len(compressed) < n:
        return compressed
    else:
        return s
