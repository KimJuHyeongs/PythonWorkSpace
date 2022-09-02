import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

M,N = map(int,input().split())
matrix = []
for i in range(M):
    matrix.append(list(map(int,input().split())))
dp = [[-1]*N for _ in range(M)]
dp[M-1][N-1] = 1

def dfs(nx,ny):
    global dp,matrix,M,N
    px,py = [1,-1,0,0], [0,0,1,-1]
    if dp[nx][ny] != -1:
        return dp[nx][ny]

    dp[nx][ny]=0
    for i in range(4):
        x,y = nx+px[i],ny+py[i]
        if 0<=x<M and 0<=y<N and matrix[x][y] < matrix[nx][ny]:
            dp[nx][ny] += dfs(x,y)
    
    return dp[nx][ny]

print(dfs(0,0))