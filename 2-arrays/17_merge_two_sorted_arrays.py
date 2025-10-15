# problem link - https://www.geeksforgeeks.org/dsa/merge-two-sorted-arrays/

# Merge Two Sorted Arrays

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-decreasing order. 
    # Merge them in sorted order. Modify arr1[] so that it contains the first N elements and modify arr2[] so that it contains the last M elements.

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: arr1[] = {1, 3, 5, 7}, arr2[] = {0, 2, 6, 8, 9}
    # Output: arr1[] = {0, 1, 2, 3, 5, 6, 7, 8, 9}
    # Explanation: After merging the two non-decreasing arrays, we get, 0, 1, 2, 3, 5, 6, 7, 8, 9.

    # Input: arr1[] = {1, 3, 5, 7}, arr2[] = {0, 2, 6, 8, 9}
    # Output: arr1[] = {0, 1, 2, 3, 5, 6, 7, 8, 9}
    # Explanation: After merging the two non-decreasing arrays, we get, 0, 1, 2, 3, 5, 6, 7, 8, 9.

    # Input: arr1[] = {1, 3, 5, 7}, arr2[] = {0, 2, 6, 8, 9}
    # Output: arr1[] = {0, 1, 2, 3, 5, 6, 7, 8, 9}
    # Explanation: After merging the two non-decreasing arrays, we get, 0, 1, 2, 3, 5, 6, 7, 8, 9.

# ------------------------------------------------------------------------------------------------

# approaches:
    # [Approach] Using Two Pointers - O(n + m) Time and O(n + m) Space
        # The idea is to use two pointers to merge the two arrays.
        # Step-by-Step Implementation:
            # Initialize two pointers: i = 0 for traversing arr1, j = 0 for traversing arr2
            # Create an empty array merged = []
            # Merge the elements into merged: While both i < n and j < m:
            # => If arr1[i] <= arr2[j], append arr1[i] to merged and increment i
            # => Else, append arr2[j] to merged and increment j
            # Append remaining elements (if any):
            # => While i < n, append arr1[i] to merged and increment i
            # => While j < m, append arr2[j] to merged and increment j
            # Distribute the merged elements back:
            # => Copy the first n elements of merged to arr1
            # => Copy the remaining m elements to arr2

# ------------------------------------------------------------------------------------------------

# solution:
def mergeArrays(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i = j = 0

    # temporary array to store merged result
    merged = []

    # merge elements in sorted order
    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # copy remaining elements from arr1
    while i < n:
        merged.append(arr1[i])
        i += 1

    # copy remaining elements from arr2
    while j < m:
        merged.append(arr2[j])
        j += 1

    # copy first n to arr1
    for i in range(n):
        arr1[i] = merged[i]

    # copy remaining m to arr2
    for j in range(m):
        arr2[j] = merged[n + j]

if __name__ == "__main__":
    arr1 = [1, 3, 5, 7]
    arr2 = [2, 4, 6, 8]

    mergeArrays(arr1, arr2)

    print(*arr1)
    print(*arr2)