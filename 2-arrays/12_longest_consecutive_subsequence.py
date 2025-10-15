# problem link - https://www.geeksforgeeks.org/dsa/longest-consecutive-subsequence/

# Longest Consecutive Subsequence

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given an array of integers, the task is to find the length of the longest subsequence such that elements in the subsequence are consecutive 
    # integers, the consecutive numbers can be in any order. 

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: arr[] = {1, 9, 3, 10, 4, 20, 2}
    # Output: 4
    # Explanation: The subsequence 1, 3, 4, 2 is the longest subsequence of consecutive elements.

    # Input: arr[] = [1,1,1,2,2,3]
    # Output: 3
    # Explanation: The subsequence [1, 2,3] is the longest subsequence of consecutive elements.

# ------------------------------------------------------------------------------------------------

# approaches:
    # [Naive Approach] - using sorting - O(nlogn) Time and O(1) Space
        # The idea is to sort the array and then find the longest consecutive subsequence.
        # Time complexity: O(nlogn)
        # Space complexity: O(1)

    # [Expected Approach] - O(n) Time and O(n) Space
        # The idea is to use a hash map to store the elements and then find the longest consecutive subsequence.
        # Time complexity: O(n)
        # Space complexity: O(n)

# ------------------------------------------------------------------------------------------------

# solution:
# using sorting
def longestConsecutiveUsingSorting(arr):
    if not arr:
        return 0
    # Sort the array
    arr.sort()

    res = 1
    cnt = 1

    # Find the maximum length by traversing the array
    for i in range(1, len(arr)):
        
        # Skip duplicates
        if arr[i] == arr[i - 1]:
            continue

        # Check if the current element is equal
        # to previous element + 1
        if arr[i] == arr[i - 1] + 1:
            cnt += 1
        else:
            # Reset the count
            cnt = 1

        # Update the result
        res = max(res, cnt)

    return res

# using hash map

def longestConsecutiveUsingHashMap(arr):
    st = set()
    res = 0

    # Hash all the array elements
    for val in arr:
        st.add(val)

    # Check each possible sequence from the start 
    # then update length
    for val in arr:

        # If current element is the starting element of a sequence
        if val in st and (val - 1) not in st:

            # Then check for next elements in the sequence
            cur = val
            cnt = 0
            while cur in st:

                # Remove this number to avoid recomputation
                st.remove(cur)
                cur += 1
                cnt += 1

            # Update optimal length
            res = max(res, cnt)

    return res


if __name__ == "__main__":
    arr = [2, 6, 1, 9, 4, 5, 3]
    print(longestConsecutiveUsingSorting(arr))
    print(longestConsecutiveUsingHashMap(arr))


