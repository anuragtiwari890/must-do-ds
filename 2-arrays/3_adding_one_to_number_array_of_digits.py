# problem link - https://www.geeksforgeeks.org/dsa/adding-one-to-number-represented-as-array-of-digits/

# Adding one to number represented as array of digits

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given a non-negative number represented as an array of digits, add 1 to the number.

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: arr[] = {1, 2, 3}
    # Output: {1, 2, 4}
    # Explanation: The number represented by the array is 123. Adding 1 to it gives 124.

    # Input: arr[] = {9, 9, 9}
    # Output: {1, 0, 0, 0}
    # Explanation: The number represented by the array is 999. Adding 1 to it gives 1000.

    # Input: arr[] = {0}
    # Output: {1}
    # Explanation: The number represented by the array is 0. Adding 1 to it gives 1.

# ------------------------------------------------------------------------------------------------

# approaches:
    # [Approach - 1] - Using Carry - O(n) Time and O(1) Space
        # To add one to the number represented by digits, follow the below steps : 
        # Parse the given array from the end as we do in school addition.
        # If the last elements are 9, make it 0 and carry = 1.
        # For the next iteration check carry and if it adds to 10, do the same as step 2.
        # After adding carry, make carry = 0 for the next iteration.
        # If the carry still remains after traversing the entire array, append 1 in the beginning.
    
    # [Approach - 2] - O(n) Time and O(1) Space
        # The idea is to start from the end of the vector and if the element is 9 set it to 0, else increment the digit by 1 and exit the loop.
        # If the loop set all digits to 0 (if all digits were 9) insert 1 at the beginning.
        # Else increment the element at the position where the loop stopped.

# ------------------------------------------------------------------------------------------------

# solution:
# Python program to add 1 to a
# number represented as an array

def addOneUsingCarry(arr):
    carry = 1

    for i in range(len(arr) - 1, -1, -1):
        sum = arr[i] + carry
        arr[i] = sum % 10
        carry = sum // 10

    if carry:
        arr.insert(0, carry)

    return arr


# Python program to add 1 to a
# number represented as an array

# function to add one 
def addOne(arr):

    # initialize an index to end of array
    index = len(arr) - 1

    # while the index is valid and the value
    # at index is 9
    while index >= 0 and arr[index] == 9:
        arr[index] = 0
        index -= 1

    # if index < 0 (if all arr were 9)
    if index < 0:
        # insert an one at the beginning of the list
        arr.insert(0, 1)

    # else increment the value at [index]
    else:
        arr[index] += 1

    return arr

if __name__ == "__main__":

    # Driver code
    arr = [9, 9, 9]
    res = addOne(arr)
    print(res)

    arr = [0, 0 ,0]
    res = addOne(arr)
    print(res)