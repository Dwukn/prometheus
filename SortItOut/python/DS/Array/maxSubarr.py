def maxSubarraySum(res):
    maxSum = res[0]
    currentSum = res[0]
    for i in range(1, len(res)):
        currentSum = max(res[i], currentSum + res[i])
        maxSum = max(maxSum, currentSum)
    return maxSum

def main():
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Maximum Subarray Sum:", maxSubarraySum(arr))

if __name__ == "__main__":
    main()
