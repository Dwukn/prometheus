### MergeSort in Python: Code and Explanation

**MergeSort** is a classic divide-and-conquer algorithm that splits an array into smaller subarrays, sorts them, and then merges them back together in sorted order. The key idea is to break down a large problem into smaller subproblems that are easier to solve and combine.

### Python Code for MergeSort

```python
def merge_sort(arr):
    # Base case: if the array has 1 or fewer elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: Divide the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Step 2: Recursively sort both halves
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # Step 3: Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_arr = []
    i = j = 0

    # Step 4: Merge the two sorted arrays
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Step 5: Append any remaining elements
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr

# Example usage:
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
```

### Explanation of MergeSort Algorithm:

1. **Base Case (Stopping Condition)**:
    - The recursion stops when the array has one or fewer elements because an array with one or zero elements is already considered sorted.

2. **Divide**:
    - The array is split into two halves. The middle index is calculated using `mid = len(arr) // 2`.
    - The two subarrays are obtained using:
      - `left = arr[:mid]`: First half of the array.
      - `right = arr[mid:]`: Second half of the array.

3. **Conquer**:
    - Recursively sort the left and right halves. This step ensures that both subarrays will be sorted eventually.
    - The `merge_sort` function is called recursively on both halves of the array.

4. **Merge**:
    - After both subarrays are sorted, they are merged together into a single sorted array.
    - The `merge` function takes two sorted arrays (`left` and `right`) and combines them into a sorted array by comparing their elements one by one.
    - **Merging Process**:
        - Compare the current elements of `left` and `right`. Append the smaller element to the `sorted_arr` list.
        - If one of the subarrays is exhausted, append the remaining elements of the other subarray to `sorted_arr`.
    - This step ensures that the merged array is sorted.

5. **Return**:
    - The final sorted array is returned after all recursive calls are completed and the arrays are merged at each level.

### Time and Space Complexity

- **Time Complexity**:
    - **Best, Worst, and Average Case**: O(n log n) — Regardless of the input, the array is divided into two halves at each level, which takes O(log n) time, and the merging of arrays takes O(n) time at each level.
    - Thus, the total time complexity is O(n log n).

- **Space Complexity**:
    - O(n) — MergeSort requires additional space for temporary arrays during the merging process. The space complexity is proportional to the size of the input array, as the algorithm creates new arrays during each merge step.

### Example Walkthrough

Let's walk through the example: `[10, 7, 8, 9, 1, 5]`

1. **First Call** (`arr = [10, 7, 8, 9, 1, 5]`):
   - The array is divided into two halves:
     - `left = [10, 7, 8]`
     - `right = [9, 1, 5]`

2. **Recursive Calls on Left Half** (`arr = [10, 7, 8]`):
   - Split further:
     - `left = [10]`
     - `right = [7, 8]`
   - Since `[10]` is already sorted, we now sort `[7, 8]`:
     - `left = [7]`, `right = [8]`
     - Merge them into `[7, 8]`.
   - Now merge `[10]` with `[7, 8]` to get `[7, 8, 10]`.

3. **Recursive Calls on Right Half** (`arr = [9, 1, 5]`):
   - Split further:
     - `left = [9]`
     - `right = [1, 5]`
   - Sort `[1, 5]`:
     - `left = [1]`, `right = [5]`
     - Merge them into `[1, 5]`.
   - Now merge `[9]` with `[1, 5]` to get `[1, 5, 9]`.

4. **Final Merge**:
   - Now merge `[7, 8, 10]` and `[1, 5, 9]`:
     - Compare the elements: `1 < 7`, so append `1`.
     - Compare `5 < 7`, so append `5`.
     - Compare `7 < 9`, so append `7`.
     - Compare `8 < 9`, so append `8`.
     - Compare `9 < 10`, so append `9`.
     - Append the remaining `10`.
   - The final sorted array is `[1, 5, 7, 8, 9, 10]`.

### Key Observations:

- **MergeSort is stable**: It maintains the relative order of elements with equal values.
- **MergeSort is consistent**: It always runs in O(n log n) time, which makes it predictable and reliable, especially for large datasets.
- **Space Complexity**: MergeSort requires O(n) extra space for merging, which can be a drawback when working with large arrays, as it requires additional memory.
- **In-place Sorting**: MergeSort is **not** an in-place sorting algorithm, meaning it requires additional space for the merging process.

### Comparison with QuickSort:

| Property          | MergeSort                           | QuickSort                          |
|-------------------|-------------------------------------|-------------------------------------|
| **Time Complexity (Best, Average, Worst Case)** | O(n log n)                         | O(n log n) (best/avg) but O(n²) in the worst case |
| **Space Complexity** | O(n) (due to merging)               | O(log n) (recursive stack space)   |
| **Stable**         | Yes                                 | No                                  |
| **In-place**       | No (requires extra space for merging) | Yes (in-place partitioning)         |
| **Best for**       | Large datasets, when stability is important | Small to medium datasets, arrays   |
| **Merging Cost**   | High (extra space required)         | Low (in-place partitioning)         |
