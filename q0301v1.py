"""Use one array to build 3 stacks. Fixed size version."""

class ThreeStack:

    def __init__(self, size):
        if size >= 3:
            self.size = size
            self.array = [None] * size
            self.limits = [(0, size//3 - 1), (size//3, 2*size//3 - 1),
                          (2*size//3, size-1)]
            self.top = [None] * 3
        else:
            self.size = None

    def push(self, index, data):
        if self.size is not None:
            if index in range(3):
                if self.top[index] is None:
                    self.top[index] = self.limits[index][0]
                    self.array[self.top[index]] = data
                elif self.top[index] < self.limits[index][1]:
                    self.top[index] += 1
                    self.array[self.top[index]] = data

    def pop(self, index):
        result = None
        if self.size is not None:
            if index in range(3):
                if self.top[index] is not None:
                    result = self.array[self.top[index]]
                    self.top[index] -= 1
                    if self.top[index] < self.limits[index][0]:
                        self.top[index] = None

        return result

