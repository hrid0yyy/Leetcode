class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        F = [0,1]
        for i in range(2,n+1):
            F.append(F[i-1]+F[i-2])
        return F[n]
obj = Solution()
print(obj.fib(9))