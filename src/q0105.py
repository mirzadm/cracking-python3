"""Compress string."""


def str_compress(s):
    n = len(s)
    s_compressed = ''
    
    current_char = s[0]
    count = 1
    for i in range(1, n):
        if s[i] == current_char:
            count += 1
        else:
            s_compressed += current_char
            s_compressed += str(count)
            # update char and count
            current_char = s[i]
            count = 1
    # Append the last char and count
    s_compressed += current_char
    s_compressed += str(count)

    if len(s_compressed) < n:
        return s_compressed
    else:
        return s


# print(str_compress('aaaaaabcde'))