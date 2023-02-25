"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 

Constraints:

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = profit = 0
        if not prices:
            return total_profit
        min_price = max_price = prices[0]
        i = j = 0
        j = j + 1
        while j < len(prices):
            # Check if the start of the window is larger than the next index
            # Slide the window to where j is
            if prices[i] >= prices[j]:
                i = j
                j = j + 1
                continue
            # Check if there's more of the window to expand
            if j + 1 < len(prices):
                # If j is larger than the next value, store the profit
                # and then reset the window to j
                if prices[j] >= prices[j+1]:
                    total_profit += prices[j] - prices[i]
                    i = j
                    j = j + 1
                    continue
                # If j is less, then expand the window size
                elif prices[j] < prices[j+1]:
                    j += 1
                    continue
            # This means we have maxed the window size so run a final calculation
            else:
                total_profit += max(0, prices[j] - prices[i])
                j += 1
                continue
        return total_profit
