arr = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 99, 1, 120]
print("Original Array:", arr)  # prints the entire array
print("First Element:", arr[0])  # print first element
print("Last Element:", arr[-1])  # prints last element

# Updating elements
arr.append(6)  # adds element at the end of the array
print("Array after appending 6:", arr)

arr.insert(0, 1)  # inserts 1 at the beginning
print("Array after inserting 1 at the beginning:", arr)

arr.remove(3)  # removes first occurrence of 3
print("Array after removing 3:", arr)

arr.pop(2)  # removes element at index 2
print("Array after popping element at index 2:", arr)

del arr[0]  # removes element at index 0
print("Array after deleting the first element:", arr)

print("Length of Array:", len(arr))  # gives the length of the array

arr.clear()  # removes all elements in the array
print("Array after clearing all elements:", arr)

# Second Array
arr1 = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 9, 9, 99, 1, 120]
print("\nSecond Array (arr1):", arr1)

# COMMON Operations
print("Is 4 in arr1?", 4 in arr1)  # returns boolean
print("Index of 99 in arr1:", arr1.index(99))  # finds position of element in array
print("Count of 9 in arr1:", arr1.count(9))  # counts number of times 9 is repeated in array

arr_copy = arr1.copy()  # creates a copy of arr1
arr_copy2 = arr1[:]  # another way to copy the array
print("Array Copy (using copy()):", arr_copy)
print("Array Copy (using slicing):", arr_copy2)

# List Comprehension
# Creates a new list with squares of the original
squares_arr1 = [X**2 for X in arr1]
print("Squared Elements of arr1:", squares_arr1)

# Creates a new list with sorted elements
sorted_arr1 = sorted(squares_arr1)
print("Sorted Squares of arr1:", sorted_arr1)

# Multidimensional Arrays

# Create a 2D array (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print the entire matrix
print("\nOriginal Matrix:")
for row in matrix:
    print(row)

# Accessing elements:
print("\nAccessing elements:")
print("Element at row 1, column 2:", matrix[0][1])  # 2 (row 1, column 2)
print("Element at row 2, column 3:", matrix[1][2])  # 6 (row 2, column 3)
print("Element at row 3, column 1:", matrix[2][0])  # 7 (row 3, column 1)

# Modify elements
print("\nModifying elements:")
matrix[0][0] = 10  # Changing the element at row 1, column 1
matrix[1][2] = 15  # Changing the element at row 2, column 3
print("Modified Matrix:")
for row in matrix:
    print(row)

# Add a new row
matrix.append([10, 11, 12])
print("\nMatrix after appending a new row:")
for row in matrix:
    print(row)

# Add a new column (this requires modifying each row individually)
for row in matrix:
    row.append(0)  # Adds '0' to each row as a new column
print("\nMatrix after adding a new column:")
for row in matrix:
    print(row)

# Matrix Traversal (iterating through the rows and columns)
print("\nTraversing through matrix:")
for i in range(len(matrix)):  # Traverse rows
    for j in range(len(matrix[i])):  # Traverse columns
        print(f"Element at ({i+1}, {j+1}): {matrix[i][j]}")

# A 3D array (list of lists of lists)
three_d_array = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]

# Accessing elements in a 3D array
print("\n3D Array Element Access:")
print("Element at [0][1][1]:", three_d_array[0][1][1])  # 4
print("Element at [1][0][0]:", three_d_array[1][0][0])  # 5
