import time
import random

def insertion(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i- 1
        while j >= 0 and arr[j] > key :
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main():
    arr = random.sample(range(1, 10**4+1), 10**4)
    sort_time = time.time()
    insertion(arr)
    end_sort = time.time() - sort_time
    print(arr)
    print(f"time taken: {end_sort}")

if __name__ == "__main__":
    main()
