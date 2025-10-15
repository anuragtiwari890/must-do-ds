# problem link - https://www.geeksforgeeks.org/dsa/rearrange-array-in-alternating-positive-negative-items-with-o1-extra-space-set-2/

# Rearrange array in alternating positive & negative items with O(1) extra space

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given an array of positive and negative numbers, arrange them in an alternate fashion such that every positive number is followed by a negative and vice-versa maintaining the order of appearance. 
    # The number of positive and negative numbers need not be equal. If there are more positive numbers they appear at the end of the array. If there are more negative numbers, they too appear at the end of the array.

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input :
    # arr[] = {-2, 3, 4, -1}
    # Output :
    # arr[] = {-2, 3, -1, 4} OR {-1, 3, -2, 4} OR ..

    # Input :
    # arr[] = {-2, 3, 1}
    # Output :
    # arr[] = {-2, 3, 1} OR {-2, 1, 3} 

    # Input : 
    # arr[] = {-5, 3, 4, 5, -6, -2, 8, 9, -1, -4}
    # Output :
    # arr[] = {-5, 3, -2, 5, -6, 4, -4, 9, -1, 8}  OR ..

# ------------------------------------------------------------------------------------------------

# approaches:
    # [Naive Approach] - 
    # Approach 1: using sorting - O(nlogn) Time and O(n) Space
        # First, sort the array in non-increasing order. Then we will count the number of positive and negative integers.
        # Then swap the one negative and one positive number in the odd positions till we reach our condition.
        # This will rearrange the array elements because we are sorting the array and accessing the element from left to right according to our need.Using Extra Space - O(n) Time and O(n) Space

    # Approach 2: Using Partitioning - O(n) Time and O(1) Space
        # The idea is to first separate positive and negative numbers using the partition process of the QuickSort.
        # In the partition process, consider 0 as a positive element.
        # Use a two-pointer technique to swap the positive and negative elements in the array to maintain the order of appearance.
        # The first pointer, i, iterates through the array, and the second pointer, j, only swaps non-zero elements.

# ------------------------------------------------------------------------------------------------

# solution:
# approach 2:
# Python3 program to rearrange array
# in alternating positive & negative
# items with O(1) extra space

# Function to rearrange positive and
# negative integers in alternate fashion.
# The below solution does not maintain
# original order of elements


def rearrange(arr):
    n = len(arr)
    i = 0
    j = n - 1

    # shift all negative values
    # to the end
    while (i < j):

        while (i <= n - 1 and arr[i] > 0):
            i += 1
        while (j >= 0 and arr[j] < 0):
            j -= 1

        if (i < j):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    # i has index of leftmost
    # negative element
    if (i == 0 or i == n):
        return 0

    # start with first positive element
    # at index 0

    # Rearrange array in alternating
    # positive & negative items
    k = 0
    while (k < n and i < n):

        # swap next positive element at even
        # position from next negative element.
        temp = arr[k]
        arr[k] = arr[i]
        arr[i] = temp
        i = i + 1
        k = k + 2

# Utility function to print an array


# Driver code
arr = [2, 3]
rearrange(arr)
print(arr)

arr = [-2, 3, 4, -1]
rearrange(arr)
print(arr)

arr = [-2, 3, 1]
rearrange(arr)
print(arr)

arr = [-5, 3, 4, 5, -6, -2, 8, 9, -1, -4]
rearrange(arr)
print(arr)
