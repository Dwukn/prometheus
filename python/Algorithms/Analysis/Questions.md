### **Question 1: Analyze the Time Complexity of Linear Search**

**Problem**:  
Consider the following algorithm for linear search:

```python
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
```

**Question**: What is the time complexity of this algorithm in the best case, worst case, and average case?

---

**Solution**:

1. **Best Case**:
   - In the best case, the element `x` is at the very first position (index 0) of the array. The algorithm will find `x` on the first comparison.
   - Time complexity: **O(1)** (constant time)

2. **Worst Case**:
   - In the worst case, the element `x` is either not present in the array or it is at the last index. In this case, the algorithm will traverse the entire array once to determine that `x` is not found.
   - Time complexity: **O(n)**, where `n` is the size of the array.

3. **Average Case**:
   - On average, the algorithm will need to check approximately half of the elements in the array before finding `x` (assuming `x` is equally likely to be anywhere in the array).
   - Time complexity: **O(n)**, because in the average case, the algorithm still needs to check half the elements, which is still proportional to `n`.

---

### **Question 2: Analyze the Time Complexity of Binary Search**

**Problem**:  
Consider the following algorithm for binary search:

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

---

**Solution**:

1. **Best Case**:
   - The best case occurs when the element `x` is at the middle of the array. The algorithm finds the element in the first comparison.
   - Time complexity: **O(1)** (constant time)

2. **Worst Case**:
   - In the worst case, the algorithm will keep halving the search space until it either finds `x` or determines that `x` is not in the array. In the worst case, the search space is reduced logarithmically with each step.
   - Time complexity: **O(log n)**, where `n` is the size of the array. At each step, the search space is halved, which gives a logarithmic growth rate.

3. **Average Case**:
   - On average, the algorithm will halve the search space with each step. The number of steps needed to find `x` or determine that `x` is not in the array is proportional to the logarithm of the array size.
   - Time complexity: **O(log n)**, because the search space is halved with each iteration.

---

### **Question 3: Analyze the Time Complexity of Bubble Sort**

**Problem**:  
Consider the following algorithm for bubble sort:

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

**Question**: What is the time complexity of this algorithm in the best case, worst case, and average case?

---

**Solution**:

1. **Best Case**:
   - In the best case, the array is already sorted. The algorithm will still go through the outer loop and check all the elements, but no swaps will occur.
   - Time complexity: **O(n)**, where `n` is the size of the array. Although the outer loop runs `n` times, the inner loop will not perform any swaps. However, this is often considered **O(n²)** in traditional bubble sort because it does not include an optimization (like checking if the list is already sorted early).
   
2. **Worst Case**:
   - In the worst case, the array is sorted in reverse order, so every element needs to be swapped during every pass of the inner loop.
   - Time complexity: **O(n²)**, where `n` is the size of the array. Both loops will run `n` times, leading to a quadratic time complexity.

3. **Average Case**:
   - In the average case, the algorithm will perform roughly half the number of swaps as the worst case, but still, each pair of elements must be compared in the inner loop for each iteration of the outer loop.
   - Time complexity: **O(n²)**, as the inner loop runs roughly `n/2` comparisons for each of the `n` iterations in the worst case scenario.

---

### **Question 4: Analyze the Space Complexity of Merge Sort**

**Problem**:  
Consider the following algorithm for merge sort:

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

**Question**: What is the space complexity of this algorithm?

---

**Solution**:

1. **Space Complexity**:
   - The primary space used by merge sort is the space for the temporary arrays (`left_half` and `right_half`) created during the recursive calls, as well as the space used for the `result` array during the merging process.
   - At each level of recursion, the input array is divided into two parts, and two temporary arrays are created. Since the input array is halved at each level of recursion, the space complexity for each recursive call adds up to **O(n)** in total.
   - The depth of the recursion tree is **O(log n)**, but the space used at each level is proportional to the size of the input, so the overall space complexity is dominated by the space used for the temporary arrays.

   - Space complexity: **O(n)**.

---

### **Question 5: Analyze the Time Complexity of Quick Sort**

**Problem**:  
Consider the following algorithm for quicksort:

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

**Question**: What is the time complexity of this algorithm in the best case, worst case, and average case?

---

**Solution**:

1. **Best Case**:
   - The best case occurs when the pivot divides the array into two nearly equal halves each time. In this case, the depth of the recursion tree is logarithmic, and each partitioning step processes all elements in linear time.
   - Time complexity: **O(n log n)**, where `n` is the size of the array.

2. **Worst Case**:
   - The worst case occurs when the pivot is the smallest or largest element every time, leading to unbalanced partitions. This results in a recursion tree with a depth of `n`, and each level processes `n` elements.
   - Time complexity: **O(n²)**, because the array is not effectively partitioned and requires quadratic time to sort.

3. **Average Case**:
   - On average, the pivot divides the array into two fairly balanced partitions, resulting in a recursion tree with depth **O(log n)** and a linear amount of work at each level.
   - Time complexity: **O(n log n)**, which is optimal for comparison-based sorting algorithms.

<br>

## **GATE-style** questions on **Analyzing Algorithms**

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
