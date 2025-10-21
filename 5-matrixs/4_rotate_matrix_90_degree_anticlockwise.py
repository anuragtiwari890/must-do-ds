# problem link - https://www.geeksforgeeks.org/dsa/rotate-matrix-90-degree-without-using-extra-space-set-2/

# Rotate Matrix 90 degree anticlockwise

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given an image represented by m x n matrix, rotate the image by 90 degrees in counterclockwise direction. 
    # Please note the dimensions of the result matrix are going to n x m for an m x n input matrix.

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input:
        # 1    2    3   4
        # 5   6    7   8  
        # 9  10   11  12
        # 13  14  15  16  
    # Output:
        # 4  8  12  16 
        # 3  7  11   15 
        # 2  6  10  14
        # 1   5  9   13
# 
    # Input:
        # 1  2  3  4 
        # 5  6  7  8 
        # 9 10 11 12 
    # Output:
        # 4  8  12 
        # 3  7  11 
        # 2  6  10 
        # 1  5  9

# ------------------------------------------------------------------------------------------------

# approaches:
    # [Approach 1] - Using Extra Space
        # [Best Approach] – O(m x n) Time
            # We mainly need to move first row elements to first column in revers order, second row elements to second column in reverse order.

            # Let us first try to find out a pattern to solve the problem for n = 4 (second example matrix above)

                # mat[0][0] goes to mat[3][0]
                # mat[0][1] goes to mat[2][0]
                # ………………………………………
                # mat[1][0] goes to mat[3][1]
                # ……………………………………..
                # mat[3][3] goes to mat[0][3]

            # Do you see a pattern? Mainly we need to move mat[i][j] to mat[n-j-1][i].

        # [Alternate Approach] – O(m x n) Time
            # When you think about rotating a matrix 90 degrees counterclockwise, each element moves to a new position. 
            # The top row becomes the leftmost column, the second row becomes the second-left column, and so forth. 
            # If we first transpose the matrix, and then reverse individual columns, we get the desired result.

            # Follow the given steps to solve the problem:

            # Perform Transpose of the matrix
            # Reverse Individual Columns

        # Time Complexity: O(m*n)
        # Space Complexity: O(m+n)

# ------------------------------------------------------------------------------------------------

# solution:
def rotate_matrix(mat):
    m, n = len(mat), len(mat[0])
    res = [[0] * m for _ in range(n)]

    # Transpose the matrix
    for i in range(m):
        for j in range(n):
            res[j][i] = mat[i][j]

    # Reverse each column (not row) of the result which is a n x m matrix
    for j in range(m):
        for i in range(n // 2):
            res[i][j], res[n - i - 1][j] = res[n - i - 1][j], res[i][j]

    return res

if __name__ == "__main__":
    mat = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    res = rotate_matrix(mat)

    for row in res:
        print(" ".join(map(str, row)))