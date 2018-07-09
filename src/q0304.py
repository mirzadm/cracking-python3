"""Chapter 3: Question 4.

Towers of Hanoi.
"""


def towers_of_hanoi(n ,s1, s2, s3):
    """Moves n plates from s1 to s3.

    Assumes there exist n plates on s1.
    """

    if n == 1:
        s2.push(s1.pop())
        s3.push(s2.pop())
    else:   
        towers_of_hanoi(n-1, s1, s2, s3)
        s2.push(s1.pop())
        towers_of_hanoi(n-1, s3, s2, s1)
        s3.push(s2.pop())
        towers_of_hanoi(n-1, s1, s2, s3)
