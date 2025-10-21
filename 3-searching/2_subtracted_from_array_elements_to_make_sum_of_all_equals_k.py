# problem link - https://www.geeksforgeeks.org/dsa/value-to-be-subtracted-from-array-elements-to-make-sum-of-all-elements-equals-k/

# Value to be subtracted from array elements to make sum of all elements equals K


# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given an integer K and an array, height[] where height[i] denotes the height of the ith tree in a forest. 
    # The task is to make a cut of height X from the ground such that exactly K unit wood is collected. 
    # If it is not possible, then print -1 else print X.

# ------------------------------------------------------------------------------------------------

# Examples:
# Input: height[] = {1, 2, 1, 2}, K = 2 
# Output: 1 
# Make a cut at height 1, the updated array will be {1, 1, 1, 1} and 
# the collected wood will be {0, 1, 0, 1} i.e. 0 + 1 + 0 + 1 = 2.

# Input: height[] = {1, 2, 3}, K = 4 
# Output: 2 
# Make a cut at height 2, the updated array will be {1, 0, 1} and 
# the collected wood will be {0, 0, 1} i.e. 0 + 0 + 1 = 1.

# Input: height[] = {5, 9, 7}, K = 4 
# Output: -1 
# It is not possible to make a cut of height X to get exactly K unit wood.

# ------------------------------------------------------------------------------------------------

# approaches:
    # [Naive Approach] - O(n^2) Time and O(1) Space
        # The naive approach is to try all possible heights and check if the collected wood is exactly K.
        # Time complexity: O(n^2)
        # Space complexity: O(1)


    # [Expected Approach] - O(nlogn) Time and O(1) Space
        # The expected approach is to use binary search to find the height such that the collected wood is exactly K.
        # Sort the heights of the trees.
        # The lowest height to make the cut is 0 and the highest height is the maximum height among all the trees. So, set low = 0 and high = max(height[i]).
        # Repeat the steps below while low ≤ high: 
        # Set mid = low + ((high - low) / 2).
            # Count the amount of wood that can be collected if the cut is made at height mid and store it in a variable collected.
            # If collected = K then mid is the answer.
            # If collected > K then update low = mid + 1 as the cut needs to be made at a height higher than the current height.
            # Else update high = mid - 1 as cuts need to be made at a lower height.
            # Time complexity: O(n^2)
            # Space complexity: O(1)
        # Time complexity: O(nlogn)
        # Space complexity: O(1)

# ------------------------------------------------------------------------------------------------
 
# solution:

# Python3 implementation of the approach

# Function to return the amount of wood
# collected if the cut is made at height m
def woodCollected(height, n, m):
    sum = 0
    for i in range(n - 1, -1, -1):
        if (height[i] - m <= 0):
            break
        sum += (height[i] - m)

    return sum

# Function that returns Height at
# which cut should be made
def collectKWood(height, n, k):
    
    # Sort the heights of the trees
    height = sorted(height)

    # The minimum and the maximum
    # cut that can be made
    low = 0
    high = height[n - 1]

    # Binary search to find the answer
    while (low <= high):
        mid = low + ((high - low) // 2)

        # The amount of wood collected
        # when cut is made at the mid
        collected = woodCollected(height, n, mid)

        # If the current collected wood is
        # equal to the required amount
        if (collected == k):
            return mid

        # If it is more than the required amount
        # then the cut needs to be made at a
        # height higher than the current height
        if (collected > k):
            low = mid + 1

        # Else made the cut at a lower height
        else:
            high = mid - 1

    return -1

# Driver code
height = [1, 2, 1, 2]
n = len(height)
k = 2

print(collectKWood(height, n, k))
