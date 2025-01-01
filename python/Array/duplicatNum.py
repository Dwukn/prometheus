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

def main():
    arr = [7,2,3,1,2,3,4,2,3]
    print("Array:", arr)
    print("Duplicate Number:", findDuplicate(arr))

if __name__ == "__main__":
    main()
