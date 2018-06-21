"""Merge and sort two arrays into one."""

def sort_array_buf(a, b):
    if b == [] or a == []:
        return None
    
    i = len(a) - 1
    j = len(b) - 1
    k = i - j - 1
    
    if k < 0:
        return None

    while i >= 0 and j >= 0 and k >= 0:
        if a[k] >= b[j]:
            a[i] = a[k]
            k -= 1
        else:
            a[i] = b[j]
            j -= 1
        i -= 1
    
    if i >= 0:
        if j >= 0:
            a[0:i+1] = b[0:j+1]
    
    return a
