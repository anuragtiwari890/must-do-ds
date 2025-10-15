# problem link - https://www.geeksforgeeks.org/dsa/represent-the-fraction-of-two-numbers-in-the-string-format/

# Fraction to Recurring Decimal

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
    # If the fractional part is repeating, enclose the repeating part in parentheses.
    # If the fractional part is non-repeating, return the string without parentheses.

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: a = 1, b = 2
    # Output: "0.5"
    # Explanation: 1/2 = 0.5 with no repeating part.

    # Input: a = 50, b = 22
    # Output: "2.(27)"
    # Explanation: 50/22 = 2.27272727... Since fractional part (27) is repeating, it is enclosed in parentheses.

# ------------------------------------------------------------------------------------------------

# Naive Approach: Using String
    # This approach is to convert the fraction to a string and then check if the fractional part is repeating.
    # If it is repeating, enclose the repeating part in parentheses.
    # If it is non-repeating, return the string without parentheses.
    # Time complexity: O(n)
    # Space complexity: O(n)

# ------------------------------------------------------------------------------------------------

# Optimal Approach: Using Hash Map
    # This approach is to use a hash map to store the remainder and the index of the fractional part.
    # If the remainder is already in the hash map, then the fractional part is repeating.
    # If the remainder is not in the hash map, then the fractional part is non-repeating.

    # Explanation:
        # The idea is to first calculate the integral quotient (absolute part before decimal point) and then calculate the fractional part. 
        # To check if the fractional part is repeating, insert the remainder (a % b) in a hash map with key as remainder 
        # and value as the index position at which this remainder occurs. If at any point of time, the remainder becomes zero, 
        # then there doesn't exist a repeating fraction otherwise if the remainder is already found in the map, then there exists a repeating fraction.

    # Time complexity: O(n)
    # Space complexity: O(n)

# ------------------------------------------------------------------------------------------------

# solution:
def fractionToDecimal(a, b):
    # Edge Case : If the fraction is a whole number, return the string without parentheses.
    if a % b == 0:
        return str(a // b)
    res = ""

    # If the fraction is a negative fraction, add a negative sign to the result.
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        res += "-"

    # Convert the fraction to a positive fraction.
    a = abs(a)
    b = abs(b)

    # Add the whole number part to the result. 
    res += str(a // b) # typecast to string because we are concatenating a string with an integer

    # Add the fractional part to the result.
    rem = a % b

    # If completely divisible, return res
    if rem == 0:
        return res
    
    # Add the fractional part to the result.
    mp = {}

    # If the remainder is not 0, then the fractional part is repeating.
    while rem > 0:
      
        # If this remainder is already seen,
        # then there exists a repeating fraction.
        if rem in mp:

            # Add parentheses to the repeating part.
            # res[:mp[rem]] is the part before the repeating part
            # res[mp[rem]:] is the repeating part
            # res[:mp[rem]] + "(" + res[mp[rem]:] + ")" is the result with parentheses
            res = res[:mp[rem]] + "(" + res[mp[rem]:] + ")"  
            break
        
        # If the remainder is seen for the first time,
        # store its index
        mp[rem] = len(res)

        rem = rem * 10

        # Calculate quotient, append it to result and
        # calculate next remainder
        res += str(rem // b)
        rem = rem % b
    
    # Return the result.
    return res


if __name__ == "__main__":
    a = 100
    b = 8
    print(fractionToDecimal(a, b))