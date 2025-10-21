# problem link - https://www.geeksforgeeks.org/dsa/sort-array-wave-form-2/

# Sort array in wave form

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given a sorted array arr[] of integers (in ascending order), rearrange the elements in-place to form a wave-like array.
    # An array is said to be in wave form if it satisfies the following pattern: arr[0] ≥ arr[1] ≤ arr[2] ≥ arr[3] ≤ arr[4] ≥ ...
    # In other words, every even-indexed element should be greater than or equal to its adjacent odd-indexed elements (if they exist).

    # Note: The given array is sorted in ascending order, and modify the given array in-place without returning a new array.

# ------------------------------------------------------------------------------------------------

# Examples:
# Input: arr[] = [1, 2, 3, 4, 5]
# Output: [2, 1, 4, 3, 5]
# Explanation: Array elements after sorting it in the waveform are 2, 1, 4, 3, 5.

# Input: arr[] = [2, 4, 7, 8, 9, 10]
# Output: [4, 2, 8, 7, 10, 9]
# Explanation: Array elements after sorting it in the waveform are 4, 2, 8, 7, 10, 9.

# ------------------------------------------------------------------------------------------------
# approaches:
    # [Approach] - Adjacent Pair Swapping Method
        # The main idea of this approach is to rearrange it into a wave form by swapping adjacent elements in pairs.

    # Since, the elements are in increasing order. 
    # Then, by swapping every pair of adjacent elements (i.e., arr[0] with arr[1], arr[2] with arr[3], and so on), we create a pattern where:
        # Every even index i holds a value greater than or equal to its neighboring odd indices i - 1 and i + 1 (if they exist).
        # This guarantees the wave condition: arr[0] ≥ arr[1] ≤ arr[2] ≥ arr[3] ≤ arr[4] ≥ ...
    # The sorted array ensures the numbers are close enough to form valid wave peaks and valleys, and the pairwise swaps are what enforce the pattern.

    # Time complexity: O(n)
    # Space complexity: O(1)

# ------------------------------------------------------------------------------------------------
# solution:
# Python3 program to sort an array in wave form

def sortInWave(arr):
    
    n = len(arr)
   
    # swap adjacent elements
    for i in range(0,n-1,2):
        arr[i], arr[i+1] = arr[i+1], arr[i]

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    sortInWave(arr)
    for i in range(0,len(arr)):
        print (arr[i],end=" ")