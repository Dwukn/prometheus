# Linked List - Notes and Concepts

## What is a Linked List?

A **Linked List** is a linear data structure where elements (nodes) are stored in memory in a non-contiguous manner. Each node contains:
- **Data**: The actual value or information.
- **Pointer (next)**: A reference (or pointer) to the next node in the sequence.

Unlike arrays, where elements are stored in contiguous memory locations, linked lists allow for dynamic memory allocation and efficient insertions or deletions.

## Types of Linked Lists

1. **Singly Linked List**: Each node points to the next node in the sequence. The last node points to `null`, indicating the end of the list.

   ```cpp
   struct Node {
       int data; // Value stored in the node
       Node* next; // Pointer to the next node
   };
   ```

2. **Doubly Linked List**: Each node contains two pointers — one to the next node and one to the previous node. This allows traversal in both directions (forward and backward).

   ```cpp
   struct Node {
       int data;
       Node* next; // Pointer to the next node
       Node* prev; // Pointer to the previous node
   };
   ```

3. **Circular Linked List**: In this type, the last node’s next pointer points to the head of the list, making the list circular. This can be implemented in both singly and doubly linked lists.

## Basic Operations

### 1. **Insertion**
Inserting a node involves adding a new node at a specific position in the list. Common insertion cases include:
- **At the beginning**: Adjust the head pointer to point to the new node.
- **At the end**: Traverse to the last node and set its next pointer to the new node.
- **At a specific position**: Traverse the list to find the correct position and adjust the pointers accordingly.

### 2. **Deletion**
Deletion involves removing a node from a specified position:
- **From the beginning**: The head pointer is updated to the next node.
- **From the end**: Traverse to the second-to-last node and set its next pointer to `null`.
- **From a specific position**: Adjust the pointers of the nodes before and after the node to be deleted.

### 3. **Traversal**
Traversal is the process of visiting each node in the list, usually for operations like printing or processing data. It starts at the head node and follows the `next` pointers until the end of the list is reached.

### 4. **Search**
Searching for a specific value involves traversing the list and checking each node's data.

### 5. **Reversal**
Reversing a linked list means reversing the direction of the pointers. The head pointer must be updated to point to the last node, and each node's `next` pointer is updated to point to the previous node.

### 6. **Freeing/Deallocation**
When a linked list is no longer needed, it is important to free the memory allocated to the nodes. This involves traversing the list and deleting each node.

## Advantages of Linked Lists
- **Dynamic Size**: Unlike arrays, linked lists don’t require pre-allocation of memory. They can grow or shrink dynamically as elements are inserted or deleted.
- **Efficient Insertions/Deletions**: Inserting or deleting nodes, especially at the beginning or middle, is more efficient than in an array, where shifting elements is required.

## Disadvantages of Linked Lists
- **Memory Overhead**: Each node requires extra memory for the pointer (`next`), which leads to higher memory usage.
- **Access Time**: Accessing an element at a particular index requires traversing the list from the head node, which takes linear time (`O(n)`).

## Linked List Operations in C++

Here’s a simple implementation of a **Singly Linked List** with basic operations such as insertion, deletion, and traversal.

```cpp
#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

Node* head = nullptr;

// Insert at the beginning
void Insert(int data) {
    Node* newNode = new Node();
    newNode->data = data;
    newNode->next = head;
    head = newNode;
}

// Delete the first node
void Delete() {
    if (head == nullptr) return;  // Empty list, nothing to delete
    Node* temp = head;
    head = head->next;
    delete temp;
}

// Print the list
void Print() {
    Node* temp = head;
    while (temp != nullptr) {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}

int main() {
    Insert(10);
    Insert(20);
    Insert(30);

    cout << "List: ";
    Print();

    Delete(); // Remove the first node (10)

    cout << "List after deletion: ";
    Print();

    return 0;
}
```

### Key Functions in the Example:
1. **Insert**: Adds a new node at the beginning of the list.
2. **Delete**: Removes the first node from the list.
3. **Print**: Traverses the list and prints all the elements.

## Common Use Cases
- **Dynamic Memory Allocation**: Linked lists are often used in systems where memory needs to be allocated and deallocated dynamically.
- **Implementation of Data Structures**: They are used to implement other data structures like stacks, queues, hash tables, and more.
- **Representing Sparse Data**: They can represent sparse data (e.g., adjacency lists in graphs) efficiently.

## Time Complexity of Linked List Operations
- **Insertion**:
  - At the beginning: `O(1)`
  - At the end: `O(n)` (if we don’t have a tail pointer)
  - At a specific position: `O(n)`

- **Deletion**:
  - From the beginning: `O(1)`
  - From the end: `O(n)`
  - From a specific position: `O(n)`

- **Traversal/Search**: `O(n)`

- **Reversal**: `O(n)`

## Conclusion

Linked lists are an important and versatile data structure, especially useful in situations where dynamic memory allocation, efficient insertions, and deletions are required. However, they come with trade-offs such as additional memory usage for pointers and slower element access times compared to arrays.
