class Solution(object):
    def miceAndCheese(self, reward1, reward2, k):
        """
        :type reward1: List[int]
        :type reward2: List[int]
        :type k: int
        :rtype: int
        """
        queue = []
        for i in range(len(reward1)):
            queue.append(reward1[i]-reward2[i])
        queue.sort()
        profit = sum(reward2)
        for i in range(k):
            profit += queue.pop()
            
        return profit