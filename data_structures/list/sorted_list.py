class SortedList:

    def __init__(self):
        self.list = list()

    def search(self, value, lower=0, upper=None):
        if upper is None:
            upper = len(self.list)-1
        if lower > upper:
            return "Search failed"

        mid = (upper + lower) // 2
        trial = self.list[mid]

        if value == trial:
            return mid
        elif value > trial:
            return self.search(value, mid + 1, upper)
        else: 
            return self.search(value, lower, mid - 1)    
