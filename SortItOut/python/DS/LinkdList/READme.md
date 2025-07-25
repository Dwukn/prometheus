# Linked List Data Structure - Notes

## Introduction
A **linked list** is a linear data structure in which elements (nodes) are stored in a sequence where each node points to the next node in the sequence. Unlike arrays, linked lists do not require contiguous memory locations. This makes linked lists more dynamic and flexible in terms of memory allocation.

### Types of Linked Lists:
1. **Singly Linked List**: Each node has a value and a pointer/reference to the next node.
2. **Doubly Linked List**: Each node has a value, a pointer to the next node, and a pointer to the previous node.
3. **Circular Linked List**: The last node points to the first node, forming a circular structure.

## Basic Operations on Singly Linked List:
1. **Insertion**: Insert a node at the beginning, end, or a specific position.
2. **Deletion**: Delete a node from the beginning, end, or a specific position.
3. **Traversal**: Traverse through the list to display the elements.
4. **Search**: Search for an element in the linked list.
5. **Reverse**: Reverse the linked list.

## Implementation of Singly Linked List in Python

### Node Class:
Each node in a linked list contains two parts:
- **Data**: The value stored in the node.
- **Next**: A reference to the next node in the list (or `None` if it is the last node).

```python
class Node:
    def __init__(self, data):
        self.data = data  # Value of the node
        self.next = None  # Reference to the next node
```

### LinkedList Class:
The `LinkedList` class will handle various operations on the list such as insertion, deletion, and traversal.

```python
class LinkedList:
    def __init__(self):
        self.head = None  # Head of the linked list

    # 1. Insertion at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # Point the new node to the current head
        self.head = new_node  # Move the head to the new node

    # 2. Insertion at the end
    def insert_at_end(self, data):
        new_node = Node(data)  # Create a new node
        if self.head is None:
            self.head = new_node  # If the list is empty, new node is the head
            return
        last = self.head
        while last.next:
            last = last.next  # Traverse to the last node
        last.next = new_node  # Point the last node to the new node

    # 3. Deletion of a node with specific data
    def delete_node(self, key):
        current = self.head
        if current and current.data == key:  # Check if the node to be deleted is the head
            self.head = current.next  # Move the head to the next node
            current = None  # Free the memory
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next  # Traverse to find the node to be deleted

        if current is None:
            print("Node not found")
            return

        prev.next = current.next  # Unlink the node from the list
        current = None  # Free the memory

    # 4. Traversing the linked list
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # 5. Searching for an element in the list
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    # 6. Reversing the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Store the next node
            current.next = prev  # Reverse the current node's pointer
            prev = current  # Move prev and current one step forward
            current = next_node
        self.head = prev  # Update the head to the new reversed list
```

### Example Usage:
```python
# Create a linked list
ll = LinkedList()

# Insert elements at the beginning
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.insert_at_end(30)

# Traverse the list
ll.traverse()  # Output: 20 -> 10 -> 30 -> None

# Delete a node
ll.delete_node(10)
ll.traverse()  # Output: 20 -> 30 -> None

# Search for an element
print(ll.search(30))  # Output: True
print(ll.search(40))  # Output: False

# Reverse the linked list
ll.reverse()
ll.traverse()  # Output: 30 -> 20 -> None
```

## Time Complexity of Operations:
1. **Insertion at the beginning**: O(1) – Adding an element at the head.
2. **Insertion at the end**: O(n) – Traversing the entire list to add an element at the end.
3. **Deletion**: O(n) – Traversing the list to find the node to delete.
4. **Search**: O(n) – Searching for an element by traversing the list.
5. **Traversal**: O(n) – Traversing the entire list to print or perform actions on all elements.
6. **Reverse**: O(n) – Reversing the entire list.

## Applications of Linked List:
Linked lists are used in various applications such as:
1. **Dynamic Memory Allocation**: Memory blocks can be dynamically allocated and deallocated during runtime.
2. **Implementing Stacks and Queues**: Linked lists are often used to implement stack and queue data structures.
3. **Navigation Systems**: Doubly linked lists can be used to implement systems like browser history or music players, where both forward and backward navigation is required.
4. **Polynomial Representation**: Linked lists can represent polynomials, where each term is a node with its coefficient and exponent.
5. **Sparse Matrices**: Linked lists can be used to represent sparse matrices efficiently by storing only non-zero elements.

## Doubly Linked List (Optional Extension)

A **doubly linked list** is a type of linked list in which each node has two pointers:
1. **Next**: A pointer to the next node.
2. **Prev**: A pointer to the previous node.

### Code for Doubly Linked List:
```python
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    # Delete a node with specific data
    def delete_node(self, key):
        current = self.head
        while current:
            if current.data == key:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                current = None
                return
            current = current.next
        print("Node not found")
```

## Conclusion:
A **linked list** is a flexible and dynamic data structure, useful for applications where you need efficient insertion and deletion of elements. While singly linked lists are commonly used for basic operations, doubly linked lists allow for more efficient navigation in both directions, providing more powerful functionality.

---

### Further Reading:
- [Linked List on Wikipedia](https://en.wikipedia.org/wiki/Linked_list)
- [Python Documentation on Lists and Deques](https://docs.python.org/3/library/collections.html#deque)
- [Linked List Algorithms and Problems](https://www.geeksforgeeks.org/data-structures/linked-list/)
