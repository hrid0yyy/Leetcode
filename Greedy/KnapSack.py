profit = [10,5,15,7,6,18,3]
weight = [2,3,5,7,1,4,1]
ratio = []
for i in range(len(profit)):
	ratio.append((profit[i]/weight[i],i))
capacity = 15
ratio.sort()
ratio.reverse()
item = []
# GREEDY KNAPSACK
i = 0
while(i < len(ratio)):
	Bitem = ratio[i][1]
	if(capacity==0):
		item.append((Bitem,0))
		i+=1
		continue
	if(capacity<weight[Bitem]):
		item.append((Bitem,capacity/weight[Bitem]))
		capacity = 0
		i += 1
		continue
	capacity = capacity - weight[Bitem]
	item.append((Bitem,1))
	i += 1
item.sort()
print(item)
	