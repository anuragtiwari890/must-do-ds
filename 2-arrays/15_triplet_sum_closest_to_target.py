# problem link - https://www.geeksforgeeks.org/dsa/find-a-triplet-in-an-array-whose-sum-is-closest-to-a-given-number/

# 3 Sum - Triplet Sum Closest to Target

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    #Given an array arr[] of n integers and an integer target, find the sum of triplets such that the sum is closest to target. 
    # Note: If there are multiple sums closest to target, print the maximum one.

# ------------------------------------------------------------------------------------------------
# Examples: 

    #Input: arr[] = [-1, 2, 2, 4], target = 4
    #Output: 5
    #Explanation: All possible triplets

    #[-1, 2, 2], sum = (-1) + 2 + 2 = 3
    #[-1, 2, 4], sum = (-1) + 2 + 4 = 5
    #[-1, 2, 4], sum = (-1) + 2 + 4 = 5
    #[2, 2, 4], sum = 2 + 2 + 4 = 8
    #Triplet [-1, 2, 2], [-1, 2, 4] and [-1, 2, 4] have sum closest to target, so return the maximum one, that is 5.

    #Input: arr[] = [1, 10, 4, 5], target = 10
    #Output: 10
    #Explanation: All possible triplets

    #[1, 10, 4], sum = (1 + 10 + 4) = 15
    #[1, 10, 5], sum = (1 + 10 + 5) = 16
    #[1, 4, 5], sum = (1 + 4 + 5) = 10
    #[10, 4, 5], sum = (10 + 4 + 5) = 19
    #Triplet [1, 4, 5] has sum = 10 which is closest to target.

# ------------------------------------------------------------------------------------------------

# Intuition
    # The idea is to sort the array and then use two pointers to find the triplet that has the sum closest to the target.
    # We can use two pointers to find the triplet that has the sum closest to the target.
    # We can use two pointers to find the triplet that has the sum closest to the target.

# ------------------------------------------------------------------------------------------------

# approaches:
    # [Naive Approach] Using Three Nested Loops - O(n^3) Time and O(1) Space
        # The naive approach is to explore all subsets of size three and keep a track of the difference between target and the sum of the subset. 
        # Then, return the sum which is closest to target.

    # [Expected Approach] Sorting and Two Pointers – O(n^2) Time and O(1) Space
        # Initially, we sort the input array so that we can apply two pointers technique. 
        # Then, we iterate over the array fixing the first element of the triplet and then use two pointers technique to find the remaining two elements. 
        # Set one pointer at the beginning (left) and another at the end (right) of the remaining array. 
        # We then find the absolute difference between the sum of triplet and target and store the triplet having minimum absolute difference.

        # If sum < target, move left pointer towards right to increase the sum.
        # If sum > target, move right pointer towards left to decrease the sum.
        # If sum == target, we’ve found the triplet with sum = target, therefore this is the triplet with closest sum.

# ------------------------------------------------------------------------------------------------

# solution:
def closest3Sum(arr, target):
    n = len(arr)
    arr.sort() 
    res = 0
    minDiff = float('inf')

    for i in range(n - 2):
        # Initialize the left and right pointers
        l, r = i + 1, n - 1

        while l < r:
            currSum = arr[i] + arr[l] + arr[r]

            # If |currSum - target| < minDiff, then we have 
            # found a triplet which is closer to target
            if abs(currSum - target) < minDiff:
                minDiff = abs(currSum - target)
                res = currSum
            # If multiple sums are closest, take maximum one
            elif abs(currSum - target) == minDiff:
                res = max(res, currSum)

            # If currSum > target then we will decrease the 
            # right pointer to move closer to target
            if currSum > target:
                r -= 1

            # If currSum <= target then we will increase the 
            # left pointer to move closer to target
            else:
                l += 1

    return res


if __name__ == "__main__":
    arr = [-1, 2, 2, 4]
    target = 4
    print(closest3Sum(arr, target))