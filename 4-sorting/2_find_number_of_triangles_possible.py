# problem link - https://www.geeksforgeeks.org/dsa/find-number-of-triangles-possible/

# Find number of triangles possible

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given an array of positive integers arr[], 
    # count the number of triangles that can be formed with three different array elements as three sides of triangles.
    # Note: The sum of any two sides of a triangle must be greater than the third side.

# ------------------------------------------------------------------------------------------------

# Examples:
# Input: arr[] = [4, 6, 3, 7]
# Output: 3
# Explanation: There are three triangles possible [3, 4, 6], [4, 6, 7] and [3, 6, 7]. 
# Note that [3, 4, 7] is not a possible triangle.  

# Input: arr[] = [10, 21, 22, 100, 101, 200, 300]
# Output: 6
# Explanation: There can be 6 possible triangles: 
# [10, 21, 22], [21, 100, 101], [22, 100, 101], [10, 100, 101], [100, 101, 200] and [101, 200, 300]

# Input: arr[] = [1, 2, 3]
# Output: 0
# Examples: No triangles are possible.

# ------------------------------------------------------------------------------------------------
# approaches:
    # [Naive Approach] - Checking all Triplets - O(n^3) Time and O(1) Space
        # The naive approach is to try all possible combinations of three elements and check if they form a triangle.
        # Time complexity: O(n^3)
        # Space complexity: O(1)

    # [Better Approach] - Using Two Pointer - O(n^2) Time and O(1) Space
        # The idea is to sort the array to simplify checking the triangle inequality. 
        # Then, for each element (treated as the largest side), 
        # use two pointers technique to find count of pairs of smaller sides that can form a triangle with it. 
        # For this, the two pointers are initialized as: 
            # one pointer (left) starts at index 0, and the other pointer (right) is positioned just before the current largest side (arr[i]).

        # Now, compare the sum of arr[left] + arr[right] with the current largest side (arr[i]):
            # If the sum is greater than or equal to arr[i], a valid triangle can be formed. 
                # Count all valid pairs between left and right, then move the right pointer to the left to explore smaller side values.
            # If the sum is less than arr[i], increment the left pointer to increase the sum and check larger values.

        # Time complexity: O(n^2)
        # Space complexity: O(1)

# ------------------------------------------------------------------------------------------------
# solution:
# Python3 program to count number of triangles that can
# be formed with three different array elements as sides

def countTriangles(arr):
    res = 0
    arr.sort()

    # Iterate through the array, fixing 
    # the largest side at arr[i]
    for i in range(2, len(arr)):
      
        # Initialize pointers for the two smaller sides
        left, right = 0, i - 1

        while left < right:
            if arr[left] + arr[right] > arr[i]:
                # arr[left] + arr[right] satisfies the triangle inequality,
                # so all pairs (x, right) with (left <= x < right) are valid
                res += right - left

                # Move the right pointer to check smaller pairs
                right -= 1
                
            else:
                # Move the left pointer to increase the sum
                left += 1

    return res


if __name__ == "__main__":
    arr = [4, 6, 3, 7]
    print(countTriangles(arr))