### **Question 1: Time Complexity of Nested Loops**

Consider the following code:

```python
for i in range(n):
    for j in range(i, n):
        for k in range(j, n):
            # Constant time operation
```

**Question**: What is the time complexity of the given code?

**Options**:
- A) O(n)
- B) O(n²)
- C) O(n³)
- D) O(n⁴)

---

**Solution**:

To analyze this, let’s examine the loops individually:
- The outer loop runs `n` times (from 0 to `n-1`).
- The middle loop runs from `i` to `n`, so the number of iterations for the middle loop depends on `i`. In the worst case, when `i = 0`, the middle loop runs `n` times. For `i = 1`, it runs `n-1` times, and so on.
- The innermost loop runs from `j` to `n`, and similarly, the number of iterations depends on `j`.

The total number of operations is the sum of the iterations of all three loops:

\[
\text{Total iterations} = \sum_{i=0}^{n-1} \sum_{j=i}^{n-1} \sum_{k=j}^{n-1} 1
\]

This simplifies to:

\[
\frac{n(n+1)(n+2)}{6}
\]

Thus, the time complexity is **O(n³)**.

**Answer**: **C) O(n³)**

---

### **Question 2: Time Complexity of Recursive Function**

Consider the following recursive function:

```python
def recursive_function(n):
    if n <= 1:
        return 1
    else:
        return recursive_function(n // 2) + recursive_function(n // 2) + n
```

**Question**: What is the time complexity of the recursive function?

**Options**:
- A) O(n)
- B) O(n log n)
- C) O(2^n)
- D) O(n²)

---

**Solution**:

To solve this, let's derive the recurrence relation:

\[
T(n) = 2T(n/2) + n
\]

This is a standard divide-and-conquer recurrence. Using the **Master Theorem** for divide-and-conquer recurrences, we compare this with the recurrence of the form:

\[
T(n) = aT(n/b) + O(n^d)
\]

Here, \(a = 2\), \(b = 2\), and \(d = 1\).

Now, compare \(a\) and \(b^d\):
- \(a = 2\)
- \(b^d = 2^1 = 2\)

Since \(a = b^d\), the time complexity is:

\[
T(n) = O(n^d \log n) = O(n \log n)
\]

**Answer**: **B) O(n log n)**

---

### **Question 3: Space Complexity of Merge Sort**

Consider the following implementation of **merge sort**:

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

**Question**: What is the space complexity of the merge sort algorithm?

**Options**:
- A) O(n)
- B) O(n log n)
- C) O(log n)
- D) O(1)

---

**Solution**:

- Merge sort is a divide-and-conquer algorithm that recursively splits the array into two halves.
- At each recursive step, it requires space to store two halves (left and right), along with the merged array.
- Since the space for the left and right halves is proportional to the size of the input, the space complexity is dominated by the storage required for the merged array.

Thus, the space complexity is **O(n)** because, at each level of recursion, we need extra space to merge the arrays.

**Answer**: **A) O(n)**

---

### **Question 4: Time Complexity of Binary Search**

Consider the following algorithm for **binary search**:

```python
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

**Question**: What is the time complexity of this algorithm?

**Options**:
- A) O(n)
- B) O(log n)
- C) O(n log n)
- D) O(1)

---

**Solution**:

Binary search divides the search space in half at each step. At each step, the number of elements to search through is halved, and the algorithm continues until the element is found or the search space is empty.

Thus, the time complexity of binary search is **O(log n)**, where `n` is the size of the array.

**Answer**: **B) O(log n)**

---

### **Question 5: Worst-Case Time Complexity of Quick Sort**

Consider the following implementation of **Quick Sort**:

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

**Question**: What is the worst-case time complexity of this algorithm?

**Options**:
- A) O(n log n)
- B) O(n²)
- C) O(n³)
- D) O(log n)

---

**Solution**:

In the worst case, the pivot divides the array into two unbalanced partitions (e.g., when the pivot is always the smallest or largest element). This results in a recursion tree with a depth of `n`, where each level processes all `n` elements.

Thus, the worst-case time complexity of quicksort is **O(n²)**.

**Answer**: **B) O(n²)**

---

### **Question 6: Best-Case Time Complexity of Merge Sort**

Consider the merge sort algorithm given above.

**Question**: What is the best-case time complexity of merge sort?

**Options**:
- A) O(n)
- B) O(n log n)
- C) O(n²)
- D) O(log n)

---

**Solution**:

In the case of merge sort, the best case happens when the array is already sorted. However, merge sort still has to divide the array and merge the subarrays regardless of whether they are sorted or not. Each merge step takes linear time, and the depth of recursion is logarithmic.

Thus, the best-case time complexity of merge sort is **O(n log n)**.

**Answer**: **B) O(n log n)**

---

### **Question 7: Space Complexity of Quick Sort**

Consider the following implementation of **Quick Sort**:

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

**Question**: What is the space complexity of this algorithm?

**Options**:
- A) O(n)
- B) O(n log n)
- C) O(log n)
- D) O(1)

---

**Solution**:

In this implementation of quicksort, new arrays (`left`, `middle`, and `right`) are created at each recursive call. Each recursive call requires additional space for these arrays. The recursion depth is logarithmic, but since arrays are created at each level, the space complexity is **O(n)**.

**Answer**: **A) O(n)**

---

### **Conclusion**

These questions cover a variety of topics related to algorithm analysis that you might encounter in the **GATE exam**. The questions test your understanding of **time complexity**, **space complexity**, and **recurrence relations**. Practice solving these types of problems to strengthen your ability to analyze and evaluate algorithms effectively in the exam.
