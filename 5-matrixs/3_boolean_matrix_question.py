# problem link - https://www.geeksforgeeks.org/dsa/a-boolean-matrix-question/

# A Boolean Matrix Question

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given a boolean matrix mat where each cell contains either 0 or 1, 
    # the task is to modify it such that if a matrix cell matrix[i][j] is 1 then all the cells in its ith row and jth column will become 1.

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: [[1, 0],
    #        [0, 0]]
    # Output: [[1, 1],
    #         [1, 0]]

    # Input: [[1, 0, 0, 1],
    #         [0, 0, 1, 0],
    #         [0, 0, 0, 0]]
    # Output: [[1, 1, 1, 1],
    #          [1, 1, 1, 1],
    #          [1, 0, 1, 1]]

# ------------------------------------------------------------------------------------------------

# approaches:
    # [Approach 1] - [Naive Approach] By Marking the Matrix
        # Assuming all the elements in the matrix are non-negative. T
        # raverse through the matrix and if you find an element with value 1, then change all the zeros in its row and column to -1.
        #  The reason for not changing other elements to 1, but -1, is because that might affect other columns and rows.
        # Finally, traverse the matrix and change all -1 to 1.
        # Time Complexity: O((n * m)*(n + m)) where n is number of rows and m is number of columns in given matrix.
            # O(n * m) for traversing through each element and (n+m) for traversing to row and column of matrix elements having value 1.
        # Space complexity: O(1)
            

    # [Better Approach] Using Extra Space
        # The idea is to use two temporary arrays, rowMarker[] and colMarker[], to keep track of which rows and columns need to be updated. 
        # Following are the steps for this approach

            # Create two temporary arrays rowMarker[] and colMarker[]. Initialize all values of rowMarker[] and colMarker[] as 0. 
            # Traverse the input matrix mat[][]. If you finds mat[i][j] as 1, then mark rowMarker[i] and colMarker[j] as true. 
            # Traverse the input matrix mat[][] again. For each entry mat[i][j], check the values of rowMarker[i] and colMarker[j]. 
            # If any of the two values (rowMarker[i] or colMarker[j]) is true, then mark mat[i][j] as 1.

        # Time Complexity: O(m*n)
        # Space Complexity: O(m+n)

    # [Expected Approach] Without Using Extra Space
        # Instead of taking two dummy arrays we can use the first row and first column of the matrix for the same work. 
        # This will help to reduce the space complexity of the problem. 
        # While traversing for the second time, the first row and column will be computed first, which will affect the values of further elements. 
        
        # So we traverse in the reverse direction.
        # Since matrix[0][0] are overlapping in first row and first column. 
        # Therefore take separate variable col0 (say) to check if the 0th column has 1 or not and use matrix[0][0] to check if the 0th row has 1 or not. 
        # Now traverse from the last element to the first element and check if matrix[i][0]==1 || matrix[0][j]==1 and if true set matrix[i][j]=1, else continue.

# ------------------------------------------------------------------------------------------------
# 
# solution:
# python3 Code For Boolean Matrix Question
# Most Optimised Approach
def booleanMatrix(mat):
    col0 = 0
    rows = len(mat)
    cols = len(mat[0])

    # Step 1: Mark the first row and column
    # if there is a 1 in the matrix
    for i in range(rows):
      
        # Check if 0th column contains 1
        if mat[i][0] == 1:
            col0 = 1  
        for j in range(1, cols):
            if mat[i][j] == 1:
                mat[i][0] = 1  
                mat[0][j] = 1  

    # Step 2: Traverse the matrix in reverse
    # direction and update values
    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, 0, -1):
            if mat[i][0] == 1 or mat[0][j] == 1:
                mat[i][j] = 1  
        if col0 == 1:
            mat[i][0] = 1 

if __name__ == "__main__":
    arr = [
        [1, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 0, 0, 0]
    ]
    
    booleanMatrix(arr)
    
    for row in arr:
        print(" ".join(map(str, row)))




