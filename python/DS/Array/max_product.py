def max_index_product(arr):
    max_product = float('-inf')  # Initialize the maximum product to a very small number
    n = len(arr)

    # Loop over all distinct pairs of indices (i, j)
    for i in range(n):
        for j in range(i + 1, n):
            # Calculate the product as per the formula
            product = arr[i] * arr[j] * i * j
            if product > max_product:
                max_product = product  # Update max_product if a larger product is found

    return max_product

def main():
    size_arr = int(input("Enter the size of the array: "))
    arr = list(map(int, input("Enter the elements of the array: ").split()))
    print("Array:", arr)
    print("Maximum index product:", max_index_product(arr))

main()

