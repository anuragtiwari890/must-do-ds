# problem link - https://www.geeksforgeeks.org/dsa/a-product-array-puzzle/

# A Product Array Puzzle

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given an array arr[] of n integers, construct a product array res[] (of the same size) 
    # such that res[i] is equal to the product of all the elements of arr[] except arr[i]. 

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: arr[] = {10, 3, 5, 6, 2}
    # Output: res[] = {180, 600, 360, 300, 900}

    # Input: arr[] = {1, 2, 3, 4, 5}
    # Output: res[] = {120, 60, 40, 30, 24}

    #Input: arr[] = [10, 3, 5, 6, 2]
    #Output: [180, 600, 360, 300, 900]
    #Explanation: 
        #For i=0, res[i] = 3 * 5 * 6 * 2 is 180.
        #For i = 1, res[i] = 10 * 5 * 6 * 2 is 600.
        #For i = 2, res[i] = 10 * 3 * 6 * 2 is 360.
        #For i = 3, res[i] = 10 * 3 * 5 * 2 is 300.
        #For i = 4, res[i] = 10 * 3 * 5 * 6 is 900.

    #Input: arr[] = [12, 0]
    #Output: [0, 12]
    #Explanation: 
        #For i = 0, res[i] = 0.
        #For i = 1, res[i] = 12.

# ------------------------------------------------------------------------------------------------

# approaches:
    # [Naive Approach] Using Nested Loops - O(n^2) Time and O(1) Space
        # This approach is to use two nested loops to calculate the product of all the elements except the current element.
        # Time complexity: O(n^2)
        # Space complexity: O(1)
    # [Better approach] Using Prefix and Suffix Array - O(n) Time and O(n) Space
        # The above approach can be optimized by avoiding the repetitive calculation of products of elements. 
        # The idea is to precompute the prefix and suffix products and store them in two arrays. 
        # Now we can find the product of array except i-th element, by using these precomputed arrays in constant time.

        # product of array except i-th element = prefProduct[i] * suffProduct[i]
        # prefProduct[i] stores product of all elements before i-th index in the array.
        # suffProduct[i] stores product of all elements after i-th index in the array.
        # Time complexity: O(n)
        # Space complexity: O(n)

    # [Efficient Approach] Using Product Array - O(n) Time and O(1) Space
        # The idea is to handle two special cases of the input array: when it contains zero(s) and when it doesn't.

        # If the array has no zeros, product of array at any index (excluding itself) can be calculated by dividing the total product of all elements by the current element. 

        # However, division by zero is undefined, so if there are zeros in the array, the logic changes. 
        # If there is exactly one zero, the product for that index will be the product of all other non-zero elements, 
        # while the elements in rest of the indices will be zero. 
        # If there are more than one zero, the product for all indices will be zero, since multiplying by zero results in zero.

        # Time complexity: O(n)
        # Space complexity: O(1)

# ------------------------------------------------------------------------------------------------

# solution:
# Function to calculate the product of all elements 
# except the current element

def productExceptSelf(arr):
    zeros = 0
    prod = 1

    # Count zeros and track the index of the zero
    for i in range(len(arr)):
        # if the current element is zero, increment the zero count
        if arr[i] == 0:
            zeros += 1
        else:
            # if the current element is not zero, multiply the product by the current element
            prod *= arr[i]

    res = [0] * len(arr)

    # If no zeros, calculate the product for all elements
    if zeros == 0:
        for i in range(len(arr)):
            # divide the product by the current element
            res[i] = prod // arr[i] # typecast to integer because we are dividing two integers
    
    # If one zero, set product only at the zero's index
    elif zeros > 0:
        for i in range(len(arr)):
            # if the current element is zero, set the product at the current index
            if arr[i] == 0:
                res[i] = prod
            else:
                # if the current element is not zero, set the product at the current index to 0
                res[i] = 0

    return res


if __name__ == "__main__":
    arr = [10, 3, 5, 6, 2]
    res = productExceptSelf(arr)
    print(res)

    arr = [1, 2, 3, 4, 5]
    res = productExceptSelf(arr)
    print(res)

    arr = [12, 0, 0, 14]
    res = productExceptSelf(arr)
    print(res)

    arr = [12, 0]
    res = productExceptSelf(arr)
    print(res)

