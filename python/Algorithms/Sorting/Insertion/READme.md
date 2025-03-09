### Insertion Sort: Notes

**Insertion Sort** is a simple comparison-based sorting algorithm that builds the final sorted list one element at a time. It is much like sorting a hand of playing cards, where you take one card at a time and insert it into the correct position among the previously sorted cards.

#### How Insertion Sort Works:
1. Start with the second element (since a single-element list is trivially sorted).
2. Compare the current element to the element before it.
3. If the current element is smaller, move the previous element one position to the right.
4. Continue shifting elements to the right until you find the correct position for the current element.
5. Insert the current element in its correct position.
6. Move to the next element and repeat the process until the entire list is sorted.

#### Key Characteristics:
- **Time Complexity**:
  - Best case: \( O(n) \) (when the list is already sorted, as no shifting is needed).
  - Worst case: \( O(n^2) \) (when the list is reverse sorted).
  - Average case: \( O(n^2) \) (when elements are in random order).
- **Space Complexity**:
  - \( O(1) \) (it is an in-place sorting algorithm).
- **Stable**: Yes (it preserves the relative order of equal elements).
- **Adaptivity**: Yes (it adapts well to nearly sorted lists and runs efficiently for them).
- **Online Algorithm**: Yes (it can sort a list as it receives input, meaning elements can be inserted one by one without needing the full list).

### Algorithm:
1. **Iterate** through the array from the second element to the last.
2. **Compare** the current element with the element before it.
3. **Shift** the larger elements to the right to make room for the current element.
4. **Insert** the current element into the correct position in the sorted portion of the list.
5. **Repeat** until the entire list is sorted.

### Example Walkthrough:
Consider sorting the list `[5, 2, 9, 1, 5, 6]` using Insertion Sort:

1. The first element (5) is already "sorted" in its own.
2. Compare 2 with 5; since 2 is smaller, shift 5 to the right and insert 2 at the start.
   - New list: `[2, 5, 9, 1, 5, 6]`
3. Compare 9 with 5; 9 is larger, so no change.
   - List remains: `[2, 5, 9, 1, 5, 6]`
4. Compare 1 with 9, then with 5, then with 2; shift all elements to the right and insert 1 at the start.
   - New list: `[1, 2, 5, 9, 5, 6]`
5. Compare 5 with 9; shift 9 to the right and insert 5 in the correct position.
   - New list: `[1, 2, 5, 5, 9, 6]`
6. Compare 6 with 9; shift 9 to the right and insert 6 in the correct position.
   - Final sorted list: `[1, 2, 5, 5, 6, 9]`

### Python Implementation of Insertion Sort:

```python
def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]  # The current element to be inserted
        j = i - 1
        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Insert the key into its correct position

# Example usage
arr = [5, 2, 9, 1, 5, 6]
insertion_sort(arr)
print("Sorted array:", arr)
```

#### Explanation of the Code:
1. **Outer loop**: Iterates over the array starting from the second element (`i = 1`).
2. **Key**: The element that is currently being inserted into the sorted portion of the array.
3. **Inner loop**: Moves elements of the sorted portion (left of `i`) that are greater than the `key` one position to the right.
4. **Insert the key**: Once the correct position is found (where no more elements are greater than the `key`), the key is placed there.

### Example Run:
For the list `[5, 2, 9, 1, 5, 6]`, after applying Insertion Sort:

**Output:**
```
Sorted array: [1, 2, 5, 5, 6, 9]
```

### Time and Space Complexity:
- **Time Complexity**:
  - **Best case (already sorted)**: \( O(n) \)
  - **Worst case (reverse sorted)**: \( O(n^2) \)
  - **Average case**: \( O(n^2) \)
- **Space Complexity**: \( O(1) \) (since it's an in-place sorting algorithm).

### When to Use:
- Insertion sort is particularly efficient for small datasets or lists that are nearly sorted (already sorted or almost sorted).
- It is also used in hybrid sorting algorithms (like Timsort, which Python uses for its built-in sort function) for small portions of data.

