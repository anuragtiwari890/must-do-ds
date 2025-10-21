# problem link - https://www.geeksforgeeks.org/dsa/painters-partition-problem/

# Painters Partition Problem

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given an array arr[] and k, where the array represents the boards and each element of the given array represents the length of each board. 
    # k numbers of painters are available to paint these boards. 
    # Consider that each unit of a board takes 1 unit of time to paint. 
    # The task is to find the minimum time to get this job done by painting all the boards 
        # under the constraint that any painter will only paint the continuous sections of boards. 
        # say board [2, 3, 4] or only board [1] or nothing but not board [2, 4, 5].

# ------------------------------------------------------------------------------------------------

# Examples: 
    # Input: arr[] = [5, 10, 30, 20, 15], k = 3
    # Output: 35
    # Explanation: 
        # The most optimal way will be: 
        # Painter 1 allocation : [5,10], 
        # Painter 2 allocation : [30],
        #  Painter 3 allocation : [20, 15],
        #  Job will be done when all painters finish i.e. at time = max(5 + 10, 30, 20 + 15) = 35

    # Input: arr[] = [10, 20, 30, 40], k = 2
    # Output: 60
    # Explanation: The most optimal way to paint: 
        # Painter 1 allocation : [10, 20, 30], 
        # Painter 2 allocation : [40], 
        # Job will be complete at time = 60

# ------------------------------------------------------------------------------------------------
# approaches:
    # [Naive Approach] - Naive Approach - Using recursion
        # A brute force solution is to consider all possible sets of contiguous partitions and calculate the maximum sum partition in each case and 
        # return the minimum of all these cases. 
            # In this problem, we need to minimize the maximum time taken by any painter to complete their assigned boards. 
                # We have k painters who can work simultaneously. 
                # The recursive approach explores every possible way of dividing the boards among the painters 
                # and then selects the division that minimizes the maximum time.
            # The recursive function tries assigning boards from index curr to last index to each painter, 
            # then recursively computes the minimum time for the remaining boards and painters.

            # Recurrence Relation:
                # Let minTime(curr, k) represent the minimum time to paint the boards from curr to the end with k remaining painters. The recurrence relation is:
                # minTime(curr, k) = min {max(sum(curr, i) + minTime(i + 1, k - 1))}
            
            # Where:
            # sum(curr, i) is the total time for the current painter to paint boards from index curr to i where i can range from curr to n-1.
            # minTime(i + 1, k - 1) is the recursive call for the remaining boards and painters.
 
            # Base Cases:
            # No boards left (curr >= n): Return 0, as there’s nothing to paint.
            # No painters left (k == 0): Return infinity as it's infeasible to paint with no painters.


    # [Better Approach] - using DP Memoization
        #If we closely observe the recursive function minTime(), it exhibits the property of overlapping subproblems, 
        # where the same subproblem is solved repeatedly in different recursive paths. 
        # This redundancy can be avoided by applying memoization. 
        # Since the changing parameters in the recursive calls are the current index (curr) and the number of remaining painters (k), 
        # we can utilize a 2D array of size n x (k+1) to store the results. 
        # We initialize this array with -1 to signify that a value has not been computed yet, thus preventing redundant calculations.
        # Time complexity: O(n*n*k)
        # Space complexity: O(n*k) 


    # 
    
