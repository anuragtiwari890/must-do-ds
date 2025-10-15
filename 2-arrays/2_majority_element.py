# problem link - https://www.geeksforgeeks.org/dsa/majority-element/

# Majority Element

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given an array of size n, find the majority element. The majority element is the element that appears more than n/2 times in the array.

# ------------------------------------------------------------------------------------------------

# Examples:

    # Input: arr[] = [1, 1, 2, 1, 3, 5, 1]
    # Output: 1
    # Explanation: Element 1 appears 4 times. Since ⌊7/2⌋ = 3, and 4 > 3, it is the majority element.

    # Input: arr[] = [7]
    # Output: 7
    # Explanation: Element 7 appears once. Since ⌊1/2⌋ = 0, and 1 > 0, it is the majority element.

    # Input: arr[] = [2, 13]
    # Output: -1
    # Explanation: No element appears more than ⌊2/2⌋ = 1 time, so there is no majority element.

# ------------------------------------------------------------------------------------------------
# approaches:
    # [Naive Approach] Using Two Nested Loops - O(n^2) Time and O(1) Space
    # [Better Approach - 1] Using Sorting - O(nlog(n)) Time and O(1) Space
    # [Better Approach - 2] Using Hashing - O(n) Time and O(n) Space
    # [Expected Approach] Using Moore's Voting Algorithm - O(n) Time and O(1) Space

# ------------------------------------------------------------------------------------------------
# [Better Approach - 2] Using Hashing - O(n) Time and O(n) Space
    # Step By Step Implementations:
        # Initialize an empty hash map.
        # Traverse the array and update the count of each element.
        # After each update, check if the count exceeds n / 2.
        # If found, return that element immediately.
        # If no such element exists after the loop, return -1.

# ------------------------------------------------------------------------------------------------
# [Expected Approach] Using Moore's Voting Algorithm - O(n) Time and O(1) Space
    # Step By Step Implementations:
        # This is a two-step process:
            # The first step gives the element that may be the majority element in the array. 
                # If there is a majority element in an array, then this step will definitely return majority element, otherwise, 
                # it will return candidate for majority element.
            # Check if the element obtained from the above step is the majority element. This step is necessary as there might be no majority element. 
    # Step By Step Approach:
        #Initialize a candidate variable and a count variable.
        # Traverse the array once:
            # -> If count is zero, set the candidate to the current element and set count to one.
            # -> If the current element equals the candidate, increment count.
            # -> If the current element differs from the candidate, decrement count.
        # Traverse the array again to count the occurrences of the candidate.
        # If the candidate's count is greater than n / 2, return the candidate as the majority element.


# solution:
def majorityElement(arr):

    n = len(arr)
    candidate = -1
    count = 0

    # Find a candidate
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # Validate the candidate
    count = 0
    for num in arr:
        if num == candidate:
            count += 1

    # If count is greater than n / 2, return 
    # the candidate; otherwise, return -1
    if count > n // 2:
        return candidate
    else:
        return -1

if __name__ == "__main__":
    
    arr = [1, 1, 2, 1, 3, 5, 1]
    print(majorityElement(arr))
    
    arr = [3,5,6,5,7,5]
    print(majorityElement(arr))

    arr = [3,5,6,5,7,5,5]
    print(majorityElement(arr))

    arr = [5,5,9,9,5] # good case to consider
    print(majorityElement(arr))

    arr = [7]
    print(majorityElement(arr))
    
    arr = [2, 13]
    print(majorityElement(arr))

