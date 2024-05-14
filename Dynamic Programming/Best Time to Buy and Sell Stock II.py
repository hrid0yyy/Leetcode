class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = float('inf')
        prev = float('-inf')
        profit = 0
        sum = 0
        for stock in prices:
            if prev < stock:
                prev = stock
            else:
                prev = stock
                buy = float('inf')
                sum += profit 
                profit = 0
            if(stock<buy):
                buy = stock
            profit = max(profit,stock - buy)
        sum += profit
        return sum
            
                   
if __name__ == "__main__":
    prices = [1,3,5,4,3,7,6,9,2,3] #expected 12
    obj = Solution()
    print(obj.maxProfit(prices))