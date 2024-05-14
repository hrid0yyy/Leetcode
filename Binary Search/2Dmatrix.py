matrix = [[1,3,5,7],
		  [10,11,16,20],
		  [23,30,34,60]]
found = False    
start = 0
end = len(matrix) -1
target = 60
while(True):
	mid = int((start + end) / 2)
	if(start==end):
		row = start
		break
	if(start+1==end and matrix[end][0]<=target):
		row = end 
		break
	if(start+1==end and matrix[end][0]>target):
		row = start
		break
	if(matrix[mid][0]>target):
		end = mid - 1
		continue
	else:
		start = mid	
start = 0
end = len(matrix[0]) -1
while(start<=end):
	mid = start  + (end - start) // 2
	if(matrix[row][mid]==target):
		found = True
		break
	elif(matrix[row][mid]<target):
		start = mid + 1
	else:
		end = mid -1
		
print(found)