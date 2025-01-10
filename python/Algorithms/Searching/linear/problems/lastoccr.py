def linearSearch(arr, target):
    revarr = arr[::-1]
    for i in range(0, len(revarr)):
        if arr[i] == target:
            return f" {arr} \n '{target}' occurs first at index: {len(arr) - i}"
    return f"{target} not in arr"
arr = [2, 1, 1, 34, 1, 82, 83, 1 ,2, 1 ,3]
target = 1
print(len(arr))
print(linearSearch(arr,target))


