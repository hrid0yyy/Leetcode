class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int] # candidates = [2,3,6,7], target = 7
        :type target: int
        :rtype: List[List[int]] # [[2,2,3],[7]]
        """
        def isSafe(list,value,target):
            count = 0
            for i in range(len(list)):
                count += list[i]
            if(count + value <= target):
                return True, count+value
            return False, count+value

        allOutput = []
        def buildOutput(list):
            import copy 
            ot = copy.deepcopy(list)
            ot.sort()
            if(ot not in allOutput):
                allOutput.append(ot)


        def helper(candidates,list,target):
            if(isSafe(list,0,target)[1]==target):
                buildOutput(list)
            
            for i in range(len(candidates)):
                if(isSafe(list,candidates[i],target)[0]):
                    list.append(candidates[i])
                    helper(candidates,list,target)
                    list.pop()
            return 
        list = []
        helper(candidates,list,target)
        return allOutput


obj = Solution()
candidates = [2,3,5]
target = 8
print(obj.combinationSum(candidates,target))


