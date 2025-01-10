def linearSearch(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return f" {arr} \n '{target}' occurs first at index: {i}"
    return f"{target} not in arr"
arr = [2, 1, 1, 34, 1, 82, 83, 1 ,2, 1 ,3]
target = 1
print(linearSearch(arr,target))
