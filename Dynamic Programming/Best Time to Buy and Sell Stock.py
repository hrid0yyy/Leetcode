class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = float('inf')
        profit = 0
        for stock in prices:
            if(stock<buy):
                buy = stock
            profit = max(profit,stock - buy)
        return profit
            