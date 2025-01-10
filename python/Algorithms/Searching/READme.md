# Searching Algorithms in Python

This section of the repository focuses on various searching algorithms implemented in Python. Searching algorithms are fundamental for efficiently finding data in a collection. Below are the most common searching algorithms, explained with examples and Python code.

---

## Table of Contents

1. [Linear Search](#linear-search)
2. [Binary Search](#binary-search)
3. [Interpolation Search](#interpolation-search)
4. [Exponential Search](#exponential-search)
5. [Jump Search](#jump-search)

---

## 1. Linear Search

### Description:
Linear Search is the simplest search algorithm. It checks each element of a list or array one by one until it finds the target or reaches the end.

### Time Complexity:
- Best: O(1)
- Average: O(n)
- Worst: O(n)

### Python Code:

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

### Example:

```python
arr = [10, 20, 30, 40, 50]
target = 30
result = linear_search(arr, target)
print(f'Target found at index: {result}')
```

---

## 2. Binary Search

### Description:
Binary Search works on sorted arrays. It repeatedly divides the search interval in half, checking if the target is in the left or right half.

### Time Complexity:
- Best: O(1)
- Average: O(log n)
- Worst: O(log n)

### Python Code:

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

### Example:

```python
arr = [10, 20, 30, 40, 50]
target = 30
result = binary_search(arr, target)
print(f'Target found at index: {result}')
```

---

## 3. Interpolation Search

### Description:
Interpolation Search is an improved version of Binary Search. It works on sorted arrays and tries to estimate the position of the target using a formula, making it more efficient when the elements are uniformly distributed.

### Time Complexity:
- Best: O(1)
- Average: O(log log n)
- Worst: O(n)

### Python Code:

```python
def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1
        # Estimate position of the target
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1
```

### Example:

```python
arr = [10, 20, 30, 40, 50]
target = 40
result = interpolation_search(arr, target)
print(f'Target found at index: {result}')
```

---

## 4. Exponential Search

### Description:
Exponential Search is useful for large, unbounded arrays. It works by first finding a range where the target may lie using exponential jumps, then applying Binary Search within that range.

### Time Complexity:
- Best: O(1)
- Average: O(log n)
- Worst: O(log n)

### Python Code:

```python
def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    index = 1
    while index < len(arr) and arr[index] <= target:
        index *= 2
    return binary_search(arr[:min(index, len(arr))], target)
```

### Example:

```python
arr = [10, 20, 30, 40, 50]
target = 40
result = exponential_search(arr, target)
print(f'Target found at index: {result}')
```

---

## 5. Jump Search

### Description:
Jump Search works by jumping ahead by fixed steps. Once a block is found that may contain the target, it performs a linear search on that block.

### Time Complexity:
- Best: O(√n)
- Average: O(√n)
- Worst: O(√n)

### Python Code:

```python
import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1
```

### Example:

```python
arr = [10, 20, 30, 40, 50]
target = 30
result = jump_search(arr, target)
print(f'Target found at index: {result}')
```

---

## Conclusion

This section covered several common searching algorithms:

- **Linear Search**: Simple but inefficient for large datasets.
- **Binary Search**: Efficient for sorted arrays.
- **Interpolation Search**: More efficient than binary search for uniformly distributed data.
- **Exponential Search**: Efficient for large or unbounded arrays.
- **Jump Search**: A compromise between Linear and Binary Search.

Feel free to explore the implementations in the Python files and run tests with different inputs to see how the algorithms behave!
