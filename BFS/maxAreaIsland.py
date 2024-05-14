class Solution(object):
    def maxAreaOfIsland(self, grid):
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
            temp = 1
            queue = []
            visited.add((r,c))
            queue.append((r,c))
            while queue:
                row, col = queue.pop()
                direction = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in direction:
                    r = dr + row
                    c = dc + col
                    if r in range(rows) and c in range(cols) and grid[r][c]== 1 and (r,c) not in visited:
                        queue.append((r,c))
                        visited.add((r,c))
                        temp += 1
            return temp

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    islands = max(islands,bfs(r,c))
        return islands