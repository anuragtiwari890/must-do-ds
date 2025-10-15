# problem link - https://www.geeksforgeeks.org/dsa/k-th-element-two-sorted-arrays/

# K-th Element of Merged Two Sorted Arrays

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given two sorted arrays of size m and n respectively, you are tasked with finding the element that would be at the k-th position of the merged array.

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: arr1 = [2, 3, 6, 7, 9], arr2 = [1, 4, 8, 10], k = 5
    # Output: 6
    # Explanation: The merged array would be [1, 2, 3, 4, 6, 7, 8, 9, 10]. The 5th element is 6.

# ------------------------------------------------------------------------------------------------

# approaches:
    # [Naive Approach] - Using Merge Sort - O(m+n) Time and O(m+n) Space
        # The idea is to merge the two arrays and then return the k-th element of the merged array.

    # using priority queue - O(m+nlog(m+n)) Time and O(m+n) Space
        # The idea is to use a priority queue to merge the two arrays and then return the k-th element of the merged array.
        # Step by step approach:
            # 1. Create a priority queue and insert all the elements of the two arrays into it.
            # 2. Pop the k-th element from the priority queue.
            # 3. Return the k-th element.

    
    # [Better Approach] - Using Two Pointers - O(k) Time and O(1) Space
        # The idea is to use two pointers to traverse the two arrays and find the k-th element of the merged array.
        # Step by step approach:
            # 1. Initialize two pointers, i and j, to the start of the two arrays.
            # 2. Traverse the two arrays until the k-th element is found.
            # 3. If the element at the current pointer in the first array is less than the element at the current pointer in the second array, 
                # then increment the pointer in the first array and decrement k.
            # 4. If the element at the current pointer in the second array is less than the element at the current pointer in the first array, 
                # then increment the pointer in the second array and decrement k.
            # 5. If k is 0, then return the element at the current pointer in the first array.

    # [Expected Approach] - Using Binary Search - O(log(min(m,n))) Time and O(1) Space
        # The idea is to use binary search to find the k-th element of the merged array.
        # Step by step approach:
            # 1. Find the middle element of the merged array.
                # 1.1. If the middle element is in the first array, then the k-th element is in the right half of the first array.
                # 1.2. If the middle element is in the second array, then the k-th element is in the right half of the second array.
                # 1.3. If the middle element is in both the arrays, then the k-th element is in the middle of the two arrays.
            # 2. Compare the middle element with the k-th element.
            # 3. If the middle element is less than the k-th element, then the k-th element is in the right half of the merged array.
            # 4. If the middle element is greater than the k-th element, then the k-th element is in the left half of the merged array.
            # 5. If the middle element is equal to the k-th element, then return the middle element.

# solution:
# using two pointers
def min(i, k):
    if i <= k:
        return i
    else:
        return i

def max(i, j):
    if i >= j:
        return i
    else:
        return j


def kthElementUsingTwoPointers(arr1, arr2, k):
    if k == 0:
        return min(arr1, arr2)
    
    arr1Idx = 0
    arr2Idx = 0
    
    # loop through both the arrays if the current element is less than the current element of the other array,
    # then increment the index of the current array
    while arr1Idx < len(arr1) and arr2Idx < len(arr2):
        k -= 1
        if arr1[arr1Idx] <= arr2[arr2Idx]:
            if k == 0:
                return arr1[arr1Idx]
            arr1Idx += 1
        else:
            if k == 0:
                return arr2[arr2Idx]
            arr2Idx += 1

    k -= 1
    
    if arr1Idx < len(arr1):
        return arr1[arr1Idx + k]
    elif arr2Idx < len(arr2):
        return arr2[arr2Idx + k]
    else:
        return -1

t = kthElementUsingTwoPointers([2, 3, 6, 7, 9], [1, 4, 8, 10], 5)

print(t)


# using binary search
def kthElement(a, b, k):
    n = len(a)
    m = len(b)

    # if a[] has more elements, then call kthElement
    # with reversed parameters
    if n > m:
        return kthElement(b, a, k)

    # binary Search on the number of elements we can
    # include in the first set from a[]
    lo = max(0, k - m)
    hi = min(k, n)

    while lo <= hi:
        mid1 = (lo + hi) // 2
        mid2 = k - mid1

        # find elements to the left and right of
        # partition in a[]
        l1 = (mid1 == 0 and float('-inf') or a[mid1 - 1])
        r1 = (mid1 == n and float('inf') or a[mid1])

        # find elements to the left and right of
        # partition in b[]
        l2 = (mid2 == 0 and float('-inf') or b[mid2 - 1])
        r2 = (mid2 == m and float('inf') or b[mid2])

        # if it is a valid partition
        if l1 <= r2 and l2 <= r1:
          
            # find and return the maximum of l1 and l2
            return max(l1, l2)

        # check if we need to take lesser elements 
        # from a[]
        if l1 > r2:
            hi = mid1 - 1

        # check if we need to take more elements
        # from a[]
        else:
            lo = mid1 + 1

    return 0

if __name__ == "__main__":
    print(kthElement([2, 3, 6, 7, 9], [1, 4, 8, 10], 5))