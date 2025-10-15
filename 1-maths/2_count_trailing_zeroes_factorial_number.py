# problem link - https://www.geeksforgeeks.org/dsa/count-trailing-zeroes-factorial-number/

# Count Trailing Zeroes in Factorial of a Number

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given an integer n, we have to returns count of trailing zeroes in n! . 

# ------------------------------------------------------------------------------------------------

# Examples : 

    # Input: n = 5
    # Output: 1 
    # Explanation: Factorial of 5 is 120 which has one trailing 0.

    # Input: n = 10
    # Output: 2
    # Explanation: Factorial of 10  is 3628800 which have 2 trailing zeroes.

# ------------------------------------------------------------------------------------------------

# Naive Approach:
    # This approach is to calculate the factorial of the number and then count the trailing zeroes.
# Time complexity: O(n)
# Space complexity: O(1)

# ------------------------------------------------------------------------------------------------

# Optimal Approach:
# This approach is to count the number of 5s in the factors of the number.
# Explanation: 
    # The number of trailing zeroes in n! is the number of times 10 is a factor in the number.
    # 10 is the product of 2 and 5. So, we need to count the number of 5s in the factors of the number.
    # We can do this by dividing the number by 5, 25, 125, etc. and adding the quotient to the count.
    # For example, for 10, we have 2 trailing zeroes because 10/5 = 2.
    # For 25, we have 6 trailing zeroes because 25/5 = 5 and 5/5 = 1.
    # For 50, we have 12 trailing zeroes because 50/5 = 10 and 10/5 = 2 and 2/5 = 0.
    # For 62, we have 14 trailing zeroes because 62/5 = 12 and 12/5 = 2 and 2/5 = 0.
    # For 125, we have 31 trailing zeroes because 125/5 = 25 and 25/5 = 5 and 5/5 = 1.
    # For 625, we have 156 trailing zeroes because 625/5 = 125 and 125/5 = 25 and 25/5 = 5 and 5/5 = 1.

# Time complexity: O(logn)
# Space complexity: O(1)

# ------------------------------------------------------------------------------------------------

def factorialTrailingZeroes(n):
    
    # Edge Case
    if (n < 0):
        return -1

    # Initialize result
    count = 0

    # Keep dividing n by
    # 5 & update Count
    while (n >= 5):
        # divide n by 5 and update count
        n = n//5    # // is used to floor the result
        count += n

    return count


if __name__ == "__main__":
    n = 62
    print(factorialTrailingZeroes(n))