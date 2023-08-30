from heap import MinHeap

def top_k_max(array, k):
    heap = MinHeap(k)
    for i, el in enumerate(array):
        heap.put(el)
        if i >= k:
            heap.pop()

    result = []
    for i in range(k):
        result.append(heap.pop())

    return result

example, result = [8, 11, 2, 3, 4, 5, 6, 7, 3, 10, 1, 2, 3], [5, 6, 7, 8, 10, 11]
print(top_k_max(example, 6))
print(top_k_max(example, 6) == result)
