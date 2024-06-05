# Stack implementation using linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty. Cannot pop.")
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.is_empty():
            raise ValueError("Stack is empty. Cannot peek.")
        return self.top.data

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return

        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Test the stack implementation
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack after pushing elements:")
stack.display()

print("Popped item:", stack.pop())
print("Popped item:", stack.pop())

print("Stack after popping elements:")
stack.display()

print("Top of the stack:", stack.peek())



# Queue implementation using Linked List

class Node2:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node2(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty. Cannot dequeue.")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def peek(self):
        if self.is_empty():
            raise ValueError("Queue is empty. Cannot peek.")
        return self.front.data

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return

        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Test the queue implementation
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue after enqueueing elements:")
queue.display()

print("Dequeued item:", queue.dequeue())
print("Dequeued item:", queue.dequeue())

print("Queue after dequeuing elements:")
queue.display()

print("Front of the queue:", queue.peek())


# Dequeue implementation using linked list.

class Node3:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def add_front(self, data):
        new_node = Node3(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

    def add_rear(self, data):
        new_node = Node3(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

    def remove_front(self):
        if self.is_empty():
            raise ValueError("Deque is empty. Cannot remove from the front.")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None
        return data

    def remove_rear(self):
        if self.is_empty():
            raise ValueError("Deque is empty. Cannot remove from the rear.")
        data = self.rear.data
        self.rear = self.rear.prev
        if self.rear is None:
            self.front = None
        else:
            self.rear.next = None
        return data

    def peek_front(self):
        if self.is_empty():
            raise ValueError("Deque is empty. Cannot peek from the front.")
        return self.front.data

    def peek_rear(self):
        if self.is_empty():
            raise ValueError("Deque is empty. Cannot peek from the rear.")
        return self.rear.data

    def display(self):
        if self.is_empty():
            print("Deque is empty.")
            return

        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Test the deque implementation
deque = Deque()
deque.add_front(1)
deque.add_front(2)
deque.add_rear(3)
deque.add_rear(4)

print("Deque after adding elements:")
deque.display()

print("Removed from front:", deque.remove_front())
print("Removed from rear:", deque.remove_rear())

print("Deque after removing elements:")
deque.display()

print("Front of the deque:", deque.peek_front())
print("Rear of the deque:", deque.peek_rear())
