# problem link - https://www.geeksforgeeks.org/dsa/count-number-of-triplets-in-an-array-having-sum-in-the-range-a-b/

# Count number of triplets in an array having sum in the range [a, b]

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given an array of distinct integers and a range [a, b], 
    # the task is to count the number of triplets having a sum in the range [a, b].

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input : arr[] = {8, 3, 5, 2}
        # range = [7, 11]
    # Output : 1
    # There is only one triplet {2, 3, 5}
    # having sum 10 in range [7, 11].

    # Input : arr[] = {2, 7, 5, 3, 8, 4, 1, 9}
        # range = [8, 16]
    # Output : 36

# ------------------------------------------------------------------------------------------------
# approaches:
    # [Naive Approach] - O(n^3) Time and O(1) Space
        # The naive approach is to try all possible combinations of three elements and check if they form a triangle.
        # Time complexity: O(n^3)
        # Space complexity: O(1)

    # [Better Approach] - O(n^2) Time and O(1) Space
        # An efficient solution is to first find the count of triplets having a sum less than or equal to upper limit b in the range [a, b]. 
        # This count of triplets will also include triplets having a sum less than the lower limit a. 
        # Subtract the count of triplets having a sum less than a. 
        # The final result is the count of triplets having a sum in the range [a, b]. 

        # The algorithm is as follows: 
            # Find count of triplets having a sum less than or equal to b. Let this count be x.
            # Find count of triplets having a sum less than a. Let this count be y.
            # Final result is x-y.

        # Time complexity: O(n^2)
        # Space complexity: O(1)

# ------------------------------------------------------------------------------------------------
# solution:
# Python program to count 
# triplets with sum that 
# lies in given range [a, b].

# Function to find count of 
# triplets having sum less
# than or equal to val.
def countTripletsLessThan(arr, n, val):

    # sort the input array.
    arr.sort()

    # Initialize result
    ans = 0

    j = 0; k = 0

    # to store sum
    sum = 0

    # Fix the first element
    for i in range(0,n-2):

        # Initialize other two 
        # elements as corner 
        # elements of subarray 
        # arr[j+1..k]
        j = i + 1
        k = n - 1

        # Use Meet in the 
        # Middle concept.
        while j != k :
            sum = arr[i] + arr[j] + arr[k]
            
            # If sum of current triplet
            # is greater, then to reduce it
            # decrease k.
            if sum > val:
                k-=1

            # If sum is less than or 
            # equal to given value, 
            # then add possible 
            # triplets (k-j) to result.
            else :
                ans += (k - j)
                j += 1
    return ans

# Function to return
# count of triplets having
# sum in range [a, b].
def countTriplets(arr, n, a, b):
    
    # to store count of triplets.
    res = 0

    # Find count of triplets 
    # having sum less than or 
    # equal to b and subtract 
    # count of triplets having 
    # sum less than or equal to a-1.
    res = (countTripletsLessThan(arr, n, b) -
        countTripletsLessThan(arr, n, a - 1))

    return res

# Driver code
if __name__ == "__main__":
    
    arr = [ 2, 7, 5, 3, 8, 4, 1, 9 ]
    n = len(arr)
    a = 8; b = 16
    print(countTriplets(arr, n, a, b))
