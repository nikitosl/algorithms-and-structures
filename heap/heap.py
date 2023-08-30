class MinHeap:
    def __init__(self, size):
        self.storage = []
        self.size = size

    def get_child_indexes(self, i):
        child1 = 2 * i + 1
        if child1 >= len(self.storage):
            return []
            
        child2 = 2 * i + 2
        if child2 >= len(self.storage):
            return [(i, child1)]
            
        return [(i, child1), (i, child2)]

    def get_parent_index(self, i):
        if i == 0:
            return None
            
        if i % 2 == 0:
            return (i - 2) // 2
            
        return (i - 1) // 2
    
    def pop(self):
        if len(self.storage) == 0:
            return None
            
        first_element = self.storage[0]
        self.storage[0] = self.storage[-1]
        self.storage = self.storage[:-1]

        child_indexes = self.get_child_indexes(0)
        while len(child_indexes) > 0:
            current_index, child_index = child_indexes.pop()
            if self.storage[child_index] < self.storage[current_index]:
                buf = self.storage[child_index]
                self.storage[child_index] = self.storage[current_index]
                self.storage[current_index] = buf
                child_indexes += self.get_child_indexes(child_index)
        
        return first_element

    def put(self, element):
        current_index = len(self.storage)
        self.storage.append(element)
        while True:
            parent_index = self.get_parent_index(current_index)
            if parent_index is None:
                break

            if self.storage[current_index] >= self.storage[parent_index]:
                break
            
            buf = self.storage[parent_index]
            self.storage[parent_index] = self.storage[current_index]
            self.storage[current_index] = buf
            current_index = parent_index
