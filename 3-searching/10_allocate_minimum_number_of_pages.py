# problem link - https://www.geeksforgeeks.org/dsa/allocate-minimum-number-of-pages/

# Allocate Minimum Number of Pages

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given an array arr[], where arr[i] represents the number of pages in the i-th book, and an integer k denoting the total number of students, 
    # allocate all books to the students such that:
        # Each student gets at least one book.
        # Books are allocated in a contiguous sequence.
        # The maximum number of pages assigned to any student is minimized.
    # If it is not possible to allocate all books among k students under these conditions, return -1.

# ------------------------------------------------------------------------------------------------

# Examples:
# Input: arr[] = [12, 34, 67, 90], k = 2
# Output: 113
# Explanation: Books can be distributed in following ways:
    # [12] and [34, 67, 90] - The maximum pages assigned to a student is  34 + 67 + 90 = 191.
    # [12, 34] and [67, 90] - The maximum pages assigned to a student is 67 + 90 = 157.
    # [12, 34, 67] and [90] - The maximum pages assigned to a student is 12 + 34 + 67 = 113.
    # The third combination has the minimum pages assigned to a student which is 113.

# Input: arr[] = [15, 17, 20], k = 5
# Output: -1
    # Explanation: Since there are more students than total books, it's impossible to allocate a book to each student.

# Input: arr[] = [22, 23, 67], k = 1
# Output: 112
    # Explanation: Since there is only 1 student, all books are assigned to that student. So, maximum pages assigned to a student is 22 + 23 + 67 = 112.

# ------------------------------------------------------------------------------------------------
# approaches:
    # [Naive Approach] Using Recursion - O(k^n) Time and O(n) Space
        # The idea is to recursively generate all possible ways of allocating the books to the students and find the one with the minimum maximum pages assigned to a student.
        # To do so, start from the first book and for each book, recursively call for all the books reachable from that book 
        # (i.e. i + arr[i]) and return the one with the minimum maximum pages assigned to a student.

        # Time complexity: O(k^n)
        # Space complexity: O(n)

    # [Better Approach] Using Binary Search - O(n log m) Time and O(1) Space
        # The maximum number of pages (page limit) that a student can be allocated has a monotonic property:
            # If at a page limit p, books cannot be allocated to all k students, 
                # then we need to reduce the page limit to ensure more students receive books.
            # If at a page limit p, we can allocate books to more than k students, 
                # then we need to increase the page limit so that fewer students are allocated books.
            # Therefore, we can apply binary search to minimize the maximum pages a student can be allocated. 
                # To check the number of students that can be allotted books for any page limit, w
                # e start assigning books to the first student until the page limit is reached, then move to the next student.

        # Time complexity: O(n log m)
        # Space complexity: O(1)

# ------------------------------------------------------------------------------------------------
# solution:
# Python3 program to find minimum number of pages
# Binary Search based solution to find
# minimum number of pages

# function to check if books can be allocated to
# all k students without exceeding 'pageLimit'
def check(arr, k, pageLimit):
    
    # starting from the first student
    cnt = 1
    pageSum = 0
    for pages in arr:
        
        # if adding the current book exceeds the page 
        # limit, assign the book to the next student
        if pageSum + pages > pageLimit:
            cnt += 1
            pageSum = pages
        else:
            pageSum += pages
            
    # if books can assigned to less than k students then
    # it can be assigned to exactly k students as well
    return cnt <= k

def findPages(arr, k):
    
    # if number of students are more than total books
    # then allocation is not possible
    if k > len(arr):
        return -1
    
    # search space for Binary Search
    lo = max(arr)
    hi = sum(arr)
    res = -1
    
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        
        if check(arr, k, mid):
            res = mid
            hi = mid - 1
        else:
            lo = mid + 1
            
    return res

if __name__ == "__main__":
    arr = [12, 34, 67, 90]
    k = 2
    print(findPages(arr, k))