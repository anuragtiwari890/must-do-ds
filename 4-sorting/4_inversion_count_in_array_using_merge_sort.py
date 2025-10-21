# problem link - https://www.geeksforgeeks.org/dsa/inversion-count-in-array-using-merge-sort/

# Inversion Count in an array using Merge Sort

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given an integer array arr[] of size n, find the inversion count in the array. 
    # Two array elements arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j.


    # Note: Inversion Count for an array indicates that how far (or close) the array is from being sorted. 
    # If the array is already sorted, then the inversion count is 0, but if the array is sorted in reverse order, the inversion count is maximum. 

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: arr[] = [4, 3, 2, 1]
    # Output: 6
    # Explanation: There are six pairs of indexes (i, j) such that arr[i] > arr[j] and i < j: (4, 3), (4, 2), (4, 1), (3, 2), (3, 1), and (2, 1).

    # Input: arr[] = [1, 2, 3, 4, 5]
    # Output: 0
    # Explanation: There is no pair of indexes (i, j) exists in the given array such that arr[i] > arr[j] and i < j

    # Input: arr[] = [10, 10, 10]
    # Output: 0
    # Explanation: There is no pair of indexes (i, j) exists in the given array such that arr[i] > arr[j] and i < j

# ------------------------------------------------------------------------------------------------
# approaches:
    # [Naive Approach] - O(n^2) Time and O(1) Space
        # The naive approach is to try all possible pairs of elements and check if they form an inversion.
        # Time complexity: O(n^2)
        # Space complexity: O(1)

    # [Better Approach] - O(nlogn) Time and O(n) Space
        # We can use merge sort to count the inversions in an array. 
        # First, we divide the array into two halves: left half and right half. 
        # Next, we recursively count the inversions in both halves. 
        # While merging the two halves back together, 
            # we also count how many elements from the left half array are greater than elements from the right half array, 
        # as these represent cross inversions 
            # (i.e., element from the left half of the array is greater than an element from the right half during the merging process in the merge sort algorithm). 
            # Finally, we sum the inversions from the left half, right half, and the cross inversions to get the total number of inversions in the array. 
            # This approach efficiently counts inversions while sorting the array.

        # Step by step approach:
            # During each merging step of the merge sort algorithm, 
            # we count cross inversions by comparing elements from the left half of the array with those from the right half. 
            # If we find an element arr[i] in the left half that is greater than an element arr[j] in the right half, 
            # we can conclude that all elements after i in the left half will also be greater than arr[j]. This allows us to count multiple inversions at once. 
            # Let's suppose if there are k elements remaining in the left half after i, then there are k cross inversions for that particular arr[j]. 
            # The rest of the merging process continues as usual, where we combine the two halves into a sorted array. 
            # This efficient counting method significantly reduces the number of comparisons needed, 
            # enhancing the overall performance of the inversion counting algorithm.

        # Time complexity: O(nlogn)
        # Space complexity: O(n)

# ------------------------------------------------------------------------------------------------
# solution:

# This function merges two sorted subarrays arr[l..m] and arr[m+1..r] 
# and also counts inversions in the whole subarray arr[l..r]
def countAndMerge(arr, l, m, r):
  
    # Counts in two subarrays
    n1 = m - l + 1
    n2 = r - m

    # Set up two lists for left and right halves
    left = arr[l:m + 1]
    right = arr[m + 1:r + 1]

    # Initialize inversion count (or result)
    # and merge two halves
    res = 0
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:

        # No increment in inversion count
        # if left[] has a smaller or equal element
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            res += (n1 - i)
        k += 1

    # Merge remaining elements
    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1

    return res

# Function to count inversions in the array
def countInv(arr, l, r):
    res = 0
    if l < r:
        m = (r + l) // 2

        # Recursively count inversions
        # in the left and right halves
        res += countInv(arr, l, m)
        res += countInv(arr, m + 1, r)

        # Count inversions such that greater element is in 
        # the left half and smaller in the right half
        res += countAndMerge(arr, l, m, r)
    return res

def inversionCount(arr):
    return countInv(arr, 0, len(arr) - 1)

if __name__ == "__main__":
    arr = [4, 3, 2, 1]
    print(inversionCount(arr))