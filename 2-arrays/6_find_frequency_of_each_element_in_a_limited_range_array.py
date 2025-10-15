# problem link - https://www.geeksforgeeks.org/dsa/find-frequency-of-each-element-in-a-limited-range-array/

# Find frequency of each element in a limited range array in less than O(n) time

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    #Given a sorted array arr[] of positive integers, the task is to find the frequency for each element in the array. 
    # Assume all elements in the array are less than some constant M

    # Note: Do this without traversing the complete array. i.e. expected time complexity is less than O(n)

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: arr[] = {1, 1, 1, 2, 3, 3, 5, 5, 8, 8, 8, 9, 9, 10}
    # Output:
    # 1 occurs 3 times
    # 2 occurs 1 time
    # 3 occurs 2 times
    # 5 occurs 2 times
    # 8 occurs 3 times
    # 9 occurs 2 times
    # 10 occurs 1 time

    # Input: arr[] = [2, 2, 6, 6, 7, 7, 7, 11] 
    # Output: 
    # Element 2 occurs 2 times
    # Element 6 occurs 2 times
    # Element 7 occurs 3 times
    # Element 11 occurs 1 times

# ------------------------------------------------------------------------------------------------
# approaches:
    # [Naive Approach - 1] Using Linear Search - O(n) time and O(1) space
        # Traverse the input array and increment the frequency of the element if the current element and the previous element are the same, 
        # otherwise reset the frequency and print the element and its frequency.

        # Time complexity: O(n)
        # Space complexity: O(1)
    
    # [Expected Approach] Using Binary Search - O(m log(n)) time and O(1) space
        # The idea is to use binary search to find the first and last occurrence of the element in the array.
        # Then the frequency of the element is the difference between the last and first occurrence + 1.
        
        # Time complexity: O(m log(n))
        # Space complexity: O(1)

        # Step by step approach:
            # Start with index i = 0 and get the current value val = arr[i]
            # Use binary search to find the last occurrence (endIndex) of val in the array
            # Calculate frequency as (endIndex - i + 1)
            # Print the value and its frequency
            # Update i to (endIndex + 1) to skip to the next unique element
            # Repeat until we reach the end of the array


# ------------------------------------------------------------------------------------------------

# solution:
# Python program to count number of occurrences of
# each value in the array in O(n) time and O(1) space

# It prints number of
# occurrences of each element in the array.
def findFrequencies(arr):
    n = len(arr)
    
    i = 0
    
    # Traverse the array and find the frequency of each element
    while i < n:
        val = arr[i]
        s, e = i, n - 1
        # Find the last occurrence of the element
        endIndex = i
        
        while s <= e:
            # Find the middle element
            mid = s + (e - s) // 2
            # If the middle element is the same as the value, update the endIndex
            if arr[mid] == val:
                # Update the endIndex
                endIndex = mid
                # Update the start index
                s = mid + 1
            # If the middle element is not the same as the value, update the end index
            else:
                # Update the end index
                e = mid - 1
        
        # Calculate the frequency
        cnt = endIndex - i + 1
        
        # Print the value and its frequency
        print(val, cnt)
        
        # Update i to next value index
        i = endIndex + 1


if __name__ == "__main__":
    arr = [1, 1, 1, 2, 3, 3, 5, 5, 8, 8, 8, 9, 9, 10]

    findFrequencies(arr)
