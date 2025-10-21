# problem link - https://www.geeksforgeeks.org/dsa/median-of-two-sorted-arrays-of-different-sizes/

# Median of two sorted arrays of different sizes

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given two sorted arrays, a[] and b[], find the median of these sorted arrays.
    #  Assume that the two sorted arrays are merged and then median is selected from the combined array.

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: a[] = [-5, 3, 6, 12, 15], b[] = [-12, -10, -6, -3, 4, 10]
    # Output: 3
    # Explanation: The merged array is [-12, -10, -6, -5 , -3, 3, 4, 6, 10, 12, 15]. So the median of the merged array is 3.

    # Input: a[] = [1], b[] = [2, 4, 5, 6, 7]
    # Output: 4.5
    # Explanation: The merged array is [1, 2, 4, 5, 6, 7]. 
    # The total number of elements are even, so there are two middle elements. Take the average between the two: (4 + 5) / 2 = 4.5

# ------------------------------------------------------------------------------------------------

# approaches:
    # [Naive Approach] Using Sorting - O((n + m) × log (n + m)) Time and O(n + m) Space
        # The naive approach is to merge the two arrays sort them and then find the median of the merged array.
        # Time complexity: O((n + m) × log (n + m))
        # Space complexity: O(n+m)

    # [Better Approach] Use Merge of Merge Sort - O(m + n) Time and O(1) Space
        # merge the two array like we do in merge sort and find the median of the merged array.
        # Time complexity: O(m + n)
        # Space complexity: O(1)

    # [Expected Approach] Use Binary Search - O(log(min(n,m))) Time and O(1) Space
        # Consider the first array is smaller. If first array is greater, then swap the arrays to make sure that the first array is smaller.
        # We mainly maintain two sets in this algorithm by doing binary search in the smaller array. 
            # Let mid1 be the partition of the smaller array. 
            # The first set contains elements from 0 to (mid1 - 1) from smaller array and mid2 = ((n+m+1) / 2 - mid1) elements from the greater array 
            # to make sure that the first set has exactly (n+m+1)/2 elements. The second set contains remaining half elements.
        # Our target is to find a point in both arrays such that all elements 
            # in the first set are smaller than all elements in the elements in the other set (set that contains elements from right side). 
            # For this we validate the partitions using the same way as we did in Median of two sorted arrays of same size.

        # Why do we apply Binary Search on the smaller array?
        # Applying Binary Search on the smaller array helps us in two ways:

        # Since we are applying binary search on the smaller array, we have optimized the time complexity of the algorithm from O(log n) to O(log(min(n, m)).
        # Also, if we don't apply the binary search on the smaller array, 
            # then then we need to set low = max(0, (n + m + 1)/2 - m) and high = min(n, (n + m + 1)/2) 
            # to avoid partitioning mid1 or mid2 outside a[] or b[] respectively.
        # To avoid handling such cases, we can simply binary search on the smaller array.
        # Time complexity: O(log(min(n,m)))
        # Space complexity: O(1)

# ------------------------------------------------------------------------------------------------
# solution:
# Python3 program to find median of two sorted arrays of
# different sizes
def medianOfUsingMergeSort(a, b):
    n = len(a)
    m = len(b)
    i = 0
    j = 0

    # m1 to store the middle element
    # m2 to store the second middle element
    m1 = -1
    m2 = -1

    # loop till (m+n)/2
    for count in range((m + n) // 2 + 1):
        m2 = m1

        # if both the arrays have remaining elements
        if i != n and j != m:
            if a[i] > b[j]:
                m1 = b[j]
                j += 1
            else:
                m1 = a[i]
                i += 1

        # if only a[] has remaining elements
        elif i < n:
            m1 = a[i]
            i += 1

        # if only b[] has remaining elements
        else:
            m1 = b[j]
            j += 1

    # return median based on odd/even size
    if (m + n) % 2 == 1:
        return m1
    else:
        return (m1 + m2) / 2.0


def medianOfUsingBinarySearch(a, b):
    n = len(a)
    m = len(b)

    # if a[] has more elements, then call medianOf2 
    # with reversed parameters
    if n > m:
        return medianOfUsingBinarySearch(b, a)

    lo = 0
    hi = n
    while lo <= hi:
        mid1 = (lo + hi) // 2
        mid2 = (n + m + 1) // 2 - mid1

        # find elements to the left and right 
        # of partition in a[]
        l1 = (mid1 == 0) and float('-inf') or a[mid1 - 1]
        r1 = (mid1 == n) and float('inf') or a[mid1]

        # find elements to the left and right 
        # of partition in b[]
        l2 = (mid2 == 0) and float('-inf') or b[mid2 - 1]
        r2 = (mid2 == m) and float('inf') or b[mid2]

        # if it is a valid partition
        if l1 <= r2 and l2 <= r1:
          
            # if the total elements are even, then median is 
            # the average of two middle elements
            if (n + m) % 2 == 0:
                return (max(l1, l2) + min(r1, r2)) / 2.0
              
            # if the total elements are odd, then median is 
            # the middle element
            else:
                return max(l1, l2)

        # check if we need to take lesser 
        # elements from a[]
        if l1 > r2:
            hi = mid1 - 1
            
        # check if we need to take more 
        # elements from a[]
        else:
            lo = mid1 + 1
    return 0


if __name__ == "__main__":
    arr1 = [-5, 3, 6, 12, 15]
    arr2 = [-12, -10, -6, -3, 4, 10]
    print(medianOfUsingMergeSort(arr1, arr2))
    print(medianOfUsingBinarySearch(arr1, arr2))