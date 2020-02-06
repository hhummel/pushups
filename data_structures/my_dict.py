class MyDict(object):

    def __init__(self, size = 1024):
        self.size = size
        self.arr = [[] for _ in range(self.size)]

    def get(self, k):
        big_hash = hash(k)
        hash_key = big_hash % self.size
        for key, value in self.arr[hash_key]:
            if big_hash == key:
                return value
        return None
         
    def set(self, k, v):
        big_hash = hash(k)
        hash_key = big_hash % self.size
        for index, (key, value) in enumerate(self.arr[hash_key]):
            if key == big_hash:
                self.arr[hash_key][index] = (big_hash, v)
                break
        self.arr[hash_key].append((big_hash, v))

    def delete(self, k):
        big_hash = hash(k)
        hash_key = big_hash % self.size
        for index, (key, value) in enumerate(self.arr[hash_key]):
            if key == big_hash:
                del self.arr[hash_key][index]
                break
        print(f"Key {k} not found")
 

