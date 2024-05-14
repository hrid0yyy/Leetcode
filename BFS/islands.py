class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        visited = set() 
        def bfs(r,c):
            queue = []
            visited.add((r,c))
            queue.append((r,c))
            while queue:
                row, col = queue.pop()
                direction = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in direction:
                    r = dr + row
                    c = dc + col
                    if row in range(rows) and col in range(cols) and grid[row][col]=="1" and (r,c) not in visited:
                        queue.append((r,c))
                        visited.add((r,c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands
        
grid =[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
obj = Solution()
print(obj.numIslands(grid))