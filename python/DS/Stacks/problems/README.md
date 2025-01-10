# STACK Practice Questions
### **Basic Stack Questions**:

1. **Implement a Stack Using Arrays**
   Implement a stack using a list/array in Python. Provide functions for:
   - `push()`: Push an element onto the stack.
   - `pop()`: Remove and return the top element from the stack.
   - `peek()`: Return the top element without removing it.
   - `isEmpty()`: Return `True` if the stack is empty.
   - `size()`: Return the number of elements in the stack.

2. **Balanced Parentheses**
   Given a string containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine if the input string is valid. An input string is valid if:
   - The brackets must close in the correct order.
   - Every opening bracket must have a corresponding closing bracket.
   ```python
   def is_balanced(expression: str) -> bool:
       pass
   ```

3. **Reverse a Stack**
   Implement a function that reverses a stack using recursion. Do not use any extra data structures except for recursion.
   ```python
   def reverse_stack(stack: List[int]) -> None:
       pass
   ```

---

### **Intermediate Stack Questions**:

4. **Implement a Min Stack**
   Design a stack that supports the following operations:
   - `push(x)`: Push an element onto the stack.
   - `pop()`: Removes the top element from the stack.
   - `top()`: Get the top element.
   - `getMin()`: Retrieve the minimum element in the stack.

   You need to implement the `getMin()` function in **O(1)** time complexity.
   ```python
   class MinStack:
       def __init__(self):
           pass
       def push(self, x: int) -> None:
           pass
       def pop(self) -> None:
           pass
       def top(self) -> int:
           pass
       def getMin(self) -> int:
           pass
   ```

5. **Evaluate Postfix Expression**
   Given a postfix expression (in the form of a list or string), evaluate it and return the result. Operators include `+`, `-`, `*`, `/`, and the operands are integers.
   Example: `"2 3 + 5 *"` → Output: `25`
   ```python
   def evaluate_postfix(expression: str) -> int:
       pass
   ```

6. **Next Greater Element**
   Given an array of integers, for each element, find the next greater element that comes after it. If no such element exists, return `-1`. Solve it using a stack.
   Example: `[4, 5, 2, 10, 8]` → Output: `[5, 10, 10, -1, -1]`
   ```python
   def next_greater_element(arr: List[int]) -> List[int]:
       pass
   ```

---

### **Advanced Stack Questions**:

7. **Implement a Queue Using Two Stacks**
   Implement a queue using two stacks. The queue should support the following operations:
   - `enqueue(x)`: Adds an element to the queue.
   - `dequeue()`: Removes the front element from the queue.

   The `enqueue` and `dequeue` operations should both be **O(1)**, and `dequeue` should be amortized over time.

8. **Stock Span Problem**
   Given an array of stock prices, find the span of each stock's price. The span of a stock price `price[i]` is defined as the maximum number of consecutive days (starting from the current day) the stock price has been less than or equal to `price[i]`.
   Example: `[100, 80, 60, 70, 60, 75, 85]` → Output: `[1, 1, 1, 2, 1, 4, 6]`
   ```python
   def calculate_span(prices: List[int]) -> List[int]:
       pass
   ```

9. **Daily Temperature**
   Given a list of temperatures, return a list of the number of days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put `0` instead.
   Example: `[73, 74, 75, 71, 69, 72, 76, 73]` → Output: `[1, 1, 4, 2, 1, 1, 0, 0]`
   ```python
   def daily_temperatures(temperatures: List[int]) -> List[int]:
       pass
   ```

10. **Remove Duplicate Letters**
    Given a string containing letters, remove duplicate letters so that every letter appears once and only once, while maintaining the lexicographical order.
    Example: `"bcabc"` → Output: `"abc"`
    ```python
    def remove_duplicate_letters(s: str) -> str:
        pass
    ```

---

### **Challenging Stack Questions**:

11. **Maximum Rectangle Area in Histogram**
    Given an array of integers representing the heights of bars in a histogram, find the area of the largest rectangle that can be formed by a contiguous set of bars. Solve it using a stack.
    Example: `[2, 1, 5, 6, 2, 3]` → Output: `10`
    ```python
    def largestRectangleArea(heights: List[int]) -> int:
        pass
    ```

12. **Trapping Rain Water**
    Given an array of non-negative integers representing the height of walls, compute how much water it can trap after raining.
    Example: `[0,1,0,2,1,0,1,3,2,1,2,1]` → Output: `6`
    ```python
    def trap(heights: List[int]) -> int:
        pass
    ```

13. **Largest Rectangle in a Binary Matrix**
    Given a binary matrix, find the area of the largest rectangle containing only 1's. Solve this problem using stacks.
    Example:
    ```
    Input:
    [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0]
    ]
    Output: 6
    ```
    ```python
    def maximalRectangle(matrix: List[List[int]]) -> int:
        pass
    ```

---

### **How to Approach These Problems**:

1. **Understand the Problem**: Make sure to thoroughly understand the problem statement and any edge cases.
2. **Plan**: Consider how stacks can be used. For example, for problems involving finding the next greater element, you will typically maintain a stack to store indices or elements while traversing.
3. **Implement**: Write clean code that performs the stack operations efficiently.
4. **Test**: Run the code with a variety of test cases, including edge cases such as empty stacks, large inputs, or cases with no valid output.
