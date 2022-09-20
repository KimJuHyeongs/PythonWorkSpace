import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(r, c, size) :
    global visited

    for idx in range(4) :
        tx, ty = r + px[idx], c + py[idx]
        
        if ((0 < tx < (row+1)) and (0 < ty < (col+1))) :
            if matrix[tx][ty] and visited[tx][ty]:
                visited[tx][ty] = 0
                size = dfs(tx,ty,size+1)
            visited[tx][ty] = 0
    
    return size


if __name__ == '__main__' :
    row, col, k = map(int,input().split())

    matrix, visited = [[0]*(col+1) for _ in range(row+1)], [[1]*(col+1) for _ in range(row+1)]
    max_size = 0
    px, py = [-1,0,1,0],[0,1,0,-1]

    for _ in range(k) :
        x, y = map(int,input().split())
        matrix[x][y] = 1

    for r in range(1,row+1) :
        for c in range(1,col+1) :
            if matrix[r][c] and visited[r][c] :
                visited[r][c] = 0
                tmp_size = dfs(r,c,1)
                if max_size < tmp_size :
                    max_size = tmp_size

    print(max_size)