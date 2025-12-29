# problem link - https://www.geeksforgeeks.org/dsa/longest-prefix-also-suffix/

# Longest Prefix also Suffix

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    #Given a string s, find the length of the longest proper prefix which is also a suffix. 
    # A proper prefix is a prefix that doesn’t include whole string. 
    # For example, prefixes of "abc" are "", "a", "ab" and "abc" but proper prefixes are "", "a" and "ab" only.

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: s = "aabcdaabc"
    # Output: 4
    # Explanation: The string "aabc" is the longest proper prefix which is also the suffix.

    # Input: s = "ababab"
    # Output: 4
    # Explanation: The string "abab" is the longest proper prefix which is also the suffix.

    # Input: s = "aaaa"
    # Output: 3
    # Explanation: The string "aaa" is the longest proper prefix which is also the suffix.

# ------------------------------------------------------------------------------------------------

# approaches:
    # [Naive Approach] - Using Nested Loops - O(n^2) Time and O(1) Space
        # The idea is to use a nested loop to find the longest proper prefix which is also a suffix.
        # Time complexity: O(n^2)
        # Space complexity: O(1)
    
    # using two pointers - O(n) Time and O(1) Space
        # The idea is to use two pointers to find the longest proper prefix which is also a suffix.
        # maintain two pointers, i and j, next_index_to_start_with (charcter at thisindex will always be similar to charcter at 0).
        # whenever the matching fails for 2 pointers, we move to next_index_to_start_with and continue the process.
        # if we found the character at second pointer is same as first character of the string we store its index in next_index_to_start_with.
        # we set the next_index_to_start_with only once per iteration matching prefix and suffix.
        #  flow would be like this:
            # 1. i = 0,j = 1, next_index_to_start_with = None
            # while j < n:
            #     if s[i] == s[j]:
            #         i += 1
            #         j += 1
            #        if s[j] == s[0] and next_index_to_start_with is None:
            #            next_index_to_start_with = j
            #     else:
            #         if next_index_to_start_with is not None:
            #             j = next_index_to_start_with
            #         else:
            #             j += 1
            #         next_index_to_start_with = None
            #
            # now do a reverse travesal of i and j to test for prefix and suffix matching.
            # longest_prefix = ''
            # whiel i > 0
            #     if s[i] == s[j]:
            #         longest_prefix += s[i]
            #         i -= 1
            #         j -= 1
            #     else:
            #         return 'Not Found'
            # return longest_prefix

    



# ------------------------------------------------------------------------------------------------
# solution:
# using two pointers
def getLPSLength(s):
    n = len(s)  # Get the length of the input string

    # Initialize LPS array with 0s. lps[i] will store the length of the longest
    # proper prefix which is also a suffix for the substring s[0..i]
    lps = [0] * n

    # Initialize the length of the previous longest prefix-suffix
    len_ = 0

    # Pointer i starts from 1 (second character) as the LPS for the first character is always 0
    i = 1

    # Loop through the string starting from index 1 to n-1
    while i < n:
        # If the current character matches the character at the position of the previous
        # longest prefix-suffix, increment both the length and the pointer i
        if s[i] == s[len_]:
            len_ += 1        # Increment the length of the current prefix-suffix
            lps[i] = len_    # Store the length in the LPS array for index i
            i += 1           # Move to the next character
        else:
            # If there is a mismatch:
            if len_ != 0:
                # If len_ is not 0, fall back in the LPS array by setting len_ to the previous
                # longest prefix-suffix, i.e., try a shorter prefix-suffix
                len_ = lps[len_ - 1]
            else:
                # If len_ is 0, there is no proper prefix-suffix for this character, 
                # so set LPS[i] to 0 and move to the next character
                lps[i] = 0
                i += 1

    # Return the value of lps[n - 1], which gives the length of the longest 
    # proper prefix which is also a suffix for the entire string
    return lps[n - 1]


if __name__ == "__main__":
    s = "ababab"  # Example string
    print(getLPSLength(s))  # Output the result of the LPS computation
