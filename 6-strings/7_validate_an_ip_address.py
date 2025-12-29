# problem link - https://www.geeksforgeeks.org/dsa/program-to-validate-an-ip-address/

# Validate an IP Address

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given a string IP, task is to check if the IP is valid. The validity of an IP address is defined as follows:
    # An IP address is a string in the form "a.b.c.d" where a, b, c, and d are integers in the range 0 to 255.
    # Leading zeros are not allowed in any of the four integers.
    # The string can be broken into 4 integers in the range 0 to 255.
    # The string is said to be valid if it contains only digits, no leading zeros, no extra leading zeros, and no extra trailing zeros.
    # The string is said to be invalid if it contains any other characters except digits and dots.

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: IP = "192.168.1.1"
    # Output: Valid
    # Explanation: The IP address is in the form "a.b.c.d" where a, b, c, and d are integers in the range 0 to 255.
    # The string contains only digits, no leading zeros, no extra leading zeros, and no extra trailing zeros.
    # The string is said to be valid.

    # Input: IP = "192.168.1.1.1"
    # Output: Invalid
    # Explanation: The IP address is not in the form "a.b.c.d" where a, b, c, and d are integers in the range 0 to 255.

# ------------------------------------------------------------------------------------------------

# approaches:
    # [Optimal Approach] - Using Regex - O(1) Time and O(1) Space
        # The idea is to use a regex to check if the IP address is valid.
        # The regex is a.b.c.d where a, b, c, and d are integers in the range 0 to 255.
        # The regex is a.b.c.d where a, b, c, and d are integers in the range 0 to 255.

# ------------------------------------------------------------------------------------------------
# solution:
def isValidIP(ip):
    # split the IP address into its four parts
    parts = ip.split('.')
    # check if there are exactly four parts
    if len(parts) != 4:
        return False
    # check if each part is an integer in the range 0 to 255
    for part in parts:
        if not part.isdigit() or int(part) < 0 or int(part) > 255:
            return False
    return True

# test cases
print(isValidIP("192.168.1.1"))
print(isValidIP("192.168.1.1.1"))
print(isValidIP("192.168.1.1.1.1"))
print(isValidIP("192.168.1.1.1.1.1"))
print(isValidIP("192.168.1.1.1.1.1.1"))
print(isValidIP("192.168.1.1.1.1.1.1.1"))
print(isValidIP("192.168.1.1.1.1.1.1.1.1"))
print(isValidIP("192.168.1.1.1.1.1.1.1.1.1"))
print(isValidIP("192.168.1.1.1.1.1.1.1.1.1.1"))
