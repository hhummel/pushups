class Heap(object):
    '''Heap of Thing objects with attribute value'''
    def __init__(self, reverse=False):
        self.array = []
        self.reverse = reverse

    def insert(self, thing):
        index = len(self.array)
        self.array.append(thing)
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

    def sort(self, list_):
        self.array = []
        for element in list_:
            self.insert(element)
        return [self.delete() for _ in range(len(list_))]

    def trickle_up(self, index):
        parent = (index - 1) // 2
        if parent >= 0 and self.reverse == False and self.array[index].value > self.array[parent].value:
            self.array[index], self.array[parent] = self.array[parent], self.array[index]
            return self.trickle_up(parent)
        elif parent >= 0 and self.reverse == True and self.array[index].value < self.array[parent].value:
            self.array[index], self.array[parent] = self.array[parent], self.array[index]
            return self.trickle_up(parent)
        else: 
            return None

    def trickle_down(self, index):
        left = preferred = 2 * index + 1
        right = left + 1
        if left >= len(self.array):
            return None
        if right < len(self.array) and self.reverse == False and self.array[right].value > self.array[left].value:
            preferred = right
        elif right < len(self.array) and self.reverse == True and self.array[right].value < self.array[left].value:
            preferred = right
        if self.reverse ==  False and self.array[index].value < self.array[preferred].value:
            self.array[index], self.array[preferred] = self.array[preferred], self.array[index]
            return self.trickle_down(preferred)
        elif self.reverse ==  True and self.array[index].value > self.array[preferred].value:
            self.array[index], self.array[preferred] = self.array[preferred], self.array[index]
            return self.trickle_down(preferred)
        return None
