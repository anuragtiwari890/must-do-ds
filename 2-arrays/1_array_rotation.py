# problem link - https://www.geeksforgeeks.org/dsa/array-rotation/

# Array Rotation

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given an array of integers arr[] of size n, the task is to rotate the array elements to the left by d positions.

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: arr[] = {1, 2, 3, 4, 5, 6}, d = 2
    # Output: {3, 4, 5, 6, 1, 2}
    # Explanation: After first left rotation, arr[] becomes {2, 3, 4, 5, 6, 1} and after the second rotation, arr[] becomes {3, 4, 5, 6, 1, 2}

    # Input: arr[] = {1, 2, 3}, d = 4
    # Output: {2, 3, 1}
    # Explanation: The array is rotated as follows:
        # After first left rotation, arr[] = {2, 3, 1}
        # After second left rotation, arr[] = {3, 1, 2}
        # After third left rotation, arr[] = {1, 2, 3}
        # After fourth left rotation, arr[] = {2, 3, 1}

# ------------------------------------------------------------------------------------------------

# Naive Approach:
    # This approach is to rotate the array by d positions to the left.
    # Time complexity: O(n*d)
    # Space complexity: O(1)

# ------------------------------------------------------------------------------------------------

# Optimal Approach: 
    # [Better Approach] Using Temporary Array 
    # Time complexity: O(n)
    # Space complexity: O(n)

# ------------------------------------------------------------------------------------------------

# Optimal Approach: 
    # [Best Approach] Using Reverse Algorithm 
    # Explanation:
        # 1. Reverse the first d elements.
        # 2. Reverse the remaining n-d elements.
        # 3. Reverse the entire array.
        
    # Time complexity: O(n)
    # Space complexity: O(1)

# ------------------------------------------------------------------------------------------------

# solution 1: using temporary array
def rotateArrayUsingTemporaryArray(arr, d):
    n = len(arr)
    temp = [0] * n
    for i in range(n):
        temp[i] = arr[i]
    for i in range(n):
        arr[i] = temp[(i + d) % n]
    return arr

# solution 2: using reverse algorithm
# Function to rotate an array by d elements to the left
def rotateArr(arr, d):
    n = len(arr)

    # Handle the case where d > size of array
    d %= n

    # Reverse the first d elements
    reverse(arr, 0, d - 1)

    # Reverse the remaining n-d elements
    reverse(arr, d, n - 1)

    # Reverse the entire array
    reverse(arr, 0, n - 1)
    return arr

# Function to reverse a portion of the array
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


# main function
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    d = 2
    print(arr)
    print("output using temporary array:", rotateArrayUsingTemporaryArray(arr, d))
    print("output using reverse algorithm:", rotateArr(arr, d))
