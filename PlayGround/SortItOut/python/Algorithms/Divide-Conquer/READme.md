### Divide and Conquer

**Divide and Conquer** is an algorithm design paradigm based on breaking a problem down into smaller subproblems, solving them recursively, and then combining the results to solve the original problem. It typically involves three steps:

1. **Divide**: Split the problem into smaller subproblems that are easier to solve.
2. **Conquer**: Solve the subproblems recursively (base cases are handled directly).
3. **Combine**: Merge the solutions to the subproblems to form the solution to the original problem.

### 1. MergeSort

**MergeSort** is a classic divide-and-conquer algorithm used for sorting an array or a list. It works by recursively dividing the input array into two halves until each subarray contains a single element (base case), and then merging the sorted subarrays back together.

#### Steps:
1. **Divide**: Split the input array into two halves.
2. **Conquer**: Recursively sort each half.
3. **Combine**: Merge the sorted halves to produce the sorted array.

#### Time Complexity:
- **Best, Worst, and Average Case**: O(n log n) — This is because the array is split in half each time (log n levels), and at each level, we merge n elements.
- **Space Complexity**: O(n) — Additional space is required for the temporary arrays during merging.

#### Advantages:
- Stable sort (maintains the relative order of equal elements).
- Works well for large datasets and linked lists.

#### Disadvantages:
- Requires extra space (O(n)) for merging.
- Slower for small datasets compared to simpler algorithms like Insertion Sort.

#### Pseudocode:
```python
def MergeSort(arr):
  if length of arr > 1:
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    MergeSort(left)
    MergeSort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
```

---

### 2. QuickSort

**QuickSort** is another divide-and-conquer sorting algorithm, but it uses a different strategy: it selects a "pivot" element from the array, partitions the other elements into two subarrays (elements less than the pivot, and elements greater than the pivot), and recursively sorts the subarrays.

#### Steps:
1. **Divide**: Choose a pivot element from the array.
2. **Conquer**: Partition the array into two subarrays: one with elements smaller than the pivot, the other with elements greater than the pivot.
3. **Combine**: Recursively sort the subarrays and combine them (no actual merging is required; the array is sorted in place).

#### Time Complexity:
- **Best and Average Case**: O(n log n) — This occurs when the pivot divides the array into two balanced halves.
- **Worst Case**: O(n^2) — This occurs when the pivot selection results in highly unbalanced partitions, such as choosing the smallest or largest element as the pivot.

#### Space Complexity:
- O(log n) on average (due to recursion stack), but in the worst case, it could be O(n) if the array is unbalanced.

#### Advantages:
- In-place sorting (no extra space required).
- Faster than MergeSort in practice for most datasets, due to better cache performance and fewer data movements.

#### Disadvantages:
- Worst-case performance can be O(n^2), but this can be mitigated with techniques like random pivot selection or the median-of-three rule.
- Not stable (relative order of equal elements may not be preserved).

#### Pseudocode:
```python
def QuickSort(arr):
  if len(arr) <= 1:
    return arr
  pivot = arr[0]
  less = [x for x in arr[1:] if x <= pivot]
  greater = [x for x in arr[1:] if x > pivot]

  return QuickSort(less) + [pivot] + QuickSort(greater)
```

### Comparison:

| Property         | MergeSort                          | QuickSort                        |
|------------------|------------------------------------|----------------------------------|
| **Time Complexity (Avg)** | O(n log n)                       | O(n log n)                       |
| **Time Complexity (Worst)** | O(n log n)                       | O(n²)                            |
| **Space Complexity** | O(n) (due to merging)              | O(log n) (due to recursion)      |
| **Stable**        | Yes                                | No                               |
| **In-place**      | No (requires extra space)          | Yes                              |
| **Best for**      | Large datasets, linked lists       | Small to medium datasets, arrays |
| **Merging Cost**  | High (extra space for merging)     | Low (in-place partitioning)      |
