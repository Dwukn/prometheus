import time
import random

def insertion(arr):
    for i in range(1, len(arr)): # Start from second element
        current = arr[i] # Elemnt to be inserted
        j = i- 1 # start comparing with element before it
        # Shift elements of sorted portion that are greater to right
        while j >= 0 and arr[j] > current :
            arr[j+1] = arr[j] # Shift elem to right
            j -= 1 # move to previos
        arr[j + 1] = current # insert current element in position

def main():
    arr = random.sample(range(1, 10**4+1), 10**4)
    sort_time = time.time()
    insertion(arr)
    end_sort = time.time() - sort_time
    print(arr)
    print(f"time taken: {end_sort}")

if __name__ == "__main__":
    main()
