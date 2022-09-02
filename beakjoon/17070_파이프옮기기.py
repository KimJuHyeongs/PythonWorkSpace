# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# def dfs(cx,cy,cd):
#     global result
    
#     if cx==n-1 and cy == n-1:
#         result += 1    
#     for cur_dir,(tx,ty) in enumerate(dir[cd]):
#         flag = True
#         x,y = cx+tx, cy+ty
#         if x <0 or x >=n or y < 0 or y>= n or matrix[x][y] == 1:
#             continue
        
#         for ch_x,ch_y in checks[(tx,ty)]:
#             xx,yy = cx+ch_x,cy+ch_y
#             if x <0 or x >=n or y < 0 or y>= n or matrix[xx][yy] == 1:
#                 flag = False
#                 break
#         if flag:
#             dfs(x,y,cur_dir)
    
# if __name__ == '__main__':
#     n = int(input())
#     matrix = [list(map(int,input().split())) for _ in range(n)]
#     # 0 = 가로, 1 = 가로대각선, 2 = 세로
#     dir = [[(0,1),(1,1),(n+1,n+1)],[(0,1),(1,1),(1,0)],[(n+1,n+1),(1,1),(1,0)]]
#     checks = {(0,1):[(0,1)], (1,1):[(0,1),(1,1),(1,0)], (1,0):[(1,0)]}
#     result = 0

#     dfs(0,1,0)
#     print(result)

import sys
from collections import defaultdict
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    # 0 = 가로, 1 = 가로대각선, 2 = 세로
    dp = [ [[0]*n for _ in range(n)] for _ in range(3)]
    dp[0][0][1] = 1
    for i in range(2,n):
        if matrix[0][i]:
            break
        dp[0][0][i] = 1
    
    for x in range(1,n):
        for y in range(2,n):
            if not(matrix[x][y] or matrix[x-1][y] or matrix[x][y-1]):
               dp[1][x][y] = sum(dp[i][x-1][y-1] for i in range(3))
            if not matrix[x][y]:
                dp[0][x][y] = dp[1][x][y-1] + dp[0][x][y-1]
                dp[2][x][y] = dp[1][x-1][y] + dp[2][x-1][y]
    print(sum(dp[i][n-1][n-1] for i in range(3)))
