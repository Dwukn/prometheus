# linear search in python

def linearSearch(arr,target):
    for index in range(0, len(arr)):
        if arr[index] == target:
            return f"'{target}' found at index: {index}"
    # If the element is not found, return -1
    return f"{target} not in arr"


def main():
    arr=[1,2,5,9.0,-1,4]
    target = 2
    print(linearSearch(arr, target))
main()
