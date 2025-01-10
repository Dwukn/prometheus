# Queue Data Structure - Notes

## Introduction
A **queue** is a linear data structure that follows the **First In, First Out (FIFO)** principle. This means that the first element added to the queue is the first one to be removed, similar to a line at a ticket counter where the person who stands first is the first to be served.

### Key Operations:
1. **Enqueue**: Adds an element to the rear of the queue.
2. **Dequeue**: Removes and returns the front element of the queue.
3. **Front (or Peek)**: Returns the front element without removing it.
4. **IsEmpty**: Checks if the queue is empty.
5. **Size**: Returns the number of elements in the queue.

## Basic Implementation in Python

Python doesn’t have a built-in queue data structure, but we can easily implement it using a **list** or **deque** from the `collections` module.

### Queue using List:
```python
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
```

### Example usage:
```python
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.front())  # Output: 10
print(queue.dequeue())  # Output: 10
print(queue.size())  # Output: 2
print(queue.is_empty())  # Output: False
```

### Queue using Deque:
The `deque` (double-ended queue) from the `collections` module provides better performance for queue operations because it allows **O(1)** time complexity for both append and pop operations from both ends of the deque.

```python
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        """Adds an item to the rear of the queue."""
        self.queue.append(item)

    def dequeue(self):
        """Removes and returns the front item of the queue."""
        if self.is_empty():
            print("Queue is empty!")
        else:
            return self.queue.popleft()

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
```

### Example usage with Deque:
```python
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.front())  # Output: 10
print(queue.dequeue())  # Output: 10
print(queue.size())  # Output: 2
print(queue.is_empty())  # Output: False
```

## Time Complexity of Queue Operations:
1. **Enqueue**: O(1) – Adding an item to the rear of the queue is a constant time operation.
2. **Dequeue**: O(1) – Removing an item from the front of the queue is a constant time operation.
3. **Front**: O(1) – Accessing the front item is a constant time operation.
4. **IsEmpty**: O(1) – Checking if the queue is empty is a constant time operation.
5. **Size**: O(1) – Getting the size of the queue is a constant time operation.

## Applications of Queue:
Queues are widely used in various applications such as:
1. **Breadth-First Search (BFS)**: A graph traversal algorithm that uses a queue to explore the graph level by level.
2. **Task Scheduling**: In operating systems, queues are used for managing tasks and processes.
3. **Print Queue**: Managing printing jobs in a printer queue.
4. **Buffering**: Used in scenarios such as streaming, where data is stored temporarily before being processed.
5. **Handling Requests**: Web servers use queues to handle incoming requests in the order they arrive.

## Example Problem: Implementing BFS (Breadth-First Search)
We can use a queue to implement the **BFS** algorithm to traverse a graph.

```python
from collections import deque

def bfs(graph, start):
    visited = set()  # Set to track visited nodes
    queue = deque([start])  # Initialize queue with the starting node

    while queue:
        node = queue.popleft()  # Dequeue the front element
        if node not in visited:
            print(node, end=" ")  # Process the node (print it)
            visited.add(node)  # Mark the node as visited

            # Enqueue all unvisited neighbors
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example graph (adjacency list representation)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Start BFS from node 'A'
bfs(graph, 'A')  # Output: A B C D E F
```

## Conclusion
A **queue** is a fundamental data structure that operates on the **FIFO** principle, making it useful for various applications like task scheduling, BFS, and buffering. Mastering queues is essential for understanding algorithms that involve managing elements in a sequential manner.

---

### Further Reading
- [Queue Operations](https://en.wikipedia.org/wiki/Queue_(abstract_data_type))
- [Queue in Python using List and Deque](https://docs.python.org/3/library/collections.html#deque)
- [Graph Traversal: BFS](https://en.wikipedia.org/wiki/Breadth-first_search)

<br>

```
This content provides you with a solid understanding of Queues, their operations, implementation, and applications. You can save it as `README.md` and refer to it whenever you need guidance on working with queues in Python! Feel free to ask if you'd like to explore any topic further or need additional explanations.
