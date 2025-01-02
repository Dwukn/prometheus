# Concepts on problems

A **circular queue** is a type of queue data structure that uses a fixed-size array in a circular manner to manage the elements. Unlike a normal queue, where the rear of the queue is at the end of the array, in a circular queue, both the front and rear pointers can wrap around to the beginning of the array when they reach the end. This avoids the problem of wasted space in the array when elements are dequeued.

### Characteristics of a Circular Queue:
1. **Fixed size**: A circular queue has a fixed size. Once the queue reaches its maximum capacity, no more elements can be added until space becomes available.
2. **Front and rear pointers**: The queue maintains two pointers:
   - **Front**: Points to the front element of the queue (the element that will be dequeued next).
   - **Rear**: Points to the next available position where a new element will be inserted (enqueued).
3. **Wrap-around**: When either pointer (front or rear) reaches the end of the array, it wraps around to the beginning of the array, making the array behave circularly.
4. **Overflow and underflow**:
   - **Overflow**: The queue is full when the rear pointer is one position behind the front pointer (in a circular sense).
   - **Underflow**: The queue is empty when the front pointer equals the rear pointer.

### Key Operations in a Circular Queue:
1. **Enqueue** (adding an element to the queue):
   - Add an element at the position indicated by the rear pointer.
   - Move the rear pointer to the next position, and wrap it around if needed.
2. **Dequeue** (removing an element from the queue):
   - Remove the element at the position indicated by the front pointer.
   - Move the front pointer to the next position, and wrap it around if needed.
3. **Peek** (getting the front element without removing it):
   - Return the element at the front position.
4. **Is Empty** (check if the queue is empty):
   - The queue is empty when the front pointer is equal to the rear pointer.
5. **Is Full** (check if the queue is full):
   - The queue is full when the next position of the rear pointer is equal to the front pointer (in a circular manner).

### Circular Queue Representation:
Consider an array `queue[]` with a fixed size of `n`. We maintain two pointers:
- `front`: Points to the first element.
- `rear`: Points to the last element (or the position where the next element will be inserted).

Example of a circular queue (with size 5):

```
queue = [10, 20, 30, 40, 50]
front = 0
rear = 4
```

If the queue is full, enqueueing another element will overwrite the oldest element in the queue, and the front pointer will move to the next position to maintain the queue's circular property.

### Circular Queue in Python:
Here's a simple implementation of a circular queue using a fixed-size list:

```python
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
```

### Explanation of Operations:
- **Enqueue**: Adds elements to the queue. The rear pointer wraps around if the queue is full and there's space available.
- **Dequeue**: Removes elements from the queue. The front pointer moves forward and wraps around when necessary.
- **Peek**: Shows the front element of the queue without removing it.
- **Display**: Prints the entire queue, starting from the front to the rear.

### Advantages of a Circular Queue:
1. **Efficient use of memory**: A circular queue makes full use of the array space by reusing the positions that are freed when elements are dequeued.
2. **Fixed size**: Since the size of the queue is fixed, it doesn't grow beyond the predefined limit, making it easy to manage memory.

### Use Cases for Circular Queues:
1. **Scheduling algorithms**: Circular queues are commonly used in round-robin scheduling for operating systems.
2. **Buffering**: Circular queues are used in data buffering, such as in streaming or data communication, where old data is overwritten by new data when the buffer is full.

#### In summary, a circular queue efficiently manages a fixed-size array by allowing pointers to "wrap around," thereby utilizing the entire space of the array and avoiding wasted space that might occur in a regular queue.

<br>

# CIRCULAR QUEUE

### Code Walkthrough:

```python
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size  # Initialize the queue with None
        self.front = -1  # Front points to the first element in the queue
        self.rear = -1   # Rear points to the last element in the queue
```

#### `__init__` method (Constructor):
- **`self.size`**: The size of the circular queue is set based on the argument passed during initialization. This defines the maximum capacity of the queue.
- **`self.queue`**: The queue itself is represented as a list of size `self.size`. Initially, all the elements in the list are set to `None`. This acts as the "container" for storing elements in the queue.
- **`self.front`**: The front pointer is initialized to `-1`, which indicates that the queue is empty initially.
- **`self.rear`**: The rear pointer is also initialized to `-1`, indicating that no elements have been added to the queue yet.

### Operations on the Circular Queue:

#### 1. **`is_empty` method**:
```python
def is_empty(self):
    return self.front == -1
```
- **Purpose**: This method checks if the queue is empty.
- **How it works**:
  - If the `front` pointer is `-1`, it means the queue is empty (because no elements have been added). In this case, the method returns `True`.
  - If `front` is not `-1`, the queue is not empty, and it returns `False`.

#### 2. **`is_full` method**:
```python
def is_full(self):
    return (self.rear + 1) % self.size == self.front
```
- **Purpose**: This method checks if the queue is full.
- **How it works**:
  - The queue is full when the next position of `rear` (calculated by `(self.rear + 1) % self.size`) is the same as `front`.
  - The modulo operation `% self.size` ensures that if `rear` reaches the end of the array, it wraps around to the beginning (circular nature).
  - If the `rear` is just one position behind the `front` in this circular manner, the queue is full.

#### 3. **`enqueue` method** (Add an element to the queue):
```python
def enqueue(self, item):
    if self.is_full():
        print("Queue is full! Cannot enqueue.")
        return
    if self.front == -1:  # If the queue is empty
        self.front = 0  # Set front to 0 since the first element is being added
    self.rear = (self.rear + 1) % self.size  # Move rear to the next position (circular)
    self.queue[self.rear] = item  # Add the item to the queue at the rear
    print(f"Enqueued: {item}")
```
- **Purpose**: This method adds an element (`item`) to the queue.
- **How it works**:
  1. It first checks if the queue is full by calling `is_full()`. If the queue is full, it prints a message and returns without adding the item.
  2. If the queue is empty (`front == -1`), the `front` pointer is set to `0` because the first element is being added to the queue.
  3. The `rear` pointer is updated by moving it to the next position using `(self.rear + 1) % self.size`. This ensures that when `rear` reaches the end of the array, it wraps around to the beginning of the array.
  4. The `item` is added to the queue at the position indicated by `rear`.
  5. A message is printed to indicate that the item has been enqueued.

#### 4. **`dequeue` method** (Remove an element from the queue):
```python
def dequeue(self):
    if self.is_empty():
        print("Queue is empty! Cannot dequeue.")
        return
    dequeued_item = self.queue[self.front]  # Get the item at the front
    if self.front == self.rear:  # If there's only one element in the queue
        self.front = self.rear = -1  # Reset the queue (empty it)
    else:
        self.front = (self.front + 1) % self.size  # Move front to the next position
    return dequeued_item
```
- **Purpose**: This method removes and returns the front element of the queue.
- **How it works**:
  1. It first checks if the queue is empty by calling `is_empty()`. If the queue is empty, it prints a message and returns.
  2. If the queue is not empty, it retrieves the item at the `front` of the queue.
  3. If there is only one item left in the queue (`front == rear`), it resets both the `front` and `rear` pointers to `-1`, effectively emptying the queue.
  4. If there are more than one elements in the queue, it moves the `front` pointer to the next position in the circular queue using `(self.front + 1) % self.size`.
  5. The dequeued item is returned.

#### 5. **`peek` method** (View the front element without removing it):
```python
def peek(self):
    if self.is_empty():
        print("Queue is empty!")
        return
    return self.queue[self.front]
```
- **Purpose**: This method returns the front element without removing it from the queue.
- **How it works**:
  1. It first checks if the queue is empty by calling `is_empty()`. If it is empty, it prints a message and returns.
  2. If the queue is not empty, it returns the item at the front of the queue (`self.queue[self.front]`).

#### 6. **`display` method** (Print the current state of the queue):
```python
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
```
- **Purpose**: This method prints all elements in the queue, starting from the front to the rear.
- **How it works**:
  1. It first checks if the queue is empty. If it is, it prints a message and returns.
  2. If the queue is not empty, it starts from the `front` pointer and iterates through the queue, printing each element.
  3. The pointer `i` is updated using `(i + 1) % self.size` to ensure circular behavior, meaning when the end of the queue is reached, it wraps around to the beginning.
  4. The loop stops when `i` equals the `rear` pointer, which indicates the last element in the queue.
  5. A newline is printed after the queue is displayed.

### Example of Circular Queue Usage:

```python
cq = CircularQueue(5)

# Enqueueing elements
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)

# Display the queue
cq.display()  # Output: 10 20 30 40 50

# Try to enqueue another element
cq.enqueue(60)  # Output: Queue is full! Cannot enqueue.

# Dequeue an element
print("Dequeued:", cq.dequeue())  # Output: 10
cq.display()  # Output: 20 30 40 50

# Enqueue another element
cq.enqueue(60)  # Output: Enqueued: 60
cq.display()  # Output: 20 30 40 50 60
```

### Key Points:
- **Circular nature**: When the rear pointer reaches the end of the array, it wraps around to the beginning using modulo arithmetic (`% self.size`).
- **Efficient memory usage**: A circular queue ensures that we don't waste space when elements are dequeued, as the pointers wrap around to utilize freed space.
- **Fixed size**: The queue has a fixed capacity, and overflow and underflow are managed accordingly.

This implementation provides an efficient way to simulate a queue with a fixed size that maintains its performance even as elements are added and removed in a circular manner.
