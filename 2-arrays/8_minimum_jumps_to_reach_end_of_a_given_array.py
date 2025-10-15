# problem link - https://www.geeksforgeeks.org/dsa/minimum-number-of-jumps-to-reach-end-of-a-given-array/

# Jump Game - Minimum Jumps to Reach End

# ------------------------------------------------------------------------------------------------
# problem statement:

# Given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps you can jump forward from that position.
    # For example:
        # If arr[i] = 3, you can jump to index i + 1, i + 2, or i + 3 from position i.
        # If arr[i] = 0, you cannot jump forward from that position.

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: arr[] = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    # Output: 3 
    # Explanation: First jump from 1st element to 2nd element with value 3. From here we jump to 5th element with value 9, and from here we will jump to the last. 

    # Input: arr = [1, 4, 3, 2, 6, 7]
    # Output: 2 
    # Explanation: First we jump from the 1st to 2nd element and then jump to the last element.

    # Input: arr = [0, 10, 20]
    # Output: -1
    # Explanation: We cannot go anywhere from the 1st element.

# ------------------------------------------------------------------------------------------------

# approach:
    # [Naive Approach] Using Recursion - O(n^n) time and O(n) space
        # The idea is to recursively generate all possible way of reaching the end of the array and find the one with the minimum steps required. 
        # To do so, start from the first element and for each element arr[i] recursively call for all the elements reachable from that element 
        # (i.e. i + arr[i]) and return the one with the minimum steps required.

        # Time complexity: O(n^n)
        # Space complexity: O(n)

    # [Better Approach 1] - Using Top-Down DP (Memoization) - O(n^2) Time and O(n) Space
        # The above approach can be optimized using memoization to avoid computing the overlapping subproblems multiple times. 
        # For example in array, arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9} minJumps(3, 9) will be called two times as arr[3] is reachable from arr[1] and arr[2].

        # So this problem has both properties (optimal substructure and overlapping subproblems) of Dynamic Programming.
        # To do so, create an array memo[] of size n, where each element memo[i] stores the minimum steps required to reach end of array from index i.
        # For each recursive call, check if subproblem is already calculated, if so return the stored value, else operate similar to above approach.

    # [Better Approach 2] - Using Bottom-Up DP (Tabulation) - O(n^2) Time and O(n) Space
        # The above approach can further be optimized using bottom-up dp (tabulation) to minimize the space required for recursive stack. 
        # To do so, create an array dp[] of size n, where each element dp[i] stores the minimum steps required to reach end of array from index i. 
        # Start from the last index i.e. n-1, and for each index i compute the minimum steps for subarray i to n-1 and store the result in dp[i]. 
        # Finally, return dp[0] as the result.

        # Time complexity: O(n^2)
        # Space complexity: O(n)

    # [Efficient Approach] - Using Greedy Approach - O(n) Time and O(1) Space
        # The idea is to use a greedy approach to find the minimum jumps to reach the end of the array.
        # Step by step approach:
            # 1. Initialize a variable to store the minimum jumps required to reach the end of the array.
            # 2. Initialize a variable to store the maximum reachable index from the current index.
            # 3. Traverse the array and update the maximum reachable index from the current index.
            # 4. If the maximum reachable index is greater than or equal to the end of the array, then return the minimum jumps required to reach the end of the array.
            # 5. If the maximum reachable index is less than the end of the array, then return -1.

# ------------------------------------------------------------------------------------------------

# Solution:
# using greedy approach
#explanation:   
# 1. Initialize a variable to store the minimum jumps required to reach the end of the array.
# 2. Initialize a variable to store the maximum reachable index from the current index.
# 3. Traverse the array and update the maximum reachable index from the current index.
# 4. If the maximum reachable index is greater than or equal to the end of the array, then return the minimum jumps required to reach the end of the array.
# 5. If the maximum reachable index is less than the end of the array, then return -1.


# Time complexity: O(n)
# Space complexity: O(1)

# nice explanation link - https://www.geeksforgeeks.org/dsa/minimum-number-jumps-reach-endset-2on-solution/

def minJumps(arr):
    n = len(arr)
    if arr[0] == 0:
        return -1

    # 1. Initialize a variable to store the minimum jumps required to reach the end of the array.
    maxReach = 0
    # 2. Initialize a variable to store the maximum reachable index from the current index.
    currReach = 0
    # 3. Initialize a variable to store the minimum jumps required to reach the end of the array.
    jump = 0

    # 4. Traverse the array and update the maximum reachable index from the current index.
    for i in range(n):
        maxReach = max(maxReach, i + arr[i])

        # 5. If the maximum reachable index is greater than or equal to the end of the array, 
        # then return the minimum jumps required to reach the end of the array.
        if maxReach >= n - 1:
            return jump + 1

        # Increment the Jump as we reached the
        # Current Reachable index
        if i == currReach:

            # If Max reach is same as current index
            # then we can not jump further
            if i == maxReach:
                return -1

            # If Max reach > current index then increment
            # jump and update current reachable index
            else:
                jump += 1
                currReach = maxReach

    return -1


if __name__ == "__main__":
    arr = [1, 3, 2, 2, 1, 4, 6]
    print(minJumps(arr))

print(minJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
print(minJumps([1, 4, 3, 2, 6, 7]))
print(minJumps([0, 10, 20]))



