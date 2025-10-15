# problem link - https://www.geeksforgeeks.org/dsa/nth-natural-number-after-removing-all-numbers-consisting-of-the-digit-9/

# Nth natural number after removing all numbers consisting of the digit 9

# ------------------------------------------------------------------------------------------------

# problem statement:
    # Given a positive integer N, find the Nth natural number after removing all numbers consisting of the digit 9.

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: N = 8
    # Output: 8
    # Explanation:
    # Since 9 is the first natural number that contains the digit 9 and is the 9th natural number, therefore, no removal required to find the 8th natural number, which is 8.

    # Input: N = 9
    # Output: 10
    # Explanation:
    # Removing number 9, the first 9 natural numbers are {1, 2, 3, 4, 5, 6, 7, 8, 10}.
    # Therefore, the 9th natural number is 10.

# ------------------------------------------------------------------------------------------------

# Naive Approach:
    # This approach is to generate all natural numbers and then remove the numbers that contain the digit 9.
    # Then, return the Nth natural number.
    # Time complexity: O(N)
    # Space complexity: O(1)

# ------------------------------------------------------------------------------------------------

# Optimal Approach:
    # It is known that, digits of base 2 numbers varies from 0 to 1. Similarly, digits of base 10 numbers varies from 0 to 9.
    # Therefore, the digits of base 9 numbers will vary from 0 to 8.
    # It can be observed that Nth number in base 9 is equal to Nth number after skipping numbers containing digit 9.
    # So the task is reduced to find the base 9 equivalent of the number N.

    # This approach is to use the formula for the Nth natural number.
    # Time Complexity: O(log9 N)
    # Auxiliary Space: O(1)

    # Follow the steps below to solve the problem:
        # Initialize two variables, say res = 0 and p = 1, to store the number in base 9 and to store the position of a digit.
        # Iterate while N is greater than 0 and perform the following operations:
        # Update res as res = res + p*(N%9).
        # Divide N by 9 and multiply p by 10.
        # After completing the above steps, print the value of res.

# ------------------------------------------------------------------------------------------------

# Function to find Nth number in base 9
def findNthNumber(N):
  
    # Stores the Nth number
    result = 0
    p = 1

    # Iterate while N is
    # greater than 0
    while (N > 0):
      
        # Update result
        result += (p * (N % 9))

        # Divide N by 9
        N = N // 9

        # Multiply p by 10
        p = p * 10
    # Return result
    return result

# Driver Code
if __name__ == '__main__':
    N = 1999
    print(findNthNumber(N))