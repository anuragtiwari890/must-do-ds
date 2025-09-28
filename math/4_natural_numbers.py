# problem link - https://www.geeksforgeeks.org/dsa/natural-numbers/

# Program to Print First N Natural Numbers

# ------------------------------------------------------------------------------------------------

# problem statement:
# Given a positive integer N, print the first N natural numbers.

# fact about natural numbers:
    # The natural numbers are the ordinary numbers, 1, 2, 3, etc., with which we count.
    # The next possible natural number can be found by adding 1 to the current natural number
    # The number zero is sometimes considered to be a natural number. Not always because no one counts starting with zero, 0, 1, 2, 3.
    # GCD of all other natural numbers with a prime is always one.
    # The natural numbers can be defined formally by relating them to sets. Then, zero is the number of elements in the empty set; 1 is the number of elements in the set containing one natural number; and so on.

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: N = 8
    # Output: 8
    # Explanation: The first 8 natural numbers are 1, 2, 3, 4, 5, 6, 7, 8. 

# ------------------------------------------------------------------------------------------------

# Python Program to print first n natural numbers

def printNaturalNumbers(n):
    for i in range(1, n + 1):
        print(i, end=" ")

if __name__ == "__main__":
    n = 10
    printNaturalNumbers(n)