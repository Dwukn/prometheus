class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size  # Initialize the queue with None
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full! Cannot enqueue.")
            return
        if self.front == -1:  # If the queue is empty
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return
        dequeued_item = self.queue[self.front]
        if self.front == self.rear:  # If there's only one element
            self.front = self.rear = -1  # Reset the queue
        else:
            self.front = (self.front + 1) % self.size
        return dequeued_item

    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

# Example usage:
cq = CircularQueue(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)

cq.display()  # Displays: 10 20 30 40 50

cq.enqueue(60)  # Queue is full, cannot enqueue

print("Dequeued:", cq.dequeue())  # Dequeues 10
cq.display()  # Displays: 20 30 40 50

cq.enqueue(60)  # Enqueues 60
cq.display()  # Displays: 20 30 40 50 60
