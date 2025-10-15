# problem link - https://www.geeksforgeeks.org/dsa/search-insert-position-of-k-in-a-sorted-array/

# Search Insert Position of K in a Sorted Array

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given a sorted array of distinct integers and a target value, return the index where it would be if it were inserted in order.

# ------------------------------------------------------------------------------------------------
# Examples: 

# Input: arr[] = [1, 3, 5, 6], k = 5
# Output: 2
# Explanation: Since 5 is found at index 2 as arr[2] = 5, the output is 2.

# Input: arr[] = [1, 3, 5, 6], k = 2
# Output: 1
# Explanation: The element 2 is not present in the array, but inserting it at index 1 will maintain the sorted order.

# ------------------------------------------------------------------------------------------------

# approaches:
    # [Naive Approach] - O(n) Time and O(1) Space
        # The naive approach is to traverse the array and find the index where the target value would be inserted.
        # Time complexity: O(n)
        # Space complexity: O(1)

    # [Expected Approach] - O(logn) Time and O(1) Space
        # The expected approach is to use binary search to find the index where the target value would be inserted.
        # Time complexity: O(logn)
        # Space complexity: O(1)

# ------------------------------------------------------------------------------------------------

# solution:
def searchInsertK(arr, k):  
    left, right = 0, len(arr) - 1  
    while left <= right:  
        mid = left + (right - left) // 2  
        
        # if k is found at mid
        if arr[mid] == k:  
            return mid  

        # if k is smaller, search in left half
        elif arr[mid] > k:  
            right = mid - 1  

        # if k is larger, search in right half
        else:  
            left = mid + 1  

    # if k is not found, return insert position
    return left  

if __name__ == "__main__":  

    arr = [1, 3, 5, 6]  
    k = 5  
    print(searchInsertK(arr, k))

