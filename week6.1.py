import random
class MinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def insert(self, data):
        self.heap_list.append(data)
        self.current_size += 1
        self.percolate_up(self.current_size)

    def percolate_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i = i // 2

    def display(self):
        print("Binary Heap Tree:")
        for i in range(1, self.current_size + 1):
            print(self.heap_list[i], end=" ")
        print()

# Generate a random list of 10 integers between 1 and 100
random_list = random.sample(range(1, 101), 10)

# Create the binary heap tree by inserting the integers one by one
min_heap = MinHeap()
for num in random_list:
    min_heap.insert(num)

# Display the binary heap tree
min_heap.display()





