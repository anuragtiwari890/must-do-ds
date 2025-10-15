# problem link - https://www.geeksforgeeks.org/dsa/find-smallest-value-represented-sum-subset-given-array/

# Smallest Value that cannot be represented as sum of any subset of a given array

# ------------------------------------------------------------------------------------------------

# problem statement:
    # Given an array of positive numbers, the task is to find the smallest positive integer value 
    # that cannot be represented as the sum of elements of any subset of a given set. 

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: arr[] = {1, 10, 3, 11, 6, 15};
    # Output: 2

    # Input: arr[] = {1, 1, 1, 1};
    # Output: 5

    # Input: arr[] = {1, 1, 3, 4};
    # Output: 10 

# ------------------------------------------------------------------------------------------------

# [Expected Approach] Using Sorting - O(n Log n) time and O(1) space
    # The idea is to sort the array in ascending order.  After Sorting, we can solve this problem using a simple loop. Let the input array be arr[0..n-1]. We first sort the  array in non-decreasing order. Let the smallest element that cannot be  represented by elements at indexes from 0 to (i-1) be ‘res’.  We  initialize ‘res’ as 1 (smallest possible answer) and traverse the given  array from i=0.  There are the following two possibilities when we  consider element at index i:

    # We decide that ‘res’ is the final result:  
        # If arr[i] is greater than ‘res’, then we found the gap which is ‘res’  because the elements after arr[i] are also going to be greater than  ‘res’.
    # The value of ‘res’ is incremented after considering arr[i]:  
        # If arr[i] is not greater than ‘res’, the value of ‘res’ is incremented  by arr[i] so ‘res’ = ‘res’+arr[i] 
        # (why? If elements from 0 to (i-1) can represent 1 to ‘res-1’, 
        # then elements from 0 to i can  represent from 1 to ‘res + arr[i] – 1’ by adding arr[i] to all subsets  
        # that represent 1 to ‘res-1’ which we have already determined to be  represented)

    # Let arr = [1, 10, 2, 11, 6, 15]
    # After Sorting, we get, arr = [1, 2, 6, 10, 11, 15]
    # We initialize res = 1. Since 1 <= res, we make res = 1 + 1 = 2
    # Since 2 <= res, res = 2 + 2 = 4
    # Since 6 is not <= res, we return res.

# ------------------------------------------------------------------------------------------------

# solution:
def findSmallest(arr, n):
    res = 1
    for i in range(n):
        if arr[i] <= res:
            res = res + arr[i]
        else:
            break
    return res

if __name__ == "__main__":
    arr = [1, 10, 3, 11, 6, 15]
    n = len(arr)
    print(findSmallest(arr, n))

    arr = [1, 1, 1, 1]
    n = len(arr)
    print(findSmallest(arr, n))

    arr = [1, 1, 3, 4]
    n = len(arr)
    print(findSmallest(arr, n))
