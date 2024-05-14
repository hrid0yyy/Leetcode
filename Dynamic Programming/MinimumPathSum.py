class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """


        def get_dimensions(matrix):
            num_rows = len(matrix)
            num_cols = len(matrix[0]) if matrix else 0 
            return num_rows, num_cols
        row = get_dimensions(grid)[0] - 1
        col = get_dimensions(grid)[1] - 1

        matrix = [[-1 for _ in range(col+1)] for _ in range(row+1)]


        def search(x, y, path):
            if x == row and y == col:
                return path[x][y]
            
            if matrix[x][y] != -1:
                return matrix[x][y]

            down = search(x + 1, y, path) if x + 1 <= row else float('inf')
            right = search(x, y + 1, path) if y + 1 <= col else float('inf')

            matrix[x][y] = min(down, right) + path[x][y]
            return matrix[x][y]
        
        return search(0,0,grid)
if __name__ == '__main__':
    path = [[1,2,3],    # 12 11  9
           [4,5,6]]     # 3  11 -1
    obj = Solution()
    print(obj.minPathSum(path))