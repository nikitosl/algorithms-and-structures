import heapq

def top_k_frequent(nums, k):
    hmap = dict()
    for num in nums:
        if num not in hmap:
            hmap[num] = 1
        else:
            hmap[num] += 1

    h = []
    for i, (num, counter) in enumerate(hmap.items()):
        heapq.heappush(h, (-counter, num))

    result = []
    for _ in range(k):
        result.append(heapq.heappop(h)[1])

    return result


example, result = [0,-1,-2,1,1,1,2,2,3,3,3,3,3], [3, 1]
print(top_k_frequent(example, 2))
print(top_k_frequent(example, 2) == result)