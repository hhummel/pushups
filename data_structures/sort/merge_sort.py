class MergeSort:
    def __init__(self):
        self.list = list()
        self.sorted = None

    def merge(self, q1, q2):
        new_list = list()
        
        while q1 and q2:
            if q1[0] < q2[0]:
                new_list.append(q1.pop(0))
            else:
                new_list.append(q2.pop(0))
        
        if q1: 
            new_list += q1
        if q2: 
            new_list += q2

        return new_list

    def recursive_sort(self, q):
        len_q = len(q)
        if len_q < 2:
            return q
        else:
            mid = len_q // 2
            left = self.recursive_sort(q[:mid])
            right = self.recursive_sort(q[mid:])
            return self.merge(left, right)

    def sort(self):
        return self.recursive_sort(self.list)
                
