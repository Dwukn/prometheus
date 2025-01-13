### QuickSort in Python: Code and Explanation

QuickSort is a comparison-based, divide-and-conquer algorithm used for sorting arrays. The basic idea of QuickSort is to pick a pivot element from the array, partition the array into two subarrays such that elements less than the pivot go to one subarray and elements greater than the pivot go to the other, and then recursively sort the two subarrays.

### Python Code for QuickSort

```python
def quicksort(arr):
    # Base case: if the array has 0 or 1 element, it's already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: Choose a pivot (we're choosing the first element here)
    pivot = arr[0]

    # Step 2: Partition the array into two subarrays
    # Left subarray: elements less than or equal to pivot
    # Right subarray: elements greater than pivot
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    # Step 3: Recursively apply QuickSort on the left and right subarrays
    # Combine the sorted left, pivot, and sorted right subarrays
    return quicksort(left) + [pivot] + quicksort(right)

# Example usage:
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)
```

### Explanation of QuickSort Algorithm:

1. **Base Case (Stopping Condition)**:
    - The recursion terminates when the input array has 0 or 1 element, because an array with one or zero elements is trivially sorted.

2. **Choosing a Pivot**:
    - A pivot element is selected from the array. In this implementation, the pivot is chosen as the first element (`arr[0]`).
    - The choice of pivot can greatly affect the performance of QuickSort. A good pivot should ideally divide the array into two approximately equal halves. Common pivot strategies include:
        - First element (as done here)
        - Last element
        - Random element
        - Median of three (first, middle, and last element)

3. **Partitioning**:
    - The array is split into two subarrays:
      - **Left subarray**: Contains elements that are less than or equal to the pivot.
      - **Right subarray**: Contains elements that are greater than the pivot.
    - This partitioning step is performed using list comprehensions:
        - `left = [x for x in arr[1:] if x <= pivot]`: Filters out elements less than or equal to the pivot.
        - `right = [x for x in arr[1:] if x > pivot]`: Filters out elements greater than the pivot.
    - The pivot is not included in the subarrays because it will be placed back in its final sorted position after sorting the subarrays.

4. **Recursion**:
    - The `quicksort` function is then called recursively on both the left and right subarrays.
    - This process repeats until the subarrays are of size 1 or 0, at which point they are naturally sorted.

5. **Combine**:
    - The final step involves combining the sorted subarrays and the pivot to form the sorted array. The left subarray is sorted recursively, then the pivot is placed between the left and right subarrays, and the right subarray is sorted recursively.

### Time and Space Complexity

- **Time Complexity**:
    - **Best and Average Case**: O(n log n) — This occurs when the pivot divides the array into approximately two equal subarrays at each level of recursion.
    - **Worst Case**: O(n²) — This happens when the pivot is consistently the smallest or largest element, leading to unbalanced partitions. For example, when the array is already sorted or nearly sorted.
    - The worst-case time complexity can be improved by using random pivot selection or median-of-three pivot selection.

- **Space Complexity**:
    - O(log n) on average for the recursion stack (since each recursive call processes one partition of the array).
    - O(n) in the worst case if the recursion stack is too deep (this happens if the array is already sorted, leading to unbalanced partitions).

### Example Walkthrough

Let's walk through the example: `[10, 7, 8, 9, 1, 5]`

1. **First Call** (`arr = [10, 7, 8, 9, 1, 5]`):
   - Pivot = 10
   - Left subarray: `[7, 8, 9, 1, 5]` (all elements ≤ 10)
   - Right subarray: `[]` (no elements > 10)
   - Recursively sort `[7, 8, 9, 1, 5]`.

2. **Second Call** (`arr = [7, 8, 9, 1, 5]`):
   - Pivot = 7
   - Left subarray: `[1, 5]` (elements ≤ 7)
   - Right subarray: `[8, 9]` (elements > 7)
   - Recursively sort `[1, 5]` and `[8, 9]`.

3. **Third Call** (`arr = [1, 5]`):
   - Pivot = 1
   - Left subarray: `[]` (no elements ≤ 1)
   - Right subarray: `[5]` (elements > 1)
   - Base case: Recursively sorted subarray is `[5]`.

4. **Fourth Call** (`arr = [8, 9]`):
   - Pivot = 8
   - Left subarray: `[]` (no elements ≤ 8)
   - Right subarray: `[9]` (elements > 8)
   - Base case: Recursively sorted subarray is `[9]`.

5. **Recombine**:
   - After sorting all subarrays, we combine the sorted results: `[1, 5] + [7] + [8, 9]` → `[1, 5, 7, 8, 9]`.
   - Finally, the pivot `10` is placed between the sorted left and right subarrays: `[1, 5, 7, 8, 9] + [10] + []` → `[1, 5, 7, 8, 9, 10]`.

### Key Observations:

- QuickSort works efficiently in most cases and is one of the fastest known general-purpose sorting algorithms.
- Its performance can degrade if the pivot selection is poor, leading to unbalanced partitions.
- Choosing a good pivot, such as randomly selecting one or using median-of-three, can help avoid the worst-case time complexity (O(n²)).
