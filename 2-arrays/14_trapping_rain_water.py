# problem link - https://www.geeksforgeeks.org/dsa/trapping-rain-water/

# Trapping Rain Water

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given an array arr[] of size n consisting of non-negative integers, 
    # where each element represents the height of a bar in an elevation map and the width of each bar is 1, 
    # determine the total amount of water that can be trapped between the bars after it rains.

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: arr[] = [3, 0, 1, 0, 4, 0, 2]
    # Output: 10
    # Explanation: The expected rainwater to be trapped is shown in the above image.

    # Input: arr[] = [3, 0, 2, 0, 4]
    # Output: 7
    # Explanation: We trap 0 + 3 + 1 + 3 + 0 = 7 units.

    # Input: arr[] = [1, 2, 3, 4]
    # Output: 0
    # Explanation: We cannot trap water as there is no height bound on both sides

# ------------------------------------------------------------------------------------------------

# Intuition
    # To trap water at any index in the elevation map, there must be taller bars on both its left and right sides.
    # The water that can be stored at each position is determined by the height of the shorter of the two boundaries (left and right), minus the height of the current bar.
    # We compute the trapped water at each index as: min(leftMax, rightMax) - height[i], if this value is positive.
    # The total trapped water is the sum of water stored at all valid indices.
    # If either side lacks a boundary, no water can be trapped at that position.

# ------------------------------------------------------------------------------------------------

# approaches:
    # [Naive Approach] - O(n^2) Time and O(1) Space
        # The idea is to traverse the array and for each element, find the maximum element to the left and right of the current element and calculate the trapped water.
        # Time complexity: O(n^2)
        # Space complexity: O(1)
        
    # [Better Approach] - O(n) Time and O(n) Space
        # In the previous approach, for every element we needed to calculate the highest element on the left and on the right. 
        # So, to reduce the time complexity:
            # => For every element we first calculate and store the highest bar on the left and on the right (say stored in arrays left[] and right[]).
            # => Then iterate the array and use the calculated values to find the amount of water stored in this index, 
            # which is the same as (min(left[i], right[i]) - arr[i])
        
        # illustration ->
            # Input: arr[] = [2, 1, 5, 3, 1, 0, 4, 1, 0]
            # left[] = [2, 2, 5, 5, 5, 5, 5, 5, 4]
            # right[] = [4, 4, 4, 4, 4, 4, 4, 1, 0]

            # 2. when left[i] <= right[i], then the water trapped at index i is left[i] - arr[i]
            # 3. when left[i] > right[i], then the water trapped at index i is right[i] - arr[i]
            # 4. the total water trapped is the sum of the water trapped at all indices

    # [Alternate Approach] Using Stack - O(n) Time and O(n) Space
        # This approach involves using next greater and previous greaterelements to solve the trapping rainwater problem. 
        # By utilizing a stack and a single traversal, we can compute both the next and previous greater elements for every item. 
        # For each element, the water trapped can be determined by the minimum height between the previous and next greater elements. 
        # The water is filled between these elements, and the process continues recursively with the next greater and previous greater elements. 

    # [Expected Approach] - Using Two Pointers - O(n) Time and O(1) Space
        # The approach is mainly based on the following facts:
            # 1. If we consider a subarray arr[left...right], we can decide the amount of water either for arr[left] or arr[right]
                # if we know the left max (max element in arr[0...left-1]) and right max (max element in arr[right+1...n-1]), 
                # then we can decide the amount of water either for arr[left] or arr[right]
            # 2. If left max is less than the right max, then we can decide for arr[left]. Else we can decide for arr[right]
            # 3. If we decide for arr[left], then the amount of water would be left max - arr[left] and if we decide for arr[right], 
                # then the amount of water would be right max - arr[right].

        # how does it works ->
            # Let us consider the case when left max is less than the right max. 
            # For arr[left], we know left max for it and we also know that the r
            # ight max for it would not be less than left max because we already have a greater value in arr[right...n-1]. 
            # So for the current bar, we can find the amount of water by finding the difference between the current bar and the left max bar.

# ------------------------------------------------------------------------------------------------

# solution: 
def maxWater(arr):
    left = 1
    right = len(arr) - 2

    # lMax : Maximum in subarray arr[0..left-1]
    # rMax : Maximum in subarray arr[right+1..n-1]
    lMax = arr[left - 1]
    rMax = arr[right + 1]

    res = 0
    while left <= right:
      
        # If rMax is smaller, then we can decide the 
        # amount of water for arr[right]
        if rMax <= lMax:
          
            # Add the water for arr[right]
            res += max(0, rMax - arr[right])

            # Update right max
            rMax = max(rMax, arr[right])

            # Update right pointer as we have decided 
            # the amount of water for this
            right -= 1
        else: 
          
            # Add the water for arr[left]
            res += max(0, lMax - arr[left])

            # Update left max
            lMax = max(lMax, arr[left])

            # Update left pointer as we have decided 
            # the amount of water for this
            left += 1
    return res

if __name__ == "__main__":
    arr = [2, 1, 5, 3, 1, 0, 4]
    print(maxWater(arr))

