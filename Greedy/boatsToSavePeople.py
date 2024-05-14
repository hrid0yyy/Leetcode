class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        boat = 0
        f = 0
        l = len(people) - 1 

        while f <= l:  #1,2,4,5
            temp = people[f] + people[l]
            if temp <= limit :
                l -= 1
                f += 1
                boat += 1
            elif temp > limit:
                l -= 1
                boat += 1

        return boat