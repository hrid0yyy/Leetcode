class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Bottom Up true DP 
        dp = [amount + 1] * (amount+1)
        
        dp[0] = 0
        
        for a in range(1,amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] =  min (dp[a], 1 + dp[a-c])
       

        return dp[amount] if dp[amount] != amount + 1 else -1

        
"""___ BFS Solution but not efficient ___"""

def bfs(coins, target):
    queue = []
    queue.append([])

    while queue:
        c = queue.pop(0)
        if sum(c) == target:
            return len(c)
        elif sum(c) > target:
            return -1
        for item in coins:
            temp = c[:]
            temp.append(item)
            queue.append(temp)


if __name__ == "__main__":
    coins = [1,3,4,5]
    target =7
    print(bfs(coins,target))
    obj = Solution()
    print(obj.coinChange(coins,target))
