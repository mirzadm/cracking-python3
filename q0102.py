"""Reverse a string."""

def reverse(string):
    
    n = len(string) 
    string2 = ''

    for i in range(n-1, -1, -1):
        string2 += string[i]

    return string2


# print(reverse(''))
# print(reverse('a'))
# print(reverse('ab'))
# print(reverse('0123456789'))

