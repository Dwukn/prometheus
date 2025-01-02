# STACK

## WHAT is a STACK?
A **Stack** is a simple *Linear Data Structure* that follows the [**LIFO (Last In, First Out)**](#LIFO) principle, meaning the element that has been added most recently is the first to be removed.

### Basic Operations on Stack
- **Push:** Adds an element on top of the stack.
- **Pop:** Removes an element from the top of the stack and returns it.
- **Peek (or Top):** Returns the element on top without removing it.
- **isEmpty:** Checks if the stack is empty.
- **Size:** Returns the size of the stack or, simply put, returns the number of elements in the stack.

### Stack in Python
In Python, a list can be used to create a stack. However, this is not the most efficient method since Python lists are dynamic arrays, which means they need to occasionally reallocate memory when they grow, causing increased time complexity. A better alternative is to use **Deque** from the `collections` module, which provides a more efficient solution.

```Python
from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    # Push element onto the stack
    def push(self, item):
        self.stack.append(item)

    # Pop element from the stack
    def pop(self):
        if self.isEmpty():
            return "Stack is empty!"
        return self.stack.pop()

    # Peek the top element
    def peek(self):
        if self.isEmpty():
            return "Stack is empty!"
        return self.stack[-1]

    # Check if stack is empty
    def isEmpty(self):
        return len(self.stack) == 0

    # Get the size of the stack
    def size(self):
        return len(self.stack)

# Usage
stack = Stack()
stack.push(10)
stack.push(20)
print(stack.peek())  # Output: 20
print(stack.pop())   # Output: 20
print(stack.size())  # Output: 1
```

## Optimizing Stack Usage in Python

To improve the performance of stack operations in Python, consider using **Deque** from the `collections` module, as it provides O(1) time complexity for both append and pop operations from either end of the deque. The **deque** is implemented as a doubly-linked list, so it avoids the resizing issues that can occur when using Python lists for stacks.

#### Comparison:
- **List Stack (using `append()` and `pop()`):** O(1) for operations, but resizing could add overhead if the stack grows too large.
- **Deque Stack:** Always O(1) for both push and pop operations, with no resizing overhead.

### Operations in Stack

- **Push:** O(1)
- **Pop:** O(1)
- **Peek (or Top):** O(1)
- **isEmpty:** O(1)
- **Size:** O(1)

---

### Use Cases of Stack
- **Expression Evaluation:** Used for parsing expressions (e.g., evaluating postfix or infix expressions).
- **Function Call Management (Recursion):** The call stack in programming manages function calls.
- **Undo Mechanism:** Used in applications like text editors to manage undo and redo operations.
- **Backtracking Algorithms:** Stacks are used in algorithms that require going back to previous states, such as in maze-solving or puzzle-solving algorithms.

---

### Applications of Stack

1. **Expression Conversion:**
   Convert infix expressions to postfix or prefix notation using stacks.

2. **Parentheses Matching:**
   Used to check whether parentheses, brackets, or braces in an expression are balanced (e.g., for code syntax validation).

3. **DFS for Graph Traversal:**
   Stack is used in **Depth-First Search (DFS)** for graph traversal, especially in iterative implementations.

4. **Undo/Redo Operations:**
   Stacks are used to keep track of user actions for undo and redo functionality in text editors or image editors.

---

### Stack Conditions
1. **Stack Overflow:** Occurs when the stack exceeds its fixed size (in static stack implementations).
2. **Stack Underflow:** Occurs when an operation attempts to pop an element from an empty stack.

### Types of Stack
1. **Static Stack:** A stack with a fixed size, where no new elements can be added once the stack is full.
2. **Dynamic Stack:** A stack that grows dynamically as needed (e.g., using Python's list or deque).

---

## **LIFO (Last In, First Out) Operation**

### **Introduction**
**LIFO** (Last In, First Out) is the principle used to describe the order of operations in data structures such as **Stacks**. It means that the **last element added** is the **first one to be removed**.

### **Key Concepts**

1. **What is LIFO?**
   LIFO is a data processing order where:
   - The most **recently added** element is processed **first**.
   - The most **recently added** element is **removed** before any other element.

2. **LIFO Characteristics:**
   - **Addition**: New elements are added on top of the stack.
   - **Removal**: The most recently added element is removed first.
   - **No Random Access**: To access an element, you must pop elements from the top.

### **Operations in LIFO:**
1. **Push**: Add an element to the top of the stack.
2. **Pop**: Remove and return the element from the top of the stack.
3. **Peek (or Top)**: View the element at the top of the stack without removing it.
4. **isEmpty**: Check if the stack is empty.
5. **Size**: Get the number of elements in the stack.

---

### **Example Walkthrough**

Let's visualize how **LIFO** works in a stack with a series of operations:

1. **Push 10**
2. **Push 20**
3. **Push 30**
4. **Pop**
5. **Pop**
6. **Pop**

### **Operations Sequence:**
- **Push 10**: Stack → `[10]`
- **Push 20**: Stack → `[10, 20]`
- **Push 30**: Stack → `[10, 20, 30]`

Now, we pop elements:
- **Pop**: Stack → `[10, 20]` (Removes **30**)
- **Pop**: Stack → `[10]` (Removes **20**)
- **Pop**: Stack → `[]` (Removes **10**)

The output sequence of popped elements is **30, 20, 10**, which follows the **LIFO** order.

---

### **Visualizing the LIFO Principle:**
```text
   --------
   |  30  |  <- Top (last pushed element)
   --------
   |  20  |
   --------
   |  10  |  <- Bottom (first pushed element)
   --------

Order of Removal (LIFO):
- First Pop: 30
- Second Pop: 20
- Third Pop: 10
```

---

### **LIFO vs FIFO (First In, First Out)**

#### **LIFO (Last In, First Out):**
- **Stack** follows LIFO.
- The most recently added element is removed first.

#### **FIFO (First In, First Out):**
- **Queue** follows FIFO.
- The first element added is the first to be removed.

#### **FIFO Example:**
1. **Enqueue 10**
2. **Enqueue 20**
3. **Enqueue 30**
4. **Dequeue**
5. **Dequeue**
6. **Dequeue**

Queue operations:
- **Enqueue 10**: Queue → `[10]`
- **Enqueue 20**: Queue → `[10, 20]`
- **Enqueue 30**: Queue → `[10, 20, 30]`

Dequeue operations:
- **Dequeue**: Queue → `[20, 30]` (Removes **10**)
- **Dequeue**: Queue → `[30]` (Removes **20**)
- **Dequeue**: Queue → `[]` (Removes **30**)

In **FIFO**, the order of removal is **10, 20, 30**, as the **first element added** is removed first.

---

## **Applications of LIFO:**
LIFO is used in various scenarios in computer science and real-world applications:
1. **Stacks**: The most common data structure that follows the LIFO principle.
2. **Function Call Stack**: The operating system maintains a stack to handle function calls and recursive calls.
3. **Undo Mechanism**: Applications like text editors use LIFO to manage undo operations, where the most recent change is undone first.
4. **Expression Evaluation**: LIFO is used in algorithms to evaluate expressions, such as converting infix to postfix notation.
5. **Depth-First Search (DFS)**: In graph traversal, DFS uses LIFO to explore nodes iteratively.

---

## **Conclusion:**

LIFO is a fundamental principle used in many algorithms and data structures. It allows efficient management of data when we need to process the most recently added items first. **Stacks**, as the data structure implementing LIFO, are vital in numerous applications, including expression parsing, recursion handling, and backtracking problems.
