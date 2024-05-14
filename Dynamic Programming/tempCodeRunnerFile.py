path = [[1,2],
        [1,1]]

def get_dimensions(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if matrix else 0 
    return num_rows, num_cols
row = get_dimensions(path)[0] - 1
col = get_dimensions(path)[1] - 1

matrix = [[-1 for _ in range(col+1)] for _ in range(row+1)]


def search(x,y,path):
    if(row == 0 and col == 0):
        return path[0][0]
    if(matrix[x][y]!= -1):
        return matrix[x][y] 
    elif(x == row and y == col):
        return 0
    if(x+1<=row and y+1<=col):
        matrix[x][y] = min(search(x+1,y,path)+path[x+1][y],search(x,y+1,path)+path[x][y+1])
    if(x+1<=row):
        matrix[x][y] = (search(x+1,y,path)+path[x+1][y])
    if(y+1<=col):
        matrix[x][y] = (search(x,y+1,path)+path[x][y+1])
    return matrix[0][0] + path[0][0]

if __name__ == "__main__":
    print(search(0,0,path))
    print(matrix)