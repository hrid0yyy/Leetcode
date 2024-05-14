class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
 
        lands = []
        direction = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(x,y):
            lands.append((x,y))
            for dr,dc in direction:
                r = dr+x 
                c = dc+y
                if r in range(len(grid)) and c in range(len(grid[0])) and grid[r][c]=="1" and (r,c) not in lands: 
                    dfs(r,c)

        
        sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in lands and grid[i][j] == "1":
                    dfs(i,j)
                    sum += 1
        return sum

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
obj = Solution()
print(obj.numIslands(grid))
