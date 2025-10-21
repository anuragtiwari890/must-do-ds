# problem link - https://www.geeksforgeeks.org/dsa/search-in-row-wise-and-column-wise-sorted-matrix/

# Search in row-wise and column-wise sorted matrix

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given a matrix mat[][] and an integer x, the task is to check if x is present in mat[][] or not. 
    # Every row and column of the matrix is sorted in increasing order.

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: x = 62, mat[][] = [[3, 30, 38],
                            #  [20, 52, 54],
                            #  [35, 60, 69]]
    # Output: false
    # Explanation: 62 is not present in the matrix.

    # Input: x = 55, mat[][] = [[18, 21, 27],
                            #  [38, 55, 67]]
    # Output: true
    # Explanation: mat[1][1] is equal to 55.

    # Input: x = 35, mat[][] = [[3, 30, 38],
                            #  [20, 52, 54],
                            #  [35, 60, 69]]
    # Output: true
    # Explanation: mat[2][0] is equal to 35.

# ------------------------------------------------------------------------------------------------
# approaches:
    # [Naive Approach] Comparing with all elements - O(n*m) Time and O(1) Space
        # The idea is to traverse through the matrix and compare the element with the target element.
        # If the element is found, return True.
        # If the element is not found, return False.
        # Time complexity: O(n*m)
        # Space complexity: O(1)

    # [Better Approach] Binary Search - O(n*logm) Time and O(1) Space
        # The idea is to use binary search on each rowto find the element in the matrix.
        # If the element is found, return True.
        # If the element is not found, return False.
        # Time complexity: O(n*logm)
        # Space complexity: O(1)

    # [Expected Approach] Staircase Search - O(n+m) Time and O(1) Space 
        # The idea Eliminating rows or columns.
        # The idea is to remove a row or column in each comparison until an element is found. 
        # Start searching from the top-right corner of the matrix. There are 3 possible cases:

            # x is greater than the current element: 
                # This ensures that all the elements in the current row are smaller than the given number 
                # as the pointer is already at the right-most element and the row is sorted. 
                # Thus, the entire row gets eliminated and continues the search from the next row. 
            # x is smaller than the current element: 
                # This ensures that all the elements in the current column are greater than the given number. 
                # Thus, the entire column gets eliminated and continues the search from the previous column, i.e. the column on the immediate left.
            # The given number is equal to the current number: This will end the search.
        # Time complexity: O(n+m)
        # Space complexity: O(1)

# ------------------------------------------------------------------------------------------------
# solution:
# Python program to search an element in row-wise
# and column-wise sorted matrix

def matSearch(mat, x):
    n = len(mat)
    m = len(mat[0])
    i = 0
    j = m - 1

    while i < n and j >= 0:
      
        # If x > mat[i][j], then x will be greater
        # than all elements to the left of 
        # mat[i][j] in row i, so increment i
        if x > mat[i][j]:
            i += 1
      
        # If x < mat[i][j], then x will be smaller
        # than all elements to the bottom of
        # mat[i][j] in column j, so decrement j
        elif x < mat[i][j]:
            j -= 1
      
        # If x = mat[i][j], return true
        else:
            return True

    # If x was not found, return false
    return False

if __name__ == "__main__":
    mat = [
        [3, 30, 38],
        [20, 52, 54],
        [35, 60, 69]
    ]
    x = 35
    if matSearch(mat, x):
        print("true")
    else:
        print("false")
