# Function to rightRotate array
def rotate(a, n, k):
    # If rotation is greater than size of array
    k = k % n  # To handle the case where k > n
    # Slice and rearrange the array to rotate it
    rotated_array = a[-k:] + a[:-k]
    return rotated_array

def main():
    arr = [1, 2, 3, 4, 5, 6, 7]
    print("Array before rotating:", arr)
    k = 3
    n = len(arr)
    rotated_arr = rotate(arr, n, k)
    print("Array after rotating by", k, "positions:", rotated_arr)
    # print(arr[-k:])

if __name__ == "__main__":
    main()
