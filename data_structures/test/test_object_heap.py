class Thing:
    def __init__(self, value):
        self.value = value

def test_insert():
    from heaps.object_heap import Heap
    heap = Heap()

    for i in range(10):
        heap.insert(Thing(i))

    assert len(heap.array) == 10

def test_delete():
    from random import shuffle
    from heaps.object_heap import Heap
    MAX_DATA = 100000

    heap = Heap()

    data = [x for x in range(MAX_DATA)]
    shuffle(data)
    for datum in data:
        heap.insert(Thing(datum))

    result = []
    for _ in range(MAX_DATA):
        result.append(heap.delete().value)

    data.sort(reverse=True)

    assert result == data

def test_sort():
    from random import shuffle
    from heaps.object_heap import Heap
    MAX_DATA = 100000

    heap = Heap()

    data = [x for x in range(MAX_DATA)]
    shuffle(data)

    result = heap.sort([Thing(x) for x in data])
    data.sort(reverse=True)

    assert [x.value for x in result] == data

