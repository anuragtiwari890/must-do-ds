# problem link - https://www.geeksforgeeks.org/dsa/find-bitonic-point-given-bitonic-sequence/#expected-approach-using-binary-search-ologn-time-and-o1-space

# Find Bitonic Point Given Bitonic Sequence

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # You are given a Bitonic Sequence, the task is to find Bitonic Point in it.
    #  A Bitonic Sequence is a sequence of numbers which is first strictly increasing then after a point strictly decreasing.
    # A Bitonic Point is a point in bitonic sequence before which elements are strictly increasing and after which elements are strictly decreasing.

# ------------------------------------------------------------------------------------------------

# Examples:
# Input: arr[] = {8, 10, 100, 200, 400, 500, 3, 2, 1}
# Output: 500

# Input: arr[] = {10, 20, 30, 40, 30, 20}
# Output: 40

# Input: arr[] = {60, 70, 120, 100, 80}
# Output: 120

# ------------------------------------------------------------------------------------------------

# approaches:
    # [Naive Approach] - O(n) Time and O(1) Space
        # The naive approach is to traverse the array and find the bitonic point.
        # Time complexity: O(n)
        # Space complexity: O(1)

    # [Expected Approach] - O(logn) Time and O(1) Space
        # The input array follows a monotonic pattern. If an element is smaller than the next one, 
        # it lies in the increasing segment of the array, and the maximum element will definitely exist after it. 
        # Conversely, if an element is greater than the next one, it lies in the decreasing segment, meaning the maximum is either at this position or earlier. 
        # Therefore, we can use binary search to efficiently find the maximum element in the array.

# ------------------------------------------------------------------------------------------------
# solution:
# Python program to find the maximum element in a bitonic 
# array using binary search.

def bitonicPoint(arr):
  
    # Search space for binary search.
    lo = 0
    hi = len(arr) - 1    
    res = hi                 
    
    while lo <= hi:
        mid = (lo + hi) // 2 
        
        # Decreasing segment
        if mid + 1 < len(arr) and arr[mid] > arr[mid + 1]:
            res = mid            
            hi = mid - 1  
        # Increasing segment
        else:
            lo = mid + 1       
            
    return arr[res]              

if __name__ == "__main__":
    arr = [8, 10, 100, 400, 500, 3, 2, 1] 
    print(bitonicPoint(arr))
