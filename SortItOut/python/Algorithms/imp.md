The reason **Exponential Search** is much faster than **Jump Search** in your case can be attributed to the following factors:

### 1. **Exponential Search is a Divide-and-Conquer Approach**:
   - Exponential Search works by first finding the range in which the target might exist (by doubling the index), then using **Binary Search** to narrow down the target's position. Binary Search works very efficiently in sorted arrays, having a time complexity of **O(log n)**.
   - **Exponential Search** can locate the target's range in **O(log n)** time and then performs a binary search within that range, which is also **O(log n)**.
   - The key here is that both the **Exponential Search** and **Binary Search** leverage the logarithmic time complexity, which is very efficient even on large arrays like the one you are working with.

### 2. **Jump Search** has **Higher Time Complexity**:
   - **Jump Search**, in contrast, works by jumping in increments of `sqrt(n)` to find a block in which the target might exist. After identifying this block, it performs a linear search within that block, which takes **O(sqrt(n))** time.
   - While Jump Search is faster than a linear search, it is not as efficient as **Binary Search** in sorted arrays. The time complexity of **Jump Search** is **O(sqrt(n))**, which is significantly slower than the **O(log n)** time complexity of Exponential Search, especially when dealing with very large arrays.

### 3. **Effect of Sorting**:
   - Both algorithms assume the array is sorted, but since **Exponential Search** uses Binary Search after finding the correct range, it is much more optimized for this scenario.
   - **Jump Search**, on the other hand, jumps through fixed intervals and then does a linear search within the block, which can take more time due to its larger search space.

### 4. **Implementation Details**:
   - The exponential search's binary search component works very efficiently because the search space is reduced rapidly (due to the doubling index). Each time, you halve the search space until the target is found, which contributes to its low time complexity.
   - **Jump Search**, on the other hand, divides the array into blocks but does a linear search within those blocks, which can make it slower as the number of elements increases, especially in large arrays like the one you're using.

### Example Time Complexities:
1. **Exponential Search**:
   - **Finding the range**: Takes **O(log n)** time.
   - **Binary Search within the range**: Takes **O(log n)** time.
   - Total time complexity: **O(log n)**.

2. **Jump Search**:
   - **Jumping through blocks**: Takes **O(sqrt(n))** time.
   - **Linear search within a block**: Takes **O(sqrt(n))** time.
   - Total time complexity: **O(sqrt(n))**.

### Why Exponential Search is Faster in This Case:
- For large arrays (like the 10 million elements you're using), **O(log n)** is significantly faster than **O(sqrt(n))**.
- Exponential Search can quickly identify the range where the target is located and narrow the search space with binary search, making it much faster in practice for large datasets.

### Summary:
- **Exponential Search** is faster because it leverages the power of **Binary Search** and works with a logarithmic time complexity, while **Jump Search** has a larger search space and performs less efficiently on large datasets.
- **Exponential Search**'s time complexity of **O(log n)** is far more optimal than Jump Search's **O(sqrt(n))**, especially when working with large arrays like the one you're using.
