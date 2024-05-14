class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob1 , rob2 = 0 , 0
        for item in nums:
            temp = max (rob1 + item, rob2)
            rob1 = rob2 
            rob2 = temp
        return rob2
        


if __name__ == "__main__":
    nums = [2,5,1,7,1,3,5]
    obj = Solution()
    print(obj.rob(nums))


