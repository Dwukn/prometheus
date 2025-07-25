# Practice problem for ARRAYS

### **1. Find the Maximum Subarray Sum (Kadane's Algorithm)**
Given an array of integers, find the sum of the contiguous subarray that has the largest sum. The subarray must contain at least one element.

**Input:**
```python
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
```

**Output:**
```python
6
```

**Explanation:**
The subarray `[4, -1, 2, 1]` has the largest sum, which is `6`.

---

### **2. Rotate an Array**
You are given an array and a number `k`. Write a function to rotate the array `k` times to the right.

**Input:**
```python
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
```

**Output:**
```python
[5, 6, 7, 1, 2, 3, 4]
```

---

### **3. Find the Duplicate Number**
Given an array of integers, find the one duplicate number in it. The array contains `n + 1` integers where each integer is between `1` and `n` (inclusive). There is only one duplicate number, but it may appear more than once.

**Input:**
```python
arr = [3, 1, 3, 4, 2]
```

**Output:**
```python
3
```

---

### **4. Move Zeros to the End**
Given an array, move all the zeros to the end of the array without changing the relative order of non-zero elements.

**Input:**
```python
arr = [0, 1, 2, 0, 4, 5, 0]
```

**Output:**
```python
[1, 2, 4, 5, 0, 0, 0]
```

---

### **5. Merge Two Sorted Arrays**
You are given two sorted arrays `arr1` and `arr2`. Merge them into a single sorted array.

**Input:**
```python
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
```

**Output:**
```python
[1, 2, 3, 4, 5, 6, 7, 8]
```

---

### **6. Find Missing Number**
Given an array of size `n` containing numbers from `1` to `n+1`, find the number that is missing.

**Input:**
```python
arr = [1, 2, 4, 5, 6]
```

**Output:**
```python
3
```

---

### **7. Longest Consecutive Sequence**
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

**Input:**
```python
arr = [100, 4, 200, 1, 3, 2]
```

**Output:**
```python
4
```

**Explanation:**
The longest consecutive sequence is `[1, 2, 3, 4]`, so the output is `4`.

---

### **8. Subarray with Given Sum**
Given an array of integers and a number `s`, find a subarray of contiguous elements that sum up to `s`. If no such subarray exists, return `None`.

**Input:**
```python
arr = [1, 4, 20, 3, 10, 5]
s = 33
```

**Output:**
```python
[20, 3, 10]
```

---

### **9. Find Pair with Given Sum**
Given an array of integers and a target sum `k`, find if there are two numbers in the array whose sum is equal to `k`.

**Input:**
```python
arr = [10, 2, 3, 5, 7]
k = 12
```

**Output:**
```python
True  # Pair is (5, 7)
```

---

### **10. Array Partition (GATE Level)**
Given an array of integers, partition the array into two subsets such that the sum of elements in both subsets is equal. If possible, return the subsets; otherwise, return `None`.

**Input:**
```python
arr = [1, 5, 11, 5]
```

**Output:**
```python
([1, 5, 5], [11])
```

---

### Bonus Challenge: **Subarray Product Less than K**
Given an array of integers and a number `k`, find the total number of contiguous subarrays whose product is less than `k`.

**Input:**
```python
arr = [10, 5, 2, 6]
k = 100
```

**Output:**
```python
8
```
