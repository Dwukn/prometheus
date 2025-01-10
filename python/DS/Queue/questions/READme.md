# QUESTIONS on QUEUE

### Here are some easy, medium, and hard-level questions on **Queues** to help you practice and strengthen your understanding of the data structure:

### **Easy Questions**

1. **Implement a Queue using Two Stacks**
   - **Problem**: Implement a queue using two stacks. You need to implement the following operations:
     - `enqueue(x)` – Adds element `x` to the queue.
     - `dequeue()` – Removes and returns the element from the front of the queue.

   - **Hint**: You can simulate queue behavior by using two stacks, one for enqueue and the other for dequeue.

2. **Reverse First K Elements of Queue**
   - **Problem**: Given a queue and an integer `k`, reverse the first `k` elements of the queue. The other elements should remain in the same order.
   - **Example**:
     - Input: `Queue = [1, 2, 3, 4, 5]`, `k = 3`
     - Output: `[3, 2, 1, 4, 5]`

3. **Check if a Queue is Empty**
   - **Problem**: Write a function to check if a queue is empty.
   - **Input**: A queue (you can implement it using lists or `deque`).
   - **Output**: Return `True` if the queue is empty, otherwise return `False`.

4. **Queue Size**
   - **Problem**: Implement a function to return the size of a queue.
   - **Example**:
     - Input: `Queue = [10, 20, 30]`
     - Output: `3`

---

### **Medium Questions**

1. **First Non-Repeating Character in Stream**
   - **Problem**: Given a stream of characters, implement a queue that returns the first non-repeating character at any point in the stream. If there is no non-repeating character, return `None`.
   - **Example**:
     - Input: `stream = "aabcc"`
     - Output: `"a"` after reading 'a', `"a"` after reading 'a', `b` after reading 'b', `c` after reading 'c'

2. **Circular Queue**
   - **Problem**: Implement a circular queue using an array. It should support the following operations:
     - `enqueue(x)` – Adds element `x` to the queue.
     - `dequeue()` – Removes and returns the front element of the queue.
     - `is_empty()` – Checks if the queue is empty.
     - `is_full()` – Checks if the queue is full.

3. **Generate Binary Numbers from 1 to N**
   - **Problem**: Given an integer `N`, generate all binary numbers from `1` to `N` using a queue.
   - **Example**:
     - Input: `N = 5`
     - Output: `["1", "10", "11", "100", "101"]`

4. **Implement a Queue with Limited Size**
   - **Problem**: Implement a queue with a fixed size and ensure that the `dequeue()` operation doesn't throw an error when the queue is empty. If the queue is full, you should handle overflow by blocking the `enqueue()` operation or dropping elements.
   - **Hint**: You can use a list or a deque to handle this.

---

### **Hard Questions**

1. **Sliding Window Maximum**
   - **Problem**: Given an array of integers and a window size `k`, find the maximum element in every sliding window of size `k` as it moves from left to right.
   - **Example**:
     - Input: `arr = [1, 3, -1, -3, 5, 3, 6, 7]`, `k = 3`
     - Output: `[3, 3, 5, 5, 6, 7]`

   - **Hint**: Use a deque to keep track of elements in the current window.

2. **Implement Priority Queue**
   - **Problem**: Implement a **priority queue** using a queue data structure. The priority queue should support:
     - `enqueue(x, priority)` – Adds an element `x` with a given `priority`.
     - `dequeue()` – Removes and returns the element with the highest priority.
     - Elements with higher priority should be dequeued first.

   - **Hint**: Use a deque to store elements along with their priorities.

3. **Task Scheduling with Queue**
   - **Problem**: You are given a list of tasks, where each task is represented by a tuple of (task_id, duration). Implement a queue that simulates task scheduling. The scheduler will process tasks in a FIFO order, but tasks can have different durations. If there are multiple tasks with the same duration, they are processed in the order they were added.
   - **Example**:
     - Input: `tasks = [(1, 4), (2, 3), (3, 2), (4, 1)]`
     - Output: Process tasks in the order of their durations and print them: `[(4, 1), (3, 2), (2, 3), (1, 4)]`.

4. **Design a Queue with Efficient `GetRandom` Operation**
   - **Problem**: Implement a queue with an efficient `get_random()` function that returns a random element from the queue in constant time, while still supporting enqueue and dequeue operations in constant time.
   - **Hint**: You can use an additional data structure, such as a list, to store the elements in the queue.

---

### **Conclusion**
These questions cover a range of difficulty levels and will help you practice different aspects of the **Queue** data structure. Start with the easy ones to get a good grasp of the basic operations, and gradually work your way up to the harder problems. Let me know if you'd like detailed solutions for any of these problems!
