import random
import time

def selection(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]

def main():
    arr_time = time.time()
    # arr = random.sample(range(1, 10**5+1), 10**5) # BAD idea to sort a 100,000 using selection
    arr = random.sample(range(1, 10**4+1), 10**4)
    end_arr = time.time() - arr_time
    start = time.time()
    selection(arr)
    end = time.time() - start
    print("sorted arr:", arr)
    print(f"time to creat: {end_arr:.6f}")
    print(f"Sorting took {end:.6f}")
    print(f"total time: {(end + end_arr):.6f}")

main()
