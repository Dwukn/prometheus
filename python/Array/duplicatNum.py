# Finds duplicate but wont work if array elements are greater than the length of the array

def findDuplicate(nums):
    slow = nums[0]
    fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    fast = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

def findDuplicateSet(nums):
    seen = set()  # Use a set to track seen numbers
    for num in nums:
        if num in seen:
            return num  # Return the duplicate number
        seen.add(num)
    return None  # If no duplicate found (though one is guaranteed in this problem)


def main():
    arr = [7,2,3,1,2,3,4,2,3]
    arr2 = [56, 34, 56, 78, 90, 12, 34, 56, 78, 90]
    print("Array:", arr)
    print("Duplicate Number:", findDuplicate(arr))
    print("Duplicate Number using set:", findDuplicateSet(arr2))

if __name__ == "__main__":
    main()
