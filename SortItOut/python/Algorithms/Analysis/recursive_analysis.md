### Notes on **Analysis of Recursive Algorithms**

Recursive algorithms are a powerful way to solve problems by breaking them down into smaller subproblems. However, analyzing their time complexity is essential to understanding their efficiency, as recursion can sometimes lead to exponential time complexity if not properly optimized.

---

### Key Concepts:

1. **Recursion**:
   - A recursive function calls itself, solving smaller instances of the same problem.
   - Each recursive call should move closer to a base case that does not involve further recursion.

2. **Base Case**:
   - The simplest scenario that can be solved without recursion. This terminates the recursive calls.

3. **Recursive Case**:
   - The case where the function calls itself with a smaller or simpler version of the problem.

4. **Time Complexity**:
   - Recursive algorithms often have different time complexities than their iterative counterparts.
   - The time complexity of a recursive function depends on how many times the function calls itself and how much work is done at each call.

---

### **How to Analyze Recursive Algorithms**

To analyze the time complexity of recursive algorithms, we use the following two main techniques:

#### 1. **Recurrence Relation**:
   - A recurrence relation expresses the total time complexity \( T(n) \) of a recursive algorithm in terms of the time complexity of smaller subproblems.
   - For example, a recursive function might solve a problem of size \( n \) by recursively solving two smaller problems of size \( n/2 \) and combining their results.
   
   Example Recurrence Relation:
   \[
   T(n) = 2T(n/2) + O(n)
   \]
   This represents a divide-and-conquer algorithm, where:
   - \( 2T(n/2) \) accounts for the two subproblems, each of size \( n/2 \).
   - \( O(n) \) accounts for the work done to combine the results of the subproblems.

#### 2. **Master Theorem**:
   - The Master Theorem is a direct method for analyzing divide-and-conquer recursions of the form:
     \[
     T(n) = aT(n/b) + O(n^d)
     \]
   - The Master Theorem helps determine the asymptotic complexity by comparing \( a \), \( b \), and \( d \).
     - **Case 1**: If \( a > b^d \), the complexity is \( O(n^{\log_b a}) \).
     - **Case 2**: If \( a = b^d \), the complexity is \( O(n^d \log n) \).
     - **Case 3**: If \( a < b^d \), the complexity is \( O(n^d) \).

---

### **Example 1: Fibonacci Numbers**

Consider the recursive implementation to calculate Fibonacci numbers:

#### Fibonacci Recursive Algorithm:

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

#### Recurrence Relation:
The time complexity can be represented by the recurrence relation:
\[
T(n) = T(n-1) + T(n-2) + O(1)
\]

Since this recursive structure leads to overlapping subproblems (subproblems like \( fibonacci(n-2) \) are solved multiple times), it leads to an **exponential time complexity**.

#### Time Complexity Analysis:
- The recurrence relation leads to an exponential growth of the number of function calls.
- This results in a time complexity of **O(2^n)**.

#### Optimized Version (Memoization or DP):

```python
def fibonacci(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]
```

In this optimized version, we store the results of subproblems to avoid redundant calculations, reducing the time complexity to **O(n)**.

---

### **Example 2: Merge Sort**

Merge Sort is a classic divide-and-conquer algorithm for sorting an array.

#### Merge Sort Algorithm:

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result
```

#### Recurrence Relation:
The time complexity of the merge sort algorithm can be represented by the recurrence relation:
\[
T(n) = 2T(n/2) + O(n)
\]
Where:
- \( 2T(n/2) \) represents the two subarrays being sorted recursively.
- \( O(n) \) represents the merging of the two sorted subarrays.

#### Time Complexity Analysis (Master Theorem):
Using the Master Theorem, we have:
- \( a = 2 \), \( b = 2 \), and \( d = 1 \).
- \( a = b^d \), so according to **Case 2** of the Master Theorem, the time complexity is:
\[
T(n) = O(n \log n)
\]

#### Time Complexity: **O(n log n)**

---

### **Example 3: Binary Search**

Binary Search is a classic example of a divide-and-conquer algorithm that works on sorted arrays.

#### Binary Search Algorithm:

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
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

#### Recurrence Relation:
Binary Search reduces the problem size by half with each recursive call. The recurrence relation for the time complexity is:
\[
T(n) = T(n/2) + O(1)
\]
Where:
- \( T(n/2) \) represents the subproblem of searching the half of the array.
- \( O(1) \) is the time for comparison at each level.

#### Time Complexity Analysis (Master Theorem):
- \( a = 1 \), \( b = 2 \), and \( d = 0 \).
- Since \( a < b^d \), by **Case 3** of the Master Theorem, the time complexity is:
\[
T(n) = O(\log n)
\]

#### Time Complexity: **O(log n)**

---

### **Example 4: Tower of Hanoi**

The Tower of Hanoi is a famous recursive puzzle involving three rods and \( n \) disks. The objective is to move all disks from one rod to another, following a set of rules.

#### Tower of Hanoi Algorithm:

```python
def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, target, source)
```

#### Recurrence Relation:
The time complexity of the Tower of Hanoi problem is given by the recurrence relation:
\[
T(n) = 2T(n-1) + O(1)
\]
Where:
- \( 2T(n-1) \) accounts for solving two subproblems of size \( n-1 \).
- \( O(1) \) accounts for the work done in moving one disk.

#### Time Complexity Analysis (Master Theorem):
- \( a = 2 \), \( b = 2 \), and \( d = 0 \).
- Since \( a = b^d \), by **Case 2** of the Master Theorem, the time complexity is:
\[
T(n) = O(2^n)
\]

#### Time Complexity: **O(2^n)**

---

### **Summary of Common Recursive Algorithms and Their Time Complexities:**

| **Algorithm**         | **Recurrence Relation**         | **Time Complexity**     |
|-----------------------|---------------------------------|-------------------------|
| **Fibonacci (naive)**  | \( T(n) = T(n-1) + T(n-2) + O(1) \) | \( O(2^n) \)           |
| **Merge Sort**         | \( T(n) = 2T(n/2) + O(n) \)    | \( O(n \log n) \)      |
| **Binary Search**      | \( T(n) = T(n/2) + O(1) \)     | \( O(\log n) \)        |
| **Tower of Hanoi**     | \( T(n) = 2T(n-1) + O(1) \)    | \( O(2^n) \)           |

---

### Conclusion:
- **Recursive algorithms** often require analyzing their recurrence relations to understand their time complexity.
- **Master Theorem** provides an efficient way to analyze divide-and-conquer recursions.
- Recursive algorithms can sometimes have exponential time complexity (like Fibonacci and Tower of Hanoi), but they can be optimized with techniques like **memoization** or **dynamic programming** (e.g., for Fibonacci).


