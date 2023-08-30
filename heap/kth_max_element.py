from heap import MinHeap
import heapq

def kth_max_element_custom(array, k):
    heap = MinHeap(k)
    for i, el in enumerate(array):
        heap.put(el)
        if i >= k:
            heap.pop()
    return heap.pop()

def kth_max_element_fast(array, k):
    heap = array[:k]
    heapq.heapify(heap)

    for num in array[k:]:
        if num > heap[0]:
            heapq.heappush(heap, num)
            heapq.heappop(heap)
    return heap[0]

example, result = [8, 11, 2, 3, 4, 5, 6, 7, 3, 10, 1, 2, 3], 8
print(kth_max_element_custom(example, 3))
print(kth_max_element_custom(example, 3) == result)
print(kth_max_element_fast(example, 3))
print(kth_max_element_fast(example, 3) == result)
