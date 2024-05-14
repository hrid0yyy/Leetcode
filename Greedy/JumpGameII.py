class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = []
        dp.append(0)
        dp.append(1)
        dp.append(1)
        for i in range(3,n+1):
            dp.append(dp[i-1] + dp[i-2] +dp[i-3])
        return dp[n]
        

                

if __name__ == "__main__":
    obj = Solution()

    print(obj.tribonacci(25))


    
    
    


