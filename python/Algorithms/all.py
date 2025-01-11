import math
import time
import random

def jump_search(arr, target):
    arr.sort()  # Sort the array before applying Jump Search
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target, low, high):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(arr, target, mid + 1, high)
        else:
            return binary_search(arr, target, low, mid - 1)
    else:
        return -1

def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    index = 1
    while index < len(arr) and arr[index] <= target:
        index *= 2
    return binary_search(arr, target, index // 2, min(index, len(arr)) - 1)

def main():
    # Generate a randomly filled list of 10 million integers
    arr = random.sample(range(1, 10**7 + 1), 10**7)  # Unique random numbers between 1 and 10 million
    target = random.choice(arr)  # Choose a random target from the array
    # print(arr)
    # Timing Jump Search
    start_time = time.time()
    j = jump_search(arr, target)
    jump_search_time = time.time() - start_time
    print(f"Jump Search: Target {target} found at index {j}")
    print(f"Jump Search took {jump_search_time:.6f} seconds\n")

    # Timing Exponential Search
    start_time = time.time()
    result = exponential_search(arr, target)
    exponential_search_time = time.time() - start_time
    print(f"Exponential Search: Target {target} found at index {result}")
    print(f"Exponential Search took {exponential_search_time:.6f} seconds")

main()
