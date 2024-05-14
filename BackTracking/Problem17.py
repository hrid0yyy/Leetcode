class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        hashMap = {
            2 : ["a","b","c"],
            3 : ["d","e","f"],
            4 : ["g","h","i"],
            5 : ["j","k","l"],
            6 : ["m","n","o"],
            7 : ["p","q","r","s"],
            8 : ["t","u","v"],
            9 : ["w","x","y","z"],

        }
        allOutput = []
        def backtrack(digits,string,index):
            if(len(string)==len(digits)):
                    allOutput.append(string)
                    return
            for i in range(len(hashMap[int(digits[index])])):
                    backtrack(digits,string+hashMap[int(digits[index])][i],index+1)      
        if(len(digits)!=0):
            backtrack(digits,"",0)
        return allOutput
digits = "23"
obj = Solution()
print(obj.letterCombinations(digits))


