# This is the memoization approach of 
# 0 / 1 Knapsack in Python in simple 
# we can say recursion + memoization = DP 
"""
SELF NOTES:
DP two types of approach: 1)Memoziation, 2)Tabulation      
"""

def knapsack(wt, val, W, n): 

	# base conditions 
	if n == 0 or W == 0: 
		return 0
	if t[n][W] != -1: 
		return t[n][W] 

	# choice diagram code 
	if wt[n-1] <= W: 
		t[n][W] = max( 
			val[n-1] + knapsack( 
				wt, val, W-wt[n-1], n-1), 
			knapsack(wt, val, W, n-1)) 
		return t[n][W] 
	elif wt[n-1] > W: 
		t[n][W] = knapsack(wt, val, W, n-1) 
		return t[n][W] 

# Driver code 
if __name__ == '__main__': 
	profit = [6, 1, 2] 
	weight = [1, 2, 3] 
	W = 5
	n = len(weight) 
	
	# We initialize the matrix with -1 at first. 
	t = [[-1 for i in range(W + 1)] for j in range(n + 1)] 
	
	print(knapsack(weight, profit, W, n)) 
	print(t)	

# This code is contributed by Prosun Kumar Sarkar 
