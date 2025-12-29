# problem link - https://www.geeksforgeeks.org/dsa/reverse-words-in-a-given-string/

# Reverse Words in a Given String

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given a String S, reverse the string without reversing its individual words. Words are separated by dots.
    # For Example:
        # Input: S = i.like.this.program.very.much
        # Output: much.very.program.this.like.i
        # Explanation: After reversing the whole string(not individual words), the input string becomes: moc.yrev.much.si.elk.i
        # After reversing the individual words, the string becomes: much.very.program.this.like.i

    # Input: S = pqr.mno
    # Output: mno.pqr
    # Explanation: After reversing the whole string(not individual words), the input string becomes: cba.dcba
# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: s = "i.like.this.program.very.much" 
    # Output: much.very.program.this.like.i
    # Explanation: The words in the input string are reversed while maintaining the dots as separators, resulting in "much.very.program.this.like.i".

    # Input: s = ”..geeks..for.geeks.” 
    # Output: geeks.for.geeks

    # Input: s = "...home......"
    # Output: home

# ------------------------------------------------------------------------------------------------

# approaches:
    # [Naive Approach] - Using Extra Space
        # The idea is to use a stack to store the words in the string.
        # Then pop the words from the stack and append them to the result string.
        # Time complexity: O(n)
        # Space complexity: O(n)

    # [Expected Approach] Using Two Pointer - O(n) Time and O(1) Space
        # The idea is to use two pointers to reverse the words in the string.
        # The first pointer, i, starts at the beginning of the string and the second pointer, j, starts at the end of the string.
        # We swap the characters between the two pointers and move the pointers towards the center.
        # Time complexity: O(n)
        # Space complexity: O(1)

# ------------------------------------------------------------------------------------------------
# solution:
# approach 1: using extra space
def reverseWords(s):
  
    # reverse the whole string
    s = s[::-1]

    n = len(s)
    i = 0
    result = []

    l = 0
    while l < n:
        if s[l] != '.':
          
            # go to the beginning of the word
            if i != 0:
                result.append('.')
                i += 1

            # go to the end of the word
            r = l
            while r < n and s[r] != '.':
                result.append(s[r])
                i += 1
                r += 1

            # reverse the word
            result[i - (r - l):i] = reversed(result[i - (r - l):i])

            # move to the next word
            l = r
        l += 1

    return ''.join(result)


if __name__ == "__main__":
    s = "..geeks..for.geeks."
    print(reverseWords(s))


