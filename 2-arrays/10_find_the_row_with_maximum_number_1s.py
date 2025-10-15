# problem link - https://www.geeksforgeeks.org/dsa/find-the-row-with-maximum-number-1s/

# Find the row with maximum number of 1s

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given a binary 2D array, where each row is sorted. Find the row with the maximum number of 1s. 

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input matrix : 0 1 1 1
    #                0 0 1 1
    #                1 1 1 1 
    #                0 0 0 0

    
    # Output: 2
    # Explanation: Row = 2 has maximum number of 1s, that is 4.
    # Input matrix : 0 1 1 1
    #                0 0 1 1
    #                1 1 1 1 
    #                0 0 0 0

    # Output: 1
    # Explanation: Row = 1 has maximum number of 1s, that is 3.

# ------------------------------------------------------------------------------------------------

# approaches:
    # [Naive Approach] - O(r*c) Time and O(1) Space
        # The idea is to traverse the matrix for each row and count the number of 1s in each row.
        # Then return the row with the maximum number of 1s.

    # [Better Approach] - O(r*log(c)) Time and O(1) Space
        # The idea is to use binary search to find the first 1 in each row.
        # Then return the row with the maximum number of 1s.

    # [Expected Approach] Traversal from top-right to outside the grid - O(M + N) Time and O(1) Space:
        # Start from the top-right cell(row = 0, col = N - 1) and store the ans = -1. If the value in the current cell is 1, update ans with the current row and move left. Otherwise, if the current cell is 0, move to the next row:

        # If mat[row][col] == 1, update ans = row and move left by col = col - 1.
        # Else if mat[row][col] == 0, row = row + 1.
        # Continue, till we move outside the grid and return ans.    

# ------------------------------------------------------------------------------------------------

# Solution:

# Python3 program to find the row
# with maximum number of 1s

# Function that returns
# index of row with maximum
# number of 1s.
def rowWithMax1s(mat):
    R = len(mat)
    C = len(mat[0])
    max_row = -1
    row = 0
    col = C - 1

    # Move till we are inside the matrix
    while row < R and col >= 0:
        # If the current value is 0, move down to the next row
        if mat[row][col] == 0:
            row += 1
        # Else if the current value is 1, update max_row and move to the left column
        else:
            max_row = row
            col -= 1

    return max_row


# Driver Code
mat = [[0, 0, 0, 1],
       [0, 1, 1, 1],
       [1, 1, 1, 1],
       [0, 0, 0, 0]]
print("Index of row with maximum 1s is",
      rowWithMax1s(mat))