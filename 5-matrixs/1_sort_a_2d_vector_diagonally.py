# problem link - https://www.geeksforgeeks.org/dsa/sort-a-2d-vector-diagonally/

# Sort a 2D Vector Diagonally

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given a 2D vector of NxM integers. The task is to sort the elements of the vectors diagonally from top-left to bottom-right in decreasing order.

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: arr[][] = { { 10, 2, 3 }, { 4, 5, 6 }, {7, 8, 9 } } 
    # Output: 
    # 10 6 3 
    # 8 9 2 
    # 7 4 5
    # Input: arr[][] = { { 10, 2, 43 }, { 40, 5, 16 }, { 71, 8, 29 }, {1, 100, 5} } 
    # Output: 
    # 29 16 43 
    # 40 10 2 
    # 100 8 5 
    # 1 71 5 

# ------------------------------------------------------------------------------------------------

# approaches:
    # [Naive Approach] - Sort all the element of matrix
        # use new 1D array to store all the elements of matrix
        # sort the 1D array
        # store the sorted elements back to the matrix
    # [Better Approach] - Sort the elements of the matrix diagonally
        # sort only the diagonals elements of matrix
        # space complexity: O(1)

# ------------------------------------------------------------------------------------------------
# solution:
# approach 1: using naive approach
def sortMatrixDiagonally(matrix):
    n = len(matrix)
    m = len(matrix[0])
    arr = [0] * (n * m)
    for i in range(n):
        for j in range(m):
            arr[i * m + j] = matrix[i][j]
    # sort in reverse order
    arr.sort(reverse=True)
    for i in range(n):
        for j in range(m):
            matrix[i][j] = arr[i * m + j]
    return matrix

if __name__ == "__main__":
    arr = [[10, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(sortMatrixDiagonally(arr))