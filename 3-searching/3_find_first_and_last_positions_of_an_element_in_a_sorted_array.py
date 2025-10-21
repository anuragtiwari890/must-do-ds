# problem link - https://www.geeksforgeeks.org/dsa/find-first-and-last-positions-of-an-element-in-a-sorted-array/

# Find First and Last Positions of an Element in a Sorted Array

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given a sorted array of integers arr[] of size N and an integer X, 
    # the task is to find the first and last position of X in the array. If X is not present in the array, then return [-1, -1].

# ------------------------------------------------------------------------------------------------

# Examples:
# Input: arr[] = {1, 3, 5, 5, 5, 5, 7, 123, 125}, X = 5
# Output: First Occurrence = 2, Last Occurrence = 5

# Input: arr[] = {1, 3, 5, 5, 5, 5, 7, 123, 125}, X = 7
# Output: First Occurrence = 6, Last Occurrence = 6

# Input: arr[] = {1, 3, 5, 5, 5, 5, 7, 123, 125}, X = 123
# Output: First Occurrence = 7, Last Occurrence = 7

# Input: arr[] = {1, 3, 5, 5, 5, 5, 7, 123, 125}, X = 125
# Output: First Occurrence = 8, Last Occurrence = 8

# ------------------------------------------------------------------------------------------------

# approaches:
    # [Naive Approach] - O(n) Time and O(1) Space
        # The naive approach is to traverse the array and find the first and last position of X.
        # Time complexity: O(n)
        # Space complexity: O(1)

    # [Expected Approach] - O(logn) Time and O(1) Space
        # The expected approach is to use binary search to find the first and last position of X.
        # Follow the below given approach:

        # 1. For the first occurrence of a number 
            # If (high >= low): Calculate  mid = low + (high - low)/2;
            # If ((mid == 0 || x > arr[mid-1]) && arr[mid] == x): return mid
            # Else if (x > arr[mid]): return first(arr, (mid + 1), high, x, n);
            # Else: return first(arr, low, (mid -1), x, n);
            # Otherwise: return -1;

        # 2. For the last occurrence of a number 
            # if (high >= low): calculate mid = low + (high - low)/2;
            # if( ( mid == n-1 || x < arr[mid+1]) && arr[mid] == x ): return mid;
            # else if(x < arr[mid]): return last(arr, low, (mid -1), x, n);
            # else: return last(arr, (mid + 1), high, x, n);
            # otherwise: return -1;
            # Time complexity: O(logn)
            # Space complexity: O(1)

# ------------------------------------------------------------------------------------------------

#solution:

# Function for finding first and last occurrence of x
def findLast(arr, x):
    n = len(arr)
    
    # Initialize low and high index
    # to find the last occurrence
    low = 0
    high = n - 1
    
    # Initialize last occurrence
    last = -1
    
    # Find last occurrence of x
    while low <= high:
        
        # Find the mid index
        mid = (low + high) // 2
        
        # If x is equal to arr[mid]
        if x == arr[mid]:
            last = mid
            low = mid + 1
        # If x is less than arr[mid], 
        # then search in the left subarray
        elif x < arr[mid]:
            high = mid - 1
        # If x is greater than arr[mid], 
        # then search in the right subarray
        else:
            low = mid + 1
    return last

# Function for finding first occurrence of x
def findFirst(arr, x):
    n = len(arr)
    
    # Initialize low and high index
    # to find the first occurrence
    low = 0
    high = n - 1
    
    # Initialize first occurrence
    first = -1
    
    # Find first occurrence of x
    while low <= high:
        
        # Find the mid index
        mid = (low + high) // 2
        
        # If x is equal to arr[mid]
        if x == arr[mid]:
            first = mid
            high = mid - 1
        # If x is less than arr[mid], 
        # then search in the left subarray
        elif x < arr[mid]:
            high = mid - 1
        # If x is greater than arr[mid], 
        # then search in the right subarray
        else:
            low = mid + 1
    return first

# Function for finding first and last occurrence of x
def find(arr, x):
    n = len(arr)
    
    # Find first and last index
    first = findFirst(arr, x)
    last = findLast(arr, x)
    
    res = [first, last]
    return res

if __name__ == "__main__":
    arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
    x = 5
    res = find(arr, x)
    print(res[0], res[1])


