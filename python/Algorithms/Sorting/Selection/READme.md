### Selection Sort: Notes

**Selection Sort** is a simple comparison-based sorting algorithm. It works by repeatedly finding the minimum (or maximum) element from the unsorted part of the list and swapping it with the element at the current position. The algorithm continues to shrink the unsorted section of the list until the entire list is sorted.

#### Steps in Selection Sort:
1. **Start from the first element** of the list.
2. **Find the smallest element** in the remaining unsorted part of the list.
3. **Swap** the smallest element with the element at the current position.
4. **Move the boundary** of the unsorted part one element to the right.
5. Repeat steps 2-4 until the entire list is sorted.

#### Characteristics:
- **Time Complexity**:
  - Best, Worst, and Average: \( O(n^2) \) (since we have two nested loops: one to traverse the list and one to find the minimum element)
- **Space Complexity**:
  - \( O(1) \) (in-place sorting)
- **Stable**: Not stable (does not preserve the relative order of equal elements)
- **Adaptivity**: Not adaptive (it always runs in \( O(n^2) \) time, regardless of the input)

### Implementation of Selection Sort in Python:

```python
def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the element at index i
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array:", arr)
```

#### Explanation of the Python code:
1. We iterate through each element in the list using the index `i`.
2. For each index `i`, we find the smallest element in the unsorted part of the list (from index `i` to the end of the list).
3. Once the minimum element is found, we swap it with the element at index `i`.
4. This continues until the list is sorted.

#### Example Run:
For the list `[64, 25, 12, 22, 11]`, after applying selection sort:
1. The first iteration finds the minimum element `11` and swaps it with `64`.
2. In the second iteration, it finds the minimum element `12` and swaps it with `25`.
3. The third iteration finds `22` and swaps it with `25`.
4. Finally, the list is sorted.

**Output:**
```
Sorted array: [11, 12, 22, 25, 64]
```

This implementation has the following behavior:
- **Time Complexity**: \( O(n^2) \) because there are two loops: one for each element and the inner loop to find the minimum.
- **Space Complexity**: \( O(1) \) as the sorting is done in place.

