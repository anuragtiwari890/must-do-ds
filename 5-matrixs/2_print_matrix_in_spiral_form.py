# problem link - https://www.geeksforgeeks.org/dsa/print-matrix-in-spiral-form/

# Print Matrix in Spiral Form

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given a matrix mat[][] of size m x n, the task is to print all elements of the matrix in spiral form.

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: mat[][] = [[1,   2,   3,   4],
    #                   [5,    6,   7,   8],
    #                   [9,   10,  11,  12],
    #                   [13,  14,  15,  16]]
    # Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

    # Input: mat[][] = [[1,   2,   3,   4],
    #                   [5,    6,   7,   8],
    #                   [9,   10,  11,  12],
    #                   [13,  14,  15,  16]]
    # Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

# ------------------------------------------------------------------------------------------------

# approaches:
    # [Approach] Using Simulation by Visited Matrix - O(m*n) Time and O(m*n) Space
        # The idea is to simulate the spiral traversal by marking the cells that have already been visited. 
        # We can use a direction array to keep track of the movement (right, down, left, up) and change direction when we hit the boundary or a visited cell.

        # Step By Step Implementations:

            # Initialize a 2D array vis[][] to keep track of visited cells.
            # Use direction arrays dr and dc to represent right, down, left, and up movements.
            # Start from the top-left cell and follow the direction arrays to visit each cell.
            # Change direction when encountering a boundary or a visited cell.
            # Continue until all cells are visited.

    # [Expected Approach] Using Boundary Traversal - O(m*n) Time and O(1) Space
        # We can print the matrix in a spiral order by dividing it into loops or boundaries. 
        # We print the elements of the outer boundary first, then move inward to print the elements of the inner boundaries.

        # Algorithm:
 
            # Define the boundaries of the matrix with variables top, bottom, left, and right.
            # Print the top row from left to right and increment top.
            # Print the right column from top to bottom and decrement right.
            # Check if boundaries have crossed; if not, print the bottom row from right to left and decrement bottom.
            # Print the left column from bottom to top and increment left.
            # Repeat until all boundaries are crossed.

# ------------------------------------------------------------------------------------------------

# solution:
def spirallyTraverse(mat):
    m, n = len(mat), len(mat[0])

    res = []

    # Initialize boundaries
    top, bottom, left, right = 0, m - 1, 0, n - 1

    # Iterate until all elements are printed
    while top <= bottom and left <= right:

        # Print top row from left to right
        for i in range(left, right + 1):
            res.append(mat[top][i])
        top += 1

        # Print right column from top to bottom
        for i in range(top, bottom + 1):
            res.append(mat[i][right])
        right -= 1

        # Print bottom row from right to left (if exists)
        if top <= bottom:
            for i in range(right, left - 1, -1):
                res.append(mat[bottom][i])
            bottom -= 1

        # Print left column from bottom to top (if exists)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(mat[i][left])
            left += 1

    return res


if __name__ == "__main__":
    mat = [[1, 2, 3, 4], 
           [5, 6, 7, 8], 
           [9, 10, 11, 12], 
           [13, 14, 15, 16]]

    res = spirallyTraverse(mat)
    print(" ".join(map(str, res)))