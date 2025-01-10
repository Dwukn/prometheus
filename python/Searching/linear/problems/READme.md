# Problems Based on LINEAR SEARCH
### 1. **Find the First Occurrence of an Element in a List**

**Problem:**
Given a list of integers, find the index of the first occurrence of a target element.

**Example:**
```python
arr = [5, 3, 7, 8, 3, 10, 3]
target = 3
```
**Solution:**
Linear search can be used to iterate through the list and return the index of the first occurrence of the target element.

---

### 2. **Check if an Element Exists in a List**

**Problem:**
Given a list of integers, check if a target element is present in the list or not.

**Example:**
```python
arr = [15, 23, 45, 78, 99]
target = 45
```
**Solution:**
You can use Linear Search to iterate over the list and check if the target is present. If found, return `True`; otherwise, return `False`.

---

### 3. **Find the Largest Element in a List**

**Problem:**
Given a list of integers, find the largest element in the list.

**Example:**
```python
arr = [10, 45, 32, 7, 18, 50, 22]
```
**Solution:**
By iterating through the list using Linear Search, we can compare each element with the current largest and update accordingly.

---

### 4. **Find the Index of the Last Occurrence of an Element**

**Problem:**
Given a list of integers, find the index of the last occurrence of a target element.

**Example:**
```python
arr = [1, 2, 3, 4, 2, 5]
target = 2
```
**Solution:**
Using Linear Search, we iterate through the list from the start and keep updating the index of the element if it's found, so the final index will be the last occurrence.

---

### 5. **Find the Position of an Element in an Unsorted List**

**Problem:**
Given an unsorted list, find the position of a target element.

**Example:**
```python
arr = [8, 3, 1, 5, 7]
target = 5
```
**Solution:**
You can use Linear Search to scan each element in the list and return the position (index) of the target element if found.

---

### 6. **Count Occurrences of an Element in a List**

**Problem:**
Given a list, count how many times a target element appears in the list.

**Example:**
```python
arr = [4, 2, 4, 5, 6, 4]
target = 4
```
**Solution:**
Perform a Linear Search, count how many times the target element is found during the traversal of the list.

---

### 7. **Find the First Non-Repeating Character in a String**

**Problem:**
Given a string, find the first non-repeating character.

**Example:**
```python
string = "aabccde"
```
**Solution:**
Linear search can be used to iterate through the string, count the frequency of each character, and find the first character that has a count of 1.

---

### 8. **Find a Specific Element in a List of Objects (e.g., Students or Products)**

**Problem:**
Given a list of objects (e.g., student records, product items), find if a specific object exists based on a given criterion (like name or ID).

**Example:**
```python
students = [{"id": 1, "name": "John"}, {"id": 2, "name": "Alice"}, {"id": 3, "name": "Bob"}]
target_name = "Alice"
```
**Solution:**
You can use Linear Search to compare the `name` field of each student object to find the one that matches the target name.

---

### 9. **Find the Smallest Element in a List**

**Problem:**
Given a list of integers, find the smallest element in the list.

**Example:**
```python
arr = [12, 5, 9, 22, 3, 14]
```
**Solution:**
Using Linear Search, iterate through the list, and keep track of the smallest value encountered during the iteration.

---

### 10. **Check if Two Lists Have Common Elements**

**Problem:**
Given two lists, check if they have any common element.

**Example:**
```python
list1 = [1, 2, 3, 4]
list2 = [5, 6, 3, 7]
```
**Solution:**
You can perform a Linear Search on one list and check if any element in the first list exists in the second list.

---

### 11. **Find the Element That Appears the Most in a List (Mode)**

**Problem:**
Given a list of integers, find the element that appears most frequently (i.e., the mode).

**Example:**
```python
arr = [4, 5, 6, 7, 5, 5, 4, 6, 5]
```
**Solution:**
By iterating through the list and counting occurrences of each element, you can determine the mode using Linear Search.

---

### 12. **Find an Element in a List of Strings**

**Problem:**
Given a list of strings, find if a target string exists in the list.

**Example:**
```python
arr = ["apple", "banana", "grape", "orange"]
target = "banana"
```
**Solution:**
Use Linear Search to go through the list and return the index if the target string exists.

---

### 13. **Find the Element in a List Based on Custom Criteria**

**Problem:**
Given a list of dictionaries (e.g., products), find a product that matches a custom criterion (like price, category, etc.).

**Example:**
```python
products = [{"id": 1, "name": "Shirt", "price": 20}, {"id": 2, "name": "Pants", "price": 30}]
target_price = 30
```
**Solution:**
Iterate through the list of products using Linear Search and compare each product’s price with the target price.

---

### 14. **Validate a List of Numbers to Check for Duplicates**

**Problem:**
Given a list of numbers, check if there are any duplicate numbers in the list.

**Example:**
```python
arr = [2, 3, 5, 7, 2, 9]
```
**Solution:**
Use Linear Search to check for any element that appears more than once. Alternatively, you can use nested linear searches to compare every pair of elements.

---

### 15. **Find the Missing Number in a Consecutive Sequence**

**Problem:**
Given a list of consecutive numbers with one missing, find the missing number.

**Example:**
```python
arr = [1, 2, 4, 5, 6]
```
**Solution:**
By performing a Linear Search, you can identify where the sequence is broken and return the missing number.
