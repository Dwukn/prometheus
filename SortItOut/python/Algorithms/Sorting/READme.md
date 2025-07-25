### Sorting Algorithms

Sorting algorithms are fundamental techniques used to arrange elements in a list or array in a specified order, such as ascending or descending. Here are detailed notes on several sorting algorithms, including simple ones like **Selection Sort**, **Bubble Sort**, and **Insertion Sort**, as well as more advanced **Divide and Conquer** algorithms like **MergeSort** and **QuickSort**.

---

#### 1. **Selection Sort**

**Concept:**
Selection Sort is an in-place, comparison-based sorting algorithm. It works by repeatedly finding the smallest (or largest, depending on sorting order) element from the unsorted portion of the list and swapping it with the leftmost unsorted element.

**Steps:**
1. Start with the first element of the array.
2. Find the minimum element from the unsorted part of the array.
3. Swap the minimum element with the leftmost unsorted element.
4. Repeat the process for the remaining unsorted portion of the array.

**Time Complexity:**
- Best, Average, Worst: O(n²), where `n` is the number of elements in the array.

**Space Complexity:**
- O(1), since it is an in-place algorithm.

**Characteristics:**
- Not stable (the relative order of equal elements might change).
- Simple and easy to implement.
- Inefficient on large lists.

**Example:**
Given array: [64, 25, 12, 22, 11]

1. Find the minimum (11) and swap it with the first element.
   → [11, 25, 12, 22, 64]
2. Find the minimum (12) in the remaining array and swap it with the second element.
   → [11, 12, 25, 22, 64]
3. Find the minimum (22) and swap it with the third element.
   → [11, 12, 22, 25, 64]
4. Continue until the array is sorted.

---

#### 2. **Bubble Sort**

**Concept:**
Bubble Sort is a simple comparison-based sorting algorithm. It works by repeatedly swapping adjacent elements if they are in the wrong order, "bubbling" the largest unsorted element to its correct position in each iteration.

**Steps:**
1. Compare the first element with the next.
2. If the first element is greater, swap them.
3. Continue this for the entire array, causing the largest element to "bubble" to the end of the array.
4. Repeat the process for the remaining unsorted portion of the array.

**Time Complexity:**
- Best: O(n) (when the list is already sorted, optimized version).
- Average, Worst: O(n²).

**Space Complexity:**
- O(1), as it is an in-place algorithm.

**Characteristics:**
- Stable (relative order of equal elements is maintained).
- Inefficient for large datasets.
- Simple but slow on larger arrays.

**Example:**
Given array: [5, 1, 4, 2, 8]

1. First pass: [1, 4, 2, 5, 8]
2. Second pass: [1, 2, 4, 5, 8]
3. Continue until no more swaps are needed.

---

#### 3. **Insertion Sort**

**Concept:**
Insertion Sort builds the sorted portion of the array one element at a time. It takes an element from the unsorted portion and places it in the correct position in the sorted portion.

**Steps:**
1. Start with the second element (first element is considered sorted).
2. Compare it with the elements in the sorted portion and shift elements as needed.
3. Insert the current element in the correct position in the sorted portion.
4. Repeat this process for the remaining elements.

**Time Complexity:**
- Best: O(n) (when the list is already sorted).
- Average, Worst: O(n²).

**Space Complexity:**
- O(1), in-place sorting.

**Characteristics:**
- Stable.
- Efficient for small datasets or nearly sorted data.
- Inefficient for large datasets.

**Example:**
Given array: [5, 1, 4, 2, 8]

1. First pass: [1, 5, 4, 2, 8] (insert 1 in its correct position)
2. Second pass: [1, 4, 5, 2, 8] (insert 4)
3. Continue until sorted.

---

### Divide and Conquer Algorithms

These algorithms break a problem down into smaller subproblems, solve each subproblem independently, and then combine the results to solve the original problem.

---

#### 4. **MergeSort**

**Concept:**
MergeSort is a divide-and-conquer algorithm that divides the array into two halves, recursively sorts each half, and then merges the sorted halves into a single sorted array.

**Steps:**
1. Split the array into two halves.
2. Recursively sort each half using MergeSort.
3. Merge the two sorted halves into one sorted array.

**Time Complexity:**
- Best, Average, Worst: O(n log n).

**Space Complexity:**
- O(n), due to the extra space used in merging.

**Characteristics:**
- Stable.
- Efficient for large datasets.
- Requires extra space for merging.

**Example:**
Given array: [38, 27, 43, 3, 9, 82, 10]

1. Split the array: [38, 27, 43] and [3, 9, 82, 10]
2. Recursively split: [38], [27, 43], and [3, 9], [82, 10]
3. Sort and merge the halves: [27, 38, 43], [3, 9, 10, 82]
4. Final merge: [3, 9, 10, 27, 38, 43, 82]

---

#### 5. **QuickSort**

**Concept:**
QuickSort is a divide-and-conquer algorithm that works by selecting a "pivot" element, partitioning the array into two subarrays (elements less than the pivot and elements greater than the pivot), and recursively sorting each subarray.

**Steps:**
1. Choose a pivot element.
2. Partition the array into two parts: one with elements less than the pivot, and the other with elements greater than the pivot.
3. Recursively sort the subarrays.
4. Combine the sorted subarrays with the pivot in between.

**Time Complexity:**
- Best, Average: O(n log n).
- Worst: O(n²), but this can be mitigated by choosing a good pivot.

**Space Complexity:**
- O(log n) for the recursion stack (if implemented optimally).

**Characteristics:**
- Not stable.
- Very efficient for large datasets.
- In-place, no extra memory required (except for recursion).

**Example:**
Given array: [10, 80, 30, 90, 40, 50, 70]

1. Choose pivot (e.g., 50).
2. Partition the array into: [10, 30, 40] and [80, 90, 70].
3. Recursively sort the subarrays.
4. Final sorted array: [10, 30, 40, 50, 70, 80, 90].

---

### Summary of Comparisons

| Algorithm         | Best Time Complexity | Average Time Complexity | Worst Time Complexity | Space Complexity | Stable |
|-------------------|----------------------|-------------------------|-----------------------|------------------|--------|
| **Selection Sort** | O(n²)                | O(n²)                   | O(n²)                 | O(1)             | No     |
| **Bubble Sort**    | O(n)                 | O(n²)                   | O(n²)                 | O(1)             | Yes    |
| **Insertion Sort** | O(n)                 | O(n²)                   | O(n²)                 | O(1)             | Yes    |
| **MergeSort**      | O(n log n)           | O(n log n)              | O(n log n)            | O(n)             | Yes    |
| **QuickSort**      | O(n log n)           | O(n log n)              | O(n²)                 | O(log n)         | No     |

---

These sorting algorithms vary in their time and space complexity, stability, and performance on different types of data. Simple algorithms like Bubble Sort and Selection Sort are easy to understand and implement, but they are inefficient for large datasets. MergeSort and QuickSort are more efficient for large datasets and are widely used in practice.
