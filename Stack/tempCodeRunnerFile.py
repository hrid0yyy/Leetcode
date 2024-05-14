class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        index = 0
        m = 4
        startingBracket = ["(","{","["]
        hashMap = {
         "(" : 1,
         ")" : 1,
         "[" : 3,
         "]" : 3,
         "{" : 2,
         "}" : 2
        }
        while(len(s)>index):
            if(s[index] in startingBracket and hashMap[s[index]] <= m):
                    stack.append(s[index])
                    m = min(m,hashMap[s[index]])
                    index += 1
                    continue
            else:
                    if(hashMap[s[index]] == hashMap[stack.pop()]):
                        index += 1 
                        continue
                    else:
                        return False
        if(len(stack)>0):
            return False
        return True            
         