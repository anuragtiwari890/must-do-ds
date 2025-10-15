# problem link - https://www.geeksforgeeks.org/dsa/factorial-large-number/

# Factorial of a non-negative integer, is the multiplication of all integers smaller than or equal to n. 

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given an integer n, find the factorial of the number.

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: 100
    # Output: 933262154439441526816992388562667004-
    #         907159682643816214685929638952175999-
    #         932299156089414639761565182862536979-
    #         208272237582511852109168640000000000-
    #         00000000000000

    # Input: 50
    # Output: 3041409320171337804361260816606476884-
    #           4377641568960512000000000000

# ------------------------------------------------------------------------------------------------

# approach:
    # Find Factorial of a number using Linked List :-
        # So the basic idea is to multiply the next number ranging between 2 to N with the data stored in the current Node and also maintain a carry just like the array approach. And then move on to the next node.
        # Let's break it down into following steps :
            # Initially we'll create 1 single node containing 1 in it.
            # Then initialized i of a for loop with 2.
            # And for each value of i up till N, we'll call a function multiply which takes 2 parameter, head of the list and value of i.
            # And perform the below operation (See the image)

        # Algorithm:
            # Find value of : node's data * i + carry. Store it in a variable 'prod'.
            # Initialize 2 pointers let's say prev and temp on the current node and Update the current node's value by storing the last digit of the 'prod'
            # Update carry by storing the remaining digits in carry (excluding the last digit)
            # Now, bring prev ptr on temp and move temp to the next node (if any) and then again perform, the previous steps until the carry becomes 0 or the temp ptr becomes NULL.
            # Once the temp pointer reaches the NULL there is a possibility that carry is still not 0. So, until carry becomes 0 we have to again perform the same steps by creating a new node for every remaining digit.

# ------------------------------------------------------------------------------------------------

# solution:
# Node Class
class Node:
    def __init__(self, n):
        self.data = n
        self.prev = None

# Function to perform desired operation
def Multiply(head, i):
    temp = head
    prevPtr = head
    carry = 0
    # Perform operation until temp becomes None
    while temp is not None:
        prod = temp.data * i + carry
        temp.data = prod % 10 # Stores the last digit
        carry = prod // 10
        prevPtr = temp # Change Links
        temp = temp.prev # Moving temp to the next node
    # If carry is greater than 0, create new nodes to store remaining digits
    while carry != 0:
        prevPtr.prev = Node(carry % 10)
        carry = carry // 10
        prevPtr = prevPtr.prev

# Using recursion to print the linked list's data in reverse
def print_list(head):
    if head is None:
        return
    print_list(head.prev)
    print(head.data, end="") # Print linked list in reverse order

# Driver code
def main():
    n = 100
    head = Node(1) # Create a node and initialize it by 1
    for i in range(2, n+1):
        Multiply(head, i) # Run a loop from 2 to n and multiply with head's i
    print("Factorial of", n, "is : ")
    print_list(head) # Print the linked list
    print()

main()