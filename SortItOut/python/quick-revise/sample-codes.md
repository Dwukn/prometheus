Sure! Here's Python code for some of the **easy DSA topics**:

### 1. **Arrays**

#### Basic operations (insert, delete, update)

```python
# Inserting an element
arr = [1, 2, 3, 4]
arr.append(5)  # Insert at the end
print("After Insertion:", arr)

# Deleting an element
arr.remove(3)  # Remove first occurrence of 3
print("After Deletion:", arr)

# Updating an element
arr[0] = 10  # Update the first element
print("After Update:", arr)
```

#### Searching (Linear Search)

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return index
    return -1  # Return -1 if not found

arr = [10, 20, 30, 40, 50]
target = 30
print("Index of", target, ":", linear_search(arr, target))
```

#### Sorting (Bubble Sort)

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", bubble_sort(arr))
```

### 2. **Strings**

#### String Reversal

```python
def reverse_string(s):
    return s[::-1]

s = "hello"
print("Reversed string:", reverse_string(s))
```

#### Palindrome Check

```python
def is_palindrome(s):
    return s == s[::-1]

s = "racecar"
print("Is palindrome:", is_palindrome(s))
```

#### Anagram Check

```python
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

s1 = "listen"
s2 = "silent"
print("Are anagrams:", are_anagrams(s1, s2))
```

### 3. **Linked Lists**

#### Singly Linked List Operations (Insert, Delete, Print)

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head
        if temp is not None and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Usage
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.print_list()  # Output: 30 -> 20 -> 10 -> None
ll.delete(20)
ll.print_list()  # Output: 30 -> 10 -> None
```

### 4. **Stacks**

#### Stack Operations (Push, Pop, Peek)

```python
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Top element:", stack.peek())  # Output: 30
print("Popped element:", stack.pop())  # Output: 30
print("Stack size:", stack.size())  # Output: 2
```

#### Parenthesis Matching (Balanced Brackets)

```python
def is_balanced(s):
    stack = []
    matching_brackets = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in matching_brackets.values():
            stack.append(char)
        elif char in matching_brackets.keys():
            if stack == [] or stack[-1] != matching_brackets[char]:
                return False
            stack.pop()
    
    return stack == []

# Usage
s = "{[()()]}"
print("Is balanced:", is_balanced(s))  # Output: True

s = "{[(])}"
print("Is balanced:", is_balanced(s))  # Output: False
```

### 5. **Queues**

#### Basic Queue Operations (Enqueue, Dequeue)

```python
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Front element:", queue.front())  # Output: 10
print("Dequeue:", queue.dequeue())  # Output: 10
print("Queue size:", queue.size())  # Output: 2
```

### 6. **Hashing**

#### Basic Hash Map Operations (Insertion, Search)

```python
# Create a hash map (dictionary in Python)
hash_map = {}

# Insert key-value pairs
hash_map["name"] = "Alice"
hash_map["age"] = 25
hash_map["city"] = "New York"

# Search for a value
print("Name:", hash_map["name"])  # Output: Alice
print("Age:", hash_map["age"])  # Output: 25

# Check if a key exists
if "city" in hash_map:
    print("City:", hash_map["city"])  # Output: New York
```

#### Handling Collisions (Using Chaining)

```python
class HashMap:
    def __init__(self, size):
        self.size = size
        self.map = [[] for _ in range(self.size)]

    def hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash(key)
        for pair in self.map[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.map[index].append([key, value])

    def search(self, key):
        index = self.hash(key)
        for pair in self.map[index]:
            if pair[0] == key:
                return pair[1]
        return None

# Usage
hash_map = HashMap(10)
hash_map.insert("name", "Bob")
hash_map.insert("age", 30)
print("Name:", hash_map.search("name"))  # Output: Bob
```

### 7. **Sorting Algorithms**

#### Quick Sort

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr = [3, 6, 8, 10, 1, 2, 1]
print("Sorted array:", quick_sort(arr))
```

---

These are Python code implementations for various **easy DSA topics**. Let me know if you need any further explanations or help with other topics!