# problem link -  https://www.geeksforgeeks.org/dsa/stock-buy-sell/

# Buy and Sell Stock

# ------------------------------------------------------------------------------------------------

# Problem Statement:
    # Given an array prices[] representing stock prices, find the maximum total profit that can be earned by buying and selling the stock any number of times.
    # Note: We can only sell a stock which we have bought earlier and we cannot hold multiple stocks on any day.

# ------------------------------------------------------------------------------------------------

# Examples:
    # Input: prices[] = [100, 180, 260, 310, 40, 535, 695]
    # Output: 865
    # Explanation: 
        # Buy the stock on day 0 and sell it on day 3 = 310 - 100 = 210 and 
        # Buy the stock on day 4 and sell it on day 6 = 695 - 40 = 655 so the Maximum Profit  is = 210 + 655 = 865.

    # Input: prices[] = [100, 220, 50, 70, 120, 90]
    # Output: 210
    # Explanation: 
        # Buy the stock on day 0 and sell it on day 1 = 220 - 100 = 120 and 
        # Buy the stock on day 2 and sell it on day 4 = 120 - 50 = 70 so the Maximum Profit  is = 120 + 70 = 190.

    # Input: prices[] = [4, 2]
    # Output: 0
    # Explanation: Stock prices keep decreasing, there is no chance to sell at a higher price after buying, so no profit can be made.

# ------------------------------------------------------------------------------------------------
# approaches:
    # [Naive Approach] - O(n^2) Time and O(1) Space
        # The idea is to use two nested loops to find the maximum profit that can be achieved by buying and selling the stock.
        # Time complexity: O(n^2)
        # Space complexity: O(1)

    # [Better Approach] - O(n) Time and O(1) Space
        # The idea is to use a greedy approach to find the maximum profit that can be achieved by buying and selling the stock.
        # Step by step approach:
            # Traverse the array and keep track of the minimum price seen so far.
            # For each price, calculate the profit that can be achieved by selling at the current price and buying at the minimum price seen so far.
            # Update the maximum profit seen so far.
            # Return the maximum profit.
        # Time complexity: O(n)
        # Space complexity: O(1)

    # [Expected Approach] By Accumulating Profit - O(n) Time and O(1) Space
        # The idea is that profit only comes when prices rise.
        #  If the price goes up from one day to the next, we can think of it as buying yesterday and selling today. 
        # Instead of waiting for the exact bottom and top, we simply grab every small upward move.
        #  Adding these small gains together is the same as if we had bought at each valley and sold at each peak because every rise between them gets counted.

        # Step by step approach:
            # Traverse the array and keep track of the minimum price seen so far.
            # For each price, calculate the profit that can be achieved by selling at the current price and buying at the minimum price seen so far.
            # Update the maximum profit seen so far.
            # Return the maximum profit.
        # Time complexity: O(n)
        # Space complexity: O(1)

# ------------------------------------------------------------------------------------------------

# Solution:

# using greedy approach
#  works for the single buy and sell
def usingGreedyApproach(prices):
    # Step 1: Initialize the variables
    n = len(prices)
    lMin = prices[0]  
    lMax = prices[0]  
    res = 0
  
    # Step 2: Traverse the array
    for i in range(n):
        # if the current price is less than the minimum price seen so far, update the minimum price seen so far
        if prices[i] < lMin:
            lMin = prices[i]
            lMax = prices[i]
        else:
            # if the current price is greater than the maximum price seen so far, update the maximum price seen so far
            if prices[i] > lMax:
                lMax = prices[i]
            # if the profit is greater than the maximum profit seen so far, update the maximum profit seen so far
            if(lMax - lMin) > res:
                res = lMax - lMin

    return res

# using accumulating profit approach
# works for the multiple buy and sell
# step by step approach:
    # Traverse the array and keep track of the minimum price seen so far.
    # For each price, calculate the profit that can be achieved by selling at the current price and buying at the minimum price seen so far.
    # Update the maximum profit seen so far.
    # Return the maximum profit.
def usingAccumulatingProfitApproach(prices):
    n = len(prices)
    res = 0
    for i in range(1, n):
        if prices[i] > prices[i - 1]:
            res += (prices[i] - prices[i - 1])
    return res

if __name__ == "__main__":
    prices = [100, 180, 260, 310, 40, 535, 695]
    print(usingGreedyApproach(prices))
    print(usingAccumulatingProfitApproach(prices))


# Stock Buy and Sell - k Transactions Allowed -> link - https://www.geeksforgeeks.org/dsa/maximum-profit-by-buying-and-selling-a-share-at-most-k-times/