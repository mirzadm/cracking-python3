"""Replace spaces with %20."""


def replace_spaces(s):
    c = '%20'
    t = ''
    for ch in s:
        if ch == ' ':
            t += c
        else:
            t += ch
    return t


# Replace in-place. Uses in array instead of a string.
def replace_spaces_array(s, n):    
    c = '%20'
    i = 0
    m = n
    while i < m:
        if s[i] == ' ':
            # shift m to i+1 two to the right
            for j in range(m-1, i, -1):
                s[j+2] = s[j]
            # insert %20 at i, i+1, i+2
            s[i], s[i+1], s[i+2] = '%', '2', '0'
            # update i to i+3
            i += 3
            # update m to m+2  
            m += 2
        else:
            i += 1
    
    return s


# print(replace_spaces_array(list('abc'), 3))
# print(replace_spaces_array(list(' a bc    '), 5))

