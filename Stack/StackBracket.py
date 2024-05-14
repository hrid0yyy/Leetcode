class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        stack.append("$")
        index = 0
        while(len(s)>index):
            if(ord(s[index]) in (40,91,123)):
                    stack.append(s[index])
                    index += 1
                    continue
            else:
                    if((ord(s[index]) == 41 and ord(stack.pop()) == 40) or (ord(s[index]) == 125 and ord(stack.pop()) == 123) or (ord(s[index]) == 93 and ord(stack.pop()) == 91)):
                        index += 1 
                        continue
                    else:
                        return False
        if(len(stack)>1):
            return False
        return True            
         
         
s = "((){}[])"
obj = Solution()
print(obj.isValid(s))
