class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(start, explore_set):
            ret.append(explore_set[:])
            for i in range(start, len(nums)):
                explore_set.append(nums[i])
                print(explore_set)
                backtrack(i+1, explore_set)
                explore_set.pop()
        ret = []
        nums.sort()
        backtrack(0, [])
        return ret
"""
________________MY SOLUTION_____________
class Solution(object):
    def subsets(self, nums):
        res = []
        alloutput = []
        for i in range(2 ** len(nums)):
            b = bin(i)[2:].zfill(len(nums))
            for i in range(len(nums)):
                if(b[i]=="1"):
                    res.append(nums[i])
            alloutput.append(res[:])
            res.clear()
        return alloutput
                    
                

"""
if __name__ == "__main__":
    list = [1,2,3]
    obj = Solution()
    print(obj.subsets(list)) 