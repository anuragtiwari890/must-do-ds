# problem link - https://www.geeksforgeeks.org/dsa/roman-number-to-integer/

# Roman Number to Integer

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given a string s representing a Roman numeral, find it's corresponding integer value.
    # Roman numerals are formed using the following symbols: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, and M = 1000.
    # Numbers are typically formed by combining these symbols from left to right, adding or subtracting their values based on specific rules.

    # How does the conversion work?

    # If a smaller value symbol comes before, we subtract. Otherwise, we add.
    # In IV, I comes before V and V has a larger value 5. So our result is 5 - 1 = 4.
    # In VI, V comes before I and I has a smaller value 1. So our result is 5 + 1 = 6.
    # In II, we have same values, so we add and get 1 + 1 = 2
    # In case of more than 2 characters, we traverse from left to right and group only when we see a greater value character after a smaller value character. 
    # For example MXVII is 1000 + 10 + 5 + 1 + 1 = 1017. And XLVII is (50 - 10) + 5 + 1 + 1 = 47. Note that L is larger and comes after X.

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: s = "IX"
    # Output: 9
    # Explanation: IX is a Roman symbol which represents 10 - 1 = 9

    # Input: s = "XL"
    # Output: 40
    # Explanation: XL is a Roman symbol which represents 50 - 10 = 40

    # Input: s = "MCMIV"
    # Output: 1904
    # Explanation: M is 1000, CM is 1000 - 100 = 900, and IV is 4. So we have total as 1000 + 900 + 4 = 1904

# ------------------------------------------------------------------------------------------------

# approaches:
    # [Naive Approach] - Using HashMap - O(n) Time and O(1) Space
        # The idea is to use a hash map to store the Roman numeral symbols and their corresponding integer values.
        # We can use an hash map or dictionary to store the values of Roman symbols. 
        # And to solve the problem, we have to iterate through the string and for each symbol, 
        # check if the current value is less than the next value. 
        # If so, subtract the current value from the next value and add the result to the total. 
        # Otherwise, add the current value to the total.
        # Time complexity: O(n)
        # Space complexity: O(1) because we are using a hash map to store the values of Roman symbols.

# ------------------------------------------------------------------------------------------------
# solution:
def romanToDecimal(s):
    romanMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}

    res = 0
    i = 0
    while i < len(s):

        # if the current value is less than the next value, 
        # subtract current from next and add to res
        if i + 1 < len(s) and romanMap[s[i]] < romanMap[s[i + 1]]:
            res += romanMap[s[i + 1]] - romanMap[s[i]]

            # skip the next symbol
            i += 1
        else:

            # otherwise, add the current value to res
            res += romanMap[s[i]]
        i += 1

    return res

if __name__ == "__main__":
    s = "IX"
    print(romanToDecimal(s))
    s = "CXIV"
    print(romanToDecimal(s))