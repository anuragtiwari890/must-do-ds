# problem link - https://www.geeksforgeeks.org/dsa/next-higher-palindromic-number-using-set-digits/

# Next Higher Palindromic Number using Set Digits

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given a palindromic number num having n number of digits. 
    # The problem is to find the smallest palindromic number greater than num using the same set of digits as in num. 
    # If no such number can be formed then print "Not Possible". 
    # The number could be very large and may or may not even fit into long long int.

# ------------------------------------------------------------------------------------------------

# Examples:
# Input : 4697557964
# Output :  4756996574

# Input : 543212345
# Output : Not Possible

# ------------------------------------------------------------------------------------------------

# approaches:

# Follow the below steps to solve the problem:
# 
# If number of digits n <= 3, then print "Not Possible" and return.
# Calculate mid = n/2 - 1.
# Start traversing from the digit at index mid up to the 1st digit 
    # and while traversing find the index i of the rightmost digit which is smaller than the digit on its right side.
# Now search for the smallest digit greater than the digit num[i] in the index range i+1 to mid. Let the index of this digit be smallest.
# If no such smallest digit found, then print "Not Possible".
# Else the swap the digits at index i and smallest and also swap the digits at index n-i-1 and n-smallest-1. 
    # This step is done so as to maintain the palindromic property in num.
# Now reverse the digits in the index range i+1 to mid. 
# Also If n is even then reverse the digits in the index range mid+1 to n-i-2 else if n is odd then reverse the digits in the index range mid+2 to n-i-2. 
# This step is done so as to maintain the palindromic property in num.
# Print the final modified number num.

# ------------------------------------------------------------------------------------------------
# solution:

# Python implementation to find next higher 
# palindromic number using the same set 
# of digits

# function to reverse the digits in the
# range i to j in 'num'
def reverse(num, i, j) :
    
    while (i < j) :
        temp = num[i]
        num[i] = num[j]
        num[j] = temp
        i = i + 1
        j = j - 1
        
    
# function to find next higher palindromic
# number using the same set of digits
def nextPalin(num, n) :
    
    # if length of number is less than '3'
    # then no higher palindromic number
    # can be formed
    if (n <= 3) :
        print("Not Possible")
        return
    
    # find the index of last digit
    # in the 1st half of 'num'
    mid = n // 2 - 1
    
    # Start from the (mid-1)th digit and
    # find the first digit that is
    # smaller than the digit next to it.
    i = mid - 1
    while i >= 0 :
        if (num[i] < num[i + 1]):
            break
        i = i - 1
    
    # If no such digit is found, then all
    # digits are in descending order which 
    # means there cannot be a greater 
    # palindromic number with same set of 
    # digits
    if (i < 0) :
        print("Not Possible")
        return
    
    # Find the smallest digit on right
    # side of ith digit which is greater 
    # than num[i] up to index 'mid'
    smallest = i + 1
    j = i + 2
    while j <= mid :
        if (num[j] > num[i] and num[j] < 
                        num[smallest]) :
            smallest = j
        j = j + 1
    
    # swap num[i] with num[smallest]
    temp = num[i]
    num[i] = num[smallest]
    num[smallest] = temp
    
    # as the number is a palindrome, 
    # the same swap of digits should
    # be performed in the 2nd half of
    # 'num'
    temp = num[n - i - 1]
    num[n - i - 1] = num[n - smallest - 1]
    num[n - smallest - 1] = temp
    
    # reverse digits in the range (i+1) 
    # to mid
    reverse(num, i + 1, mid)
    
    # if n is even, then reverse
    # digits in the range mid+1 to 
    # n-i-2
    if (n % 2 == 0) :
        reverse(num, mid + 1, n - i - 2)
        
    # else if n is odd, then reverse 
    # digits in the range mid+2 to n-i-2
    else :
        reverse(num, mid + 2, n - i - 2)
        
        
    # required next higher palindromic 
    # number
    result = ''.join(num)
    
    print("Next Palindrome: ",result)
    
# Driver Code
st = "4697557964"
num = list(st)
n = len(st)

nextPalin(num, n)