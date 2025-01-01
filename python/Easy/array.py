arr=[1,2,3,4,5,6,7,7,8,9,99,1,120,]
print(arr) # prints the entire array
print(arr[0]) # print first element
print(arr[-1]) # prints last element

# Updating elements
arr.append(6) # adds element at lat of array
print(arr)

arr.insert(0,1) # inserts at location
print(arr)

arr.remove(3) # remove first occurance
print(arr)

arr.pop(2)
print(arr)

del arr[0] # remove element at index 0
print(arr)

print(len(arr)) # gives length of array

print(arr.clear()) # removes all element in array

arr1=[1,2,3,4,5,6,7,7,8,9,9,9,99,1,120,]
print(arr1)
# COMMON Operaions
print(4 in arr1) # returns boolean
print(arr1.index(99)) # finds position of element in array
print(arr1.count(9)) # counts number of time repeated/occured in array
arr_copy = arr.copy()

# copies the entire array
arr_copy2 = arr[:]
print("fsa",arr_copy2)
print("copy", arr_copy)


# List Comprenhsion
# creates new list with squares of the original
squares_arr1 = [X**2 for X in arr1]
print(squares_arr1)
# creates new list with sorted elements
sorted_arr1 = sorted(squares_arr1)
print(sorted_arr1)

# Multidimensional Arrays
