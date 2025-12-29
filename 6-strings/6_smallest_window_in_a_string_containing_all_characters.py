# problem link - https://www.geeksforgeeks.org/dsa/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/

# Smallest window in a String containing all characters of other String

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given two strings s and p, the task is to find the smallest substring in s that contains all characters of p, including duplicates. 
    # If no such substring exists, return "". 
    # If multiple substrings of the same length are found, return the one with the smallest starting index.

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: s = "timetopractice", p = "toc"
    # Output: toprac
    # Explanation: "toprac" is the smallest substring in which "toc" can be found.

    # Input: s = "zoomlazapzo", p = "oza"
    # Output: apzo
    # Explanation: "apzo" is the smallest substring in which "oza" can be found.

# ------------------------------------------------------------------------------------------------

# approaches:
    # [Optimal Approach] - Using Sliding Window - O(n) Time and O(1) Space
        # The idea is to use Window Sliding (start and j) to maintain a sliding window over string S, while tracking character frequencies with two count arrays:
            # 1. Initialize:
                # A count array to store the frequency of characters in P.
                # Another count array to track the characters in the current window of S.
                # Variables to track the minimum window length and its start index.
            # 2. Expand the Window:
                # Move the j pointer through S, updating the window's character counts.
                # When all characters of P are present in the window, a valid window is found.
            # 3. Shrink the Window before updating result
                # Move the start pointer right to minimize the window while ensuring all characters from P remain in the window.
                # Track the smallest window during this process.
            # 4. Return Result:
                # If a valid window is found, return the smallest substring. If no valid window exists, return "-1".
        # Time complexity: O(n^2)
        # Space complexity: O(1)


# ------------------------------------------------------------------------------------------------
# solution:
def smallestWindow(s, p):
    len1 = len(s)
    len2 = len(p)

    if len1 < len2:
        return "-1"

    countP = [0] * 256
    countS = [0] * 256

    # Store occurrence of characters of P
    for char in p:
        countP[ord(char)] += 1

    start = 0
    start_idx = -1
    min_len = float('inf')
    count = 0

    for j in range(len1):
        
        # Count occurrence of characters of string S
        countS[ord(s[j])] += 1

        # If S's char matches with P's char, increment count
        if countP[ord(s[j])] != 0 and countS[ord(s[j])] <= countP[ord(s[j])]:
            count += 1

        # If all characters are matched
        if count == len2:
            
            # Try to minimize the window
            while countS[ord(s[start])] > countP[ord(s[start])] or countP[ord(s[start])] == 0:
                if countS[ord(s[start])] > countP[ord(s[start])]:
                    countS[ord(s[start])] -= 1
                start += 1

            # Update window size
            length = j - start + 1
            if min_len > length:
                min_len = length
                start_idx = start

    if start_idx == -1:
        return "-1"

    return s[start_idx:start_idx + min_len]

s = "timetopractice"
p = "toc"
res = smallestWindow(s, p)
print(res)