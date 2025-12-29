# problem link - https://www.geeksforgeeks.org/dsa/find-the-longest-substring-with-k-unique-characters-in-a-given-string/

# Longest substring with k unique characters

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given a string s and a non negative integer k, find the length of the longest substring that contains exactly k distinct characters.
    # If no such substring exists, return -1.
    
# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: s = "aabacbebebe", k = 3
    # Output: 7
    # Explanation: The longest substring with exactly 3 distinct characters is "cbebebe", which includes 'c', 'b', and 'e'.

    # Input: s = "aaaa", k = 2
    # Output: -1
    # Explanation: The string contains only one unique character, so there's no substring with 2 distinct characters.

    # Input: s = "aabaaab", k = 2
    # Output: 7
    # Explanation: The entire string "aabaaab" has exactly 2 unique characters 'a' and 'b', making it the longest valid substring.

# ------------------------------------------------------------------------------------------------

# approaches:
    # [Expected Approach]Sliding Window with Frequency Count - O(n) Time and O(1) Space
        # This approach uses the sliding window technique with two pointers to maintain a dynamic window of characters. 
        # A frequency array tracks how many times each character appears, while a counter keeps track of the number of unique characters in the window. 
        # If the count exceeds k, the window is shrunk from the left. The maximum window length with exactly k unique characters is updated during traversal.

        # Step by Step Approach:
            # Start with two pointers i and j (window start and end). 
            # Expand the window by moving j and include each character in a frequency array of size 26 (for lowercase a–z).
            # Keep a counter cnt that tracks how many unique characters are currently in the window. Increment cnt when a character appears for the first time.
            # If the number of unique characters exceeds k, move the start pointer i forward (shrinking the window from the left), 
            # and update the frequency and cnt ( decrease the value of cnt if it is the last occurrence of that character ) accordingly.
            # Whenever the number of unique characters in the window is exactly k, update the maximum length found so far.

        # Time complexity: O(n)
        # Space complexity: O(1)


# ------------------------------------------------------------------------------------------------
# solution:
def longestKSubstr(s, k):
    n = len(s)
    i = 0
    j = 0
    cnt = 0
    maxi = -1
    fre = [0] * 26
    
    # cnt represents the number of
    # unique characters in the current window

    while j < n:

        # include s[j] into the window
        fre[ord(s[j]) - ord('a')] += 1

        # it is the first occurrence of 
        # this character in the window
        if fre[ord(s[j]) - ord('a')] == 1:
            cnt += 1

        # shrink the window if the number of
        # unique character is more than k
        while cnt > k:
            fre[ord(s[i]) - ord('a')] -= 1

            # one unique character removed
            if fre[ord(s[i]) - ord('a')] == 0:
                cnt -= 1
            i += 1

        # we have exactly k unique characters
        if cnt == k:
            maxi = max(maxi, j - i + 1)

        j += 1

    return maxi

if __name__ == "__main__":
    s = "aabacbebebe"
    k = 3
    print(longestKSubstr(s, k))