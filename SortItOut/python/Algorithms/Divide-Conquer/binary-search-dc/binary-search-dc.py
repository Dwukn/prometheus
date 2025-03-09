import random
import time

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

# Generate a sorted array of 1 million random integers
arr = sorted(random.randint(1, 10**6) for _ in range(10**6))

# Choose a random target value from the array
target = random.choice(arr)

# Start measuring time
start_time = time.time()

# Perform binary search
result = binary_search(arr, target)

# Stop measuring time
end_time = time.time()

# Output the result and execution time
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found")

t_time = end_time - start_time
# Print the execution time
print(f"Execution Time: {t_time:.8f} seconds")

