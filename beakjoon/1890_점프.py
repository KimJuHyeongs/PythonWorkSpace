import sys
input = sys.stdin.readline

li = []
N = int(input())
for _ in range(N):
    li.append(list(map(int,input().split(' '))))
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1
for x in range(N):
    for y in range(N):
        if x == N-1 and y == N-1 : break
        move = li[x][y]
        if x+move < N :
            dp[x+move][y] += dp[x][y]
        if y+move < N :
            dp[x][y+move] += dp[x][y]
print(dp[N-1][N-1])
        


    

