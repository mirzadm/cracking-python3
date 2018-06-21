"""Two strings are permutaitons of each other."""

def is_permutation_sort(s1, s2):

    s1_list = list(s1)
    s2_list = list(s2)
    s1_list.sort()
    s2_list.sort()

    return s1_list == s2_list
 

# Works for ascii-coded strings
def is_permutation_count(s1, s2):
    count1 = [0] * 256
    count2 = [0] * 256
    for ch in s1:
        count1[ord(ch)] += 1
    
    for ch in s2:
        count2[ord(ch)] += 1

    for i in range(256):
        if count1[i] != count2[i]:
            return False
    return True


# Uses a dictionary works with any coding
def is_permutation_dict(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    
    if n1 != n2:
        return False
    
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


# Uses a set. Works with any coding
def is_permutation_set(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    
    if n1 != n2:
        return False
    
    unique_chars = set()
    
    for ch in s1:
        if ch not in unique_chars:
            unique_chars |= {ch}
            k = 0
            for c in s1:
                if c == ch:
                    k += 1
            for c in s2:
                if c == ch:
                    k -= 1
            if k != 0:
                return False

    return True


print(is_permutation_set('ab c', 'cb a'))
print(is_permutation_set('abbddcd', 'ddddcba'))
 