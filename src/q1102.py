"""Sort an array by anagram."""

def sort_by_anagram(array):
    
    n = len(array)
    if n <= 2:
        return array
    i = 0
    while i < n-2:
        for j in range(i+1, n):
            if is_anagram(array[i], array[j]):
                i += 1
                array[i], array[j] = array[j], array[i]
        i += 1
    
    return array


def is_anagram(s, t):
    if len(s) != len(t):
        return False

    s_array = list(s.lower())
    t_array = list(t.lower())
    s_array.sort()
    t_array.sort()
    
    return s_array == t_array
