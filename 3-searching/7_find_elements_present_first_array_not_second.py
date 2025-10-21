# problem link - https://www.geeksforgeeks.org/dsa/find-elements-present-first-array-not-second/

# Find elements which are present in first array and not in second

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given two arrays, the task is that we find numbers which are present in first array, but not present in the second array. 

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input : 
        # a[] = {1, 2, 3, 4, 5, 10};
        # b[] = {2, 3, 1, 0, 5};
    # Output : 4 10    
    # 4 and 10 are present in first array, but
    # not in second array.

    # Input : 
        # a[] = {4, 3, 5, 9, 11};
        # b[] = {4, 9, 3, 11, 10};
    # Output : 5  

# ------------------------------------------------------------------------------------------------

# approaches:
    # [Naive Approach] - O(n*m) Time and O(1) Space
        # The naive approach is to traverse the first array and check if the element is present in the second array.
        # If it is not present, then we print the element.
        # Time complexity: O(n*m)
        # Space complexity: O(1)

    # [Expected Approach] - Method 2 (Use Hashing): 
        # In this method, we store all elements of second array in a hash table (unordered_set). 
        # One by one check all elements of first array and print all those elements which are not present in the hash table.

# ------------------------------------------------------------------------------------------------
# solution:

# Python3 efficient program to find elements 
# which are not present in second array

# Function for finding elements which 
# are there in a[] but not in b[].
def findMissing(a, b, n, m):
    
    # Store all elements of second 
    # array in a hash table
    s = dict()
    for i in range(m):
        s[b[i]] = 1

    # Print all elements of first array 
    # that are not present in hash table
    for i in range(n):
        if a[i] not in s.keys():
            print(a[i], end = " ")

# Driver code
a = [ 1, 2, 6, 3, 4, 5 ]
b = [ 2, 4, 3, 1, 0 ]
n = len(a)
m = len(b)
findMissing(a, b, n, m)