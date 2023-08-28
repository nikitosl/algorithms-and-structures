from structures.heap import MinHeap

def top_k_max(array, k):
    heap = MinHeap(k)
    for i, el in enumerate(array):
        heap.put(el)
        if i >= k:
            heap.pop()
        print(heap.storage)

    result = []
    for i in range(k):
        result.append(heap.pop())

    return result

print(top_k_max([8, 11, 2, 3, 4, 5, 6, 7, 3, 10, 1, 2, 3], 6))
