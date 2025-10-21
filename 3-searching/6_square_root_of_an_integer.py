# problem link - https://www.geeksforgeeks.org/dsa/square-root-of-an-integer/

# Square Root of an Integer

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given an integer X, find its square root. If X is not a perfect square, then return floor(√X).

# ------------------------------------------------------------------------------------------------

# Examples:
# Input: n = 4
# Output: 2
# Explanation: The square root of 4 is 2.

# Input: n = 11
# Output: 3
# Explanation: The square root of 11 lies in between 3 and 4 so floor of the square root is 3.

# ------------------------------------------------------------------------------------------------

# approaches:
    # [Naive Approach] - O(n) Time and O(1) Space
        # The naive approach is to traverse the array and find the index of the given key.
        # Time complexity: O(n)
        # Space complexity: O(1)

    # [Expected Approach] - O(logn) Time and O(1) Space
        # The expected approach is to use binary search to find the index of the given key.
        # Time complexity: O(logn)
        # Space complexity: O(1)

    # [Expected Approach] Using Formula: O(1) Time and O(1) Space
    # Let's say square root of n is x:
        # => x = √n
    # Squaring both the sides:
        # => x2 =n
    # Taking log on both the sides:
        # => log(x2) = log(n)
        # => 2 × log(x) = log(n)
        # => log(x) = 1/2 × log(n)
    # To isolate x, exponentiate both sides with base e:
        # => x = e1/2 * log(n)
    # x is the square root of n:
        # => √n = e1/2 × log(n)

    # Because of the way computations are done in computers in case of decimals, the result from the expression may be slightly less than the actual square root. 
    # Therefore, we will also consider the next integer after the calculated result as a potential answer.

# ------------------------------------------------------------------------------------------------

# solution:
# Python program to find the square root of a number
# using binary search
import math


def floorSqrt(n):
    
    # initial search space
    lo = 1
    hi = n
    res = 1
    
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        
        # if square of mid is less than or equal to n 
        # update the result and search in upper half
        if mid * mid <= n:
            res = mid
            lo = mid + 1
            
        # if square of mid exceeds n, 
        # search in the lower half
        else:
            hi = mid - 1
    
    return res


def floorSqrtUsingFormula(n):
   
    # calculating square root using 
    # mathematical formula	
    res = int(math.exp(0.5 * math.log(n)))
    
    # If square of res + 1 is less than or equal to n
    # then, it will be our answer
    if (res + 1) ** 2 <= n:
        res += 1
    
    return res


if __name__ == "__main__":
    n = 11
    print(floorSqrt(n))
    print(floorSqrtUsingFormula(n))