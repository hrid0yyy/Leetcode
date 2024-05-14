class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        from collections import defaultdict
        counts = defaultdict(int)
        for item in answers:
            counts[item] += 1
        import math
        rabbits = 0
        for key, value in counts.items():
            rabbits += math.ceil(value/(key+1))*(key+1)
        return rabbits

        

                

if __name__ == "__main__":
    answers = [10,10,10]
    obj = Solution()
    print(obj.numRabbits(answers))
