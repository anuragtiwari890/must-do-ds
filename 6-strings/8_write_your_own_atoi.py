# problem link - https://www.geeksforgeeks.org/dsa/write-your-own-atoi/

# Write your own Atoi

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given a string s, convert it to an integer.
    # The string can contain leading spaces, trailing spaces, and other non-digit characters.
    # The string can contain a sign (+ or -).
    # The string can contain a decimal point.
    # The string can contain a number.
    # The string can contain a number.
    
# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: s = "-123"
    # Output: -123
    # 
    # Input: s = "   -"
    # Output: 0
    # Explanation: No digits are present, therefore 0.
    # 
    # Input: s = "  1231231231311133"
    # Output: 2147483647
    # Explanation: The converted number is greater than 231 - 1, therefore print 231 - 1 = 2147483647.
    # 
    # Input: s = "-999999999999"
    # Output: -2147483648
    # Explanation: The converted number is smaller than -231, therefore print -231 = -2147483648.
    # 
    # Input: s = "  -0012gfg4"
    # Output: -12
    # Explanation: Nothing is read after -12 as a non-digit character 'g' was encountered.

# ------------------------------------------------------------------------------------------------

# approaches:
    # Skip the leading whitespaces by iterating from the first character.
    # Now, check for at most one sign character ('+' or '-') and maintain a sign variable to keep track of the sign of the number.
    # Finally, read all the digits and construct the number until the first non-digit character is encountered or end of the input string is reached. 
    # While constructing the number, if the number becomes greater than 231 - 1, print 231 - 1. Similarly, if the number becomes less than -231, print -231.

    # How to check if the number is greater than 231 - 1 or smaller than -231 ?
        # The naive way is to use a data type which has size greater than 32 bits like long, BigInteger to store the number. 
        # However, we can also use 32-bit integer by appending the digits one-by-one and for each digit, 
        # check if appending current digit to the number will make it underflow (< -231) or overflow(> 231- 1). 
        # While appending a digit to the current number, we can have 3 cases:
            # Case 1: current number < (231 - 1)/10 or current number > -231/10: Simply append the digit to the current number as it won't cause overflow/underflow.
            # Case 2: current number > (231 - 1)/10 or current number < -231/10: Return (231 - 1) in case of overflow and -231 in case of underflow.
            # Case 3: current number = (231 - 1)/10 or current number = -231/10: In this case, if current number = (231 - 1)/10, 
                    # then only 0-7 digits can be appended and if current number = -231/10, then only 0-8 digits can be appended.


# ------------------------------------------------------------------------------------------------
# solution:
def myAtoi(s):
    sign = 1
    res = 0
    idx = 0
    n = len(s)

    # Ignore leading whitespaces
    while idx < n and s[idx] == ' ':
        idx += 1

    # Store the sign of number
    if idx < n and (s[idx] == '+' or s[idx] == '-'):
        if s[idx] == '-':
            sign = -1
        idx += 1

    # Construct the number digit by digit
    while idx < n and '0' <= s[idx] <= '9':
        digit = ord(s[idx]) - ord('0')
        res = 10 * res + digit

        # Handle overflow and underflow
        if res > 2**31 - 1:
            return (2**31 - 1) if sign == 1 else -2**31

        idx += 1

    return res * sign

if __name__ == "__main__":
    s = " -0012g4"
    print(myAtoi(s))