# problem link - https://www.geeksforgeeks.org/dsa/find-the-missing-number/

# Find the Missing Number

# Problem Statement:

# Given an array arr[] of size n-1 with distinct integers in the range of [1, n]. 
# This array represents a permutation of the integers from 1 to n with one element missing. Find the missing element in the array.

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: arr[] = [8, 2, 4, 5, 3, 7, 1]
    # Output: 6
    # Explanation: All the numbers from 1 to 8 are present except 6.

    # Input: arr[] = [1, 2, 3, 5]
    # Output: 4
    # Explanation: Here the size of the array is 4, so the range will be [1, 5]. The missing number between 1 to 5 is 4

# ------------------------------------------------------------------------------------------------

# Naive Approach:
    # This approach iterates through each number from 1 to n (where n is the size of the array + 1) 
    # and checks if the number is present in the array. For each number, it uses a nested loop to search the array.
    #  If a number is not found, it is returned as the missing number. This approach has a time complexity of O(n^2).

# ------------------------------------------------------------------------------------------------

# Native approach 2:
    # sort the array and then find the missing number
    # time complexity: O(nlogn)
    # space complexity: O(1)

# ------------------------------------------------------------------------------------------------

# Optimal Approach 1:
    # This approach uses the formula for the sum of the first n natural numbers: n*(n+1)/2.
    # It calculates the sum of the array elements and subtracts it from the sum of the first n natural numbers.
    # The difference is the missing number. This approach has a time complexity of O(n).
    # drawback: This approach can cause integer overflow if the array contains large numbers.

# Code:
# def find_missing_number(arr):
#     n = len(arr) + 1
#     total_sum = n*(n+1)//2
#     return total_sum - sum(arr)

# ------------------------------------------------------------------------------------------------

# optimal_approach 2:
    # [Expected Approach 2] Using XOR Operation - O(n) Time and O(1) Space Complexity
    # This approach uses the XOR operation to find the missing number.
    # XOR operation has a property where a number XORed with itself is 0 and a number XORed with 0 is the number itself.
    # This approach has a time complexity of O(n) and a space complexity of O(1).

# ------------------------------------------------------------------------------------------------


# solution 1: using sum of n natural numbers
def missingNum(arr):
    n = len(arr) + 1

    # Calculate the sum of array elements
    totalSum = sum(arr)

    # Calculate the expected sum
    expSum = n * (n + 1) // 2

    # Return the missing number
    return expSum - totalSum

# ------------------------------------------------------------------------------------------------

# solution 2: using XOR operation
def missingNumXOR(arr):
    n = len(arr) + 1
    xor1 = 0
    xor2 = 0

    # XOR all array elements
    for i in range(n - 1):
        xor2 ^= arr[i]

    # XOR all numbers from 1 to n
    for i in range(1, n + 1):
        xor1 ^= i

    # Missing number is the XOR of xor1 and xor2
    return xor1 ^ xor2


if __name__ == '__main__':
    arr = [8, 2, 4, 5, 3, 7, 1]
    res = missingNumXOR(arr)
    print(res)
