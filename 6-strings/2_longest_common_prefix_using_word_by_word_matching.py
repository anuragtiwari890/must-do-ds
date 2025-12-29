# problem link - https://www.geeksforgeeks.org/dsa/longest-common-prefix-using-word-by-word-matching/

# Longest Common Prefix using Word by Word Matching

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given a list of N strings, the task is to find the longest common prefix among all the strings present in the list.

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: arr[] = [“geeksforgeeks”, “geeks”, “geek”, “geezer”]
    # Output: "gee"
    # Explanation: “gee” is the longest common prefix in all the given strings: "geeksforgeeks", "geeks", "geeks" and "geezer".

    # Input: arr[] = ["apple", "ape", "april"]
    # Output : "ap"
    # Explanation: “ap” is the longest common prefix in all the given strings: "apple", "ape" and "april".

    # Input: arr[] = [“hello”, “world”]
    # Output: ""
    # Explanation: There’s no common prefix in the given strings.

# ------------------------------------------------------------------------------------------------

# approaches:
    # [Approach] - using LCP
        # the idea is to find the shortest string in the list and then compare it with the other strings in the list.
        # the compare it by each strings characters one by one.
        # extract the common prefix while comparing the strings

# ------------------------------------------------------------------------------------------------
# solution:
#  using LCP using shortest string
def longestCommonPrefix(arr):
    if not arr:
        return ""
    shortest = min(arr, key=len)
    for i, char in enumerate(shortest):
        for other in arr:
            if other[i] != char:
                return shortest[:i]
    return shortest

if __name__ == "__main__":
    arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
    print(longestCommonPrefix(arr))

    arr = ["apple", "ape", "april"]
    print(longestCommonPrefix(arr))

    arr = ["hello", "world"]
    print(longestCommonPrefix(arr))

    
    
        

