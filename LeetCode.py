class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list = s.split()
        list.reverse()
        return ' '.join(list)

        

if __name__ == "__main__":
    s = "a good   example"
    obj = Solution()
    print(obj.reverseWords(s))


    
    
    


