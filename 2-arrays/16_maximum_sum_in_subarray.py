# problem link - https://www.geeksforgeeks.org/dsa/print-the-maximum-subarray-sum/

# Maximum Sum in Subarray

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given an array arr[] of size N, the task is to find the maximum sum of the subarray among all subarrays.

# ------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: arr[] = {-2, -3, 4, -1, -2, 1, 5, -3}
    # Output: 7
    # Explanation: The subarray [4, -1, -2, 1, 5] has the maximum sum among all subarrays.

    # Input: arr[] = {-2, -5, 6, -2, -3, 1, 5, -6}
    # Output: 7
    # Explanation: The subarray [6, -2, -3, 1, 5] has the maximum sum among all subarrays.

# ------------------------------------------------------------------------------------------------

# approach:
    # [Naive Approach] By iterating over all subarrays - O(n^2) Time and O(1) Space
        # The idea is to run two nested loops to iterate over all possible subarrays and find the maximum sum. 
        # The outer loop will mark the starting point of a subarray and inner loop will mark the ending point of the subarray.
        # Time complexity: O(n^2)
        # Space complexity: O(1)

    # [Expected Approach] Using Kadane's Algorithm - O(n) Time and O(1) Space
        # The idea of Kadane's algorithm is to traverse over the array from left to right and for each element,
        # find the maximum sum among all subarrays ending at that element. The result will be the maximum of all these values.
        # To calculate the maximum sum of subarray ending at current element, say maxEnding, we can use the maximum sum ending at the previous element.
        # Choice 1: Extend the maximum sum subarray ending at the previous element by adding the current element to it. 
            # If the maximum subarray sum ending at the previous index is positive, then it is always better to extend the subarray.

        # Choice 2: Start a new subarray starting from the current element. 
            # If the maximum subarray sum ending at the previous index is negative, it is always better to start a new subarray from the current element.

        # This means that maxEnding at index i = max(maxEnding at index (i - 1) + arr[i], arr[i]) 
            # and the maximum value of maxEnding at any index will be our answer.

        # Kadane's algorithm is a dynamic programming algorithm that finds the maximum sum of a subarray in linear time.

        # Time complexity: O(n)
        # Space complexity: O(1)

# ------------------------------------------------------------------------------------------------

# solution:
def maxSubarraySum(arr):
    
    # Stores the result (maximum sum found so far)
    res = arr[0]
    
    # Maximum sum of subarray ending at current position
    maxEnding = arr[0]

    for i in range(1, len(arr)):
        
        # Either extend the previous subarray or start 
        # new from current element
        maxEnding = max(maxEnding + arr[i], arr[i])
        
        # Update result if the new subarray sum is larger
        res = max(res, maxEnding)
    
    return res

if __name__ == "__main__":
    arr = [2, 3, -8, 7, -1, 2, 3]
    print(maxSubarraySum(arr))