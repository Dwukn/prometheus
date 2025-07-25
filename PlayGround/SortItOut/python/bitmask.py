import random
import time

# Generate a random array with 10 million elements
array = random.sample(range(1, 10001), 10000)

# Bitmask sum approach using a for loop
def bitmask_sum(array, bitmask):
    total_sum = 0
    for i in range(len(array)):
        if (bitmask >> i) & 1:  # Check if the i-th bit is set
            total_sum += array[i]
    return total_sum

# Normal sum approach using a for loop
def normal_sum(array):
    total_sum = 0
    for num in array:
        total_sum += num
    return total_sum



# Example: Using bitmasking for TSP dynamic programming
# n cities, dp[mask] stores the minimum cost of visiting cities represented by 'mask'

n = 4  # Number of cities
dp = [float('inf')] * (1 << n)  # DP table with 2^n states
dp[0] = 0  # Base case: no cities visited, cost is 0

dist = [
    [0, 10, 15, 20],  # Distances from city 0 to others
    [10, 0, 35, 25],  # Distances from city 1 to others
    [15, 35, 0, 30],  # Distances from city 2 to others
    [20, 25, 30, 0],  # Distances from city 3 to others
]

# Updating the DP table using bitmasking
for mask in range(1 << n):
    for u in range(n):  # Try to visit city 'u' from all cities in the current 'mask'
        if (mask & (1 << u)) == 0:  # If city u is not in the current subset
            continue
        # Update the DP value for the next state
        for v in range(n):
            if (mask & (1 << v)) == 0:
                dp[mask | (1 << v)] = min(dp[mask | (1 << v)], dp[mask] + dist[u][v])


# # Set a random bitmask (random selection of 1's and 0's)
# bitmask = random.getrandbits(len(array))

# # Measure time for bitmask sum
# start_time = time.time()
# bitmask_result = bitmask_sum(array, bitmask)
# bitmask_duration = time.time() - start_time

# # Measure time for normal sum
# start_time = time.time()
# normal_result = normal_sum(array)
# normal_duration = time.time() - start_time

# print(f"Bitmask sum time: {bitmask_duration:.6f} seconds")
# print(f"Normal sum time: {normal_duration:.6f} seconds")

# Subset sum problem with bitmask
# nums = [1, 2, 3, 4, 5]
target_sum = 7
n = len(array)

# Iterate through all possible subsets using a bitmask
for mask in range(1 << n):
    subset_sum = 0
    for i in range(n):
        if mask & (1 << i):  # If the i-th bit is set, include nums[i]
            subset_sum += array[i]

    if subset_sum == target_sum:
        print(f"Subset with target sum {target_sum}:")
        for i in range(n):
            if mask & (1 << i):
                print(array[i], end=' ')
        print()
