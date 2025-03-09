class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Adds an item to the rear of the queue."""
        self.queue.append(item)

    def dequeue(self):
        """Removes and returns the front item of the queue."""
        if self.is_empty():
            print("Queue is empty!")
        else:
            return self.queue.pop(0)

    def front(self):
        """Returns the front item without removing it."""
        if self.is_empty():
            print("Queue is empty!")
        else:
            return self.queue[0]

    def is_empty(self):
        """Returns True if the queue is empty, False otherwise."""
        return len(self.queue) == 0

    def size(self):
        """Returns the size of the queue."""
        return len(self.queue)

    def front(self):
        """Returns the front item without removing it."""
        if self.is_empty():
            print("Queue is empty!")
        else:
            return self.queue[0]

    def rear(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            return self.queue[-1]

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Front Value",queue.front())  # Output: 10
print("Rear Value:",queue.rear())  # Output: 30
print("Removed Value",queue.dequeue())  # Output: 10
print("Size of Queue",queue.size())  # Output: 2
print("Is Empty?",queue.is_empty())  # Output: False


# Queue using list
list1 = []
list1.append('a')
list1.append('b')
list1.append('c')
print("Initial queue")
print(list1)
print("Elements dequeued from queue")
print(list1.pop(0))
print(list1.pop(0))
print(list1.pop(0))
print("Queue after removing elements")
print(list1)
