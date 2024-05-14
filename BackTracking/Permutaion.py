nums = [1,2,3]
ls = []
allBoard = []
import copy
def Permutation(ls,nums):
    if(len(ls) == len(nums)):
        temp = copy.deepcopy(ls)
        allBoard.append(temp)
        return
    for i in range(len(nums)):
        if(nums[i] not in ls):
            ls.append(nums[i])
            Permutation(ls,nums)
            ls.pop()
Permutation(ls,nums)
print(allBoard)
