
def test_insert():
    from heap import Heap
    heap = Heap()

    for i in range(10):
        heap.insert(i)

    assert len(heap.array) == 10

def test_delete():
    from random import shuffle
    from heap import Heap
    MAX_DATA = 100000

    heap = Heap()

    data = [x for x in range(MAX_DATA)]
    shuffle(data)
    for datum in data:
        heap.insert(datum)

    result = []
    for _ in range(MAX_DATA):
        result.append(heap.delete())

    data.sort(reverse=True)

    assert result == data
