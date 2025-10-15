# problem link - https://www.geeksforgeeks.org/dsa/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/

# Maximum j - i in an array such that arr[i] <= arr[j]

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given an array arr[] of n positive integers, the task is to find the maximum of j - i subjected to the constraint of arr[i] <= arr[j] and i <= j.

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: arr[] = {34, 8, 10, 3, 2, 80, 30, 33, 1}
    # Output: 6
    # Explanation: In the given array arr, arr[1] - arr[7] = 7  & (8 - 1)is the maximum value of j - i.

    # Input: arr[] =   [1, 2, 3, 4, 5, 6]
    # Output: 5  
    # Explanation: For i = 0 and j = 5, arr[j] >= arr[i] and j - i is maximum

    # Input:  [6, 5, 4, 3, 2, 1]
    # Output: 0
    # Explanation: Take any i and j where i == j.

# ------------------------------------------------------------------------------------------------

# approaches:
    # [Naive Approach] - O(n^2) Time and O(1) Space
        # The idea is to traverse the array and for each element, find the maximum element to the right of the current element and check if the current element is less than the maximum element.
        # If yes, then update the maximum difference.

        # Time complexity: O(n^2)
        # Space complexity: O(1)
        
    # [Better Approach] - using sorting and preseving their index - O(nlogn) Time and O(n) Space
        # The idea is to sort the array and then use two pointers to find the maximum difference.
        # The first pointer, i, starts from the beginning of the array and the second pointer, j, starts from the end of the array.
        # If the element at i is less than the element at j, then update the maximum difference.
        # If the element at i is greater than the element at j, then move the first pointer to the right.
        # If the element at i is equal to the element at j, then move the second pointer to the left.

        # Time complexity: O(nlogn)
        # Space complexity: O(n)

   # [Expected Approach - 1] Using Precomputed Min Max Values - O(n) time and O(n) space
        # Precompute the minimum values from left to right for each position.
        # Precompute the maximum values from right to left for each position.
        # Use two pointers starting at the beginning of both arrays.
        # When the minimum value is less than or equal to maximum value, record the distance and move right pointer.
        # When the condition fails, move the left pointer to find a smaller minimum value.

        # illustration:
            # Input: arr[] = {34, 8, 10, 3, 2, 80, 30, 33, 1}
            # First we build lMin array (minimum values from left to right): 
                # [34, 8, 8, 3, 2, 2, 2, 2, 1]
            # Then we build rMax array (maximum values from right to left): 
                # [80, 80, 80, 80, 80, 80, 33, 33, 1]
            # Starting with i=0, j=0: lMin[0]=34, rMax[0]=80, 
                # condition is satisfied (34≤80), record diff=0, increment j
            # At i=0, j=5: lMin[0]=34, rMax[5]=80, max diff=5, 
                # increment j
            # Continue until i=1, j=8: lMin[1]=8, rMax[8]=1, 
                # condition fails (8>1), increment i
            # At i=4, j=7: lMin[4]=2, rMax[7]=33, 
                # condition satisfied (2≤33), max diff=3, increment j
            # Final result: When we've exhausted all valid combinations, the maximum difference found is 7 
                # (occurring when i=1, j=8 - the difference right before condition failed)

# ------------------------------------------------------------------------------------------------

# solution:
def maxIndexDiff(arr):
    
    n = len(arr)
    lMin = [0] * n
    rMax = [0] * n
    
    # lMin[i] stores the minimum value 
    # in the range [0, i]
    lMin[0] = arr[0]
    for i in range(1, n):
        lMin[i] = min(lMin[i - 1], arr[i])
    
    # rMax[i] stores the maximum value
    # in the range [i, n-1]
    rMax[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        rMax[i] = max(rMax[i + 1], arr[i])
    
    i = 0
    j = 0
    ans = 0
    
    while i < n and j < n:
        
        # Compare with answer and increment
        # j.
        if lMin[i] <= rMax[j]:
            ans = max(ans, j - i)
            j += 1
        
        # Else, increment i.
        else:
            i += 1
    
    return ans

if __name__ == "__main__":
    arr = [34, 8, 10, 3, 2, 80, 30, 33, 1]
    print(maxIndexDiff(arr))