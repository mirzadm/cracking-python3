"""Chapter 3: Question 1.

Use one array to implement 3 stacks.
"""


class ThreeStacks:
    """Implements 3 stacks using one list.

    Raises:
        ValueError: If the initialized with a size < 3.
    """

    def __init__(self, size):
        if size < 3:
            raise ValueError('Size must greater than or equal to 3.')

        self.size = size
        self.array = [None] * size
        self.limits = [(0, size//3 - 1), (size//3, 2*size//3 - 1),
                      (2*size//3, size-1)]
        self.top = [None] * 3

    def push(self, index, data):
        """Pushes data to the proper stack according to index.
        
        Nothing happens if the correspoing stack is full.

        Raises:
            IndexError: If index not 0, 1, or 2.
        """
        if index not in (0, 1, 2):
            raise IndexError('Index must be 0, 1, or 2.')

        if self.is_empty(index):
            self.top[index] = self.limits[index][0]
            self.array[self.top[index]] = data
        elif self.top[index] < self.limits[index][1]:
            self.top[index] += 1
            self.array[self.top[index]] = data

    def pop(self, index):
        """Pops a value from the stack referenced by index.

        Returns:
            None if stack is empty.
        Raises:
            IndexError: If index not 0, 1, or 2.
        """
        if index not in (0, 1, 2):
            raise IndexError('Index must be 0, 1, or 2.')

        result = None
        if self.top[index] is not None:
            result = self.array[self.top[index]]
            self.top[index] -= 1
            if self.top[index] < self.limits[index][0]:
                self.top[index] = None

        return result

    def is_empty(self, index):
        """Checks emptiness of the stack pointed to by index.

        Raises:
            IndexError: If index not 0, 1, or 2.
        """
        if index not in (0, 1, 2):
            raise IndexError('Index must be 0, 1, or 2.')

        return (self.top[index] is None)
