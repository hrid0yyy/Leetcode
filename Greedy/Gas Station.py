"""
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
    
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        start = 0
        for i in range(len(gas)):
            total += (gas[i]-cost[i])
            if total < 0:
                start = i+1
                total = 0
        return start
"""
# My solution 
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        net = []
        maX = -1
        for i in range(len(gas)):
            if(gas[i]-cost[i]>maX):
                maX = gas[i]-cost[i]
                net.insert(0,(gas[i]-cost[i],i))
                continue
            elif(gas[i]-cost[i]>0):
                net.append((gas[i]-cost[i],i))

        def drive(index,gas,cost):
            destination = index
            tank = 0
            while(True):
                tank = tank + gas[index]
                if(tank - cost[index]>=0):
                    tank -= cost[index]
                    index = (index+1)%len(gas)
                else: 
                    return False
                if(index == destination):
                    return True
        for netvalue,index in net:
            if(drive(index,gas,cost)):
                return index
        return -1
gas = [5,8,2,8]
cost = [6,5,6,6]
obj = Solution()
print(obj.canCompleteCircuit(gas,cost))
