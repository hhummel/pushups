class Heap(object):
    def __init__(self):
        self.array = []

    def insert(self, value):
        index = len(self.array)
        self.array.append(value)
        self.trickle_up(index)

    def delete(self):
        if not self.array:
            return None
        top = self.array[0]
        bottom = self.array.pop()
        if self.array:
            self.array[0] = bottom
            self.trickle_down(0)
        return top 

    def trickle_up(self, index):
        parent = (index - 1) // 2
        if parent >= 0 and self.array[index] > self.array[parent]:
            self.array[index], self.array[parent] = self.array[parent], self.array[index]
            return self.trickle_up(parent)
        else: 
            return None

    def trickle_down(self, index):
        left = larger = 2 * index + 1
        right = left + 1
        if left >= len(self.array):
            return None
        if right < len(self.array) and self.array[right] > self.array[left]:
            larger = right
        if self.array[index] < self.array[larger]:
            self.array[index], self.array[larger] = self.array[larger], self.array[index]
            return self.trickle_down(larger)
        return None