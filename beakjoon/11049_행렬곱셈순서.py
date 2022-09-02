import math
import sys
input = sys.stdin.readline

N, li = int(input()), []
li = list(map(int,input().split()))
dp = [[0]*N for _ in range(N)] 
for _ in range(1,N):
    _,b = map(int,input().split())
    li.append(b)
for x in range(1,N):
    for i in range(N-x):
        j = i+x
        dp[i][j] = math.inf
        for k in range(i,j):
            dp[i][j] = min(dp[i][j],dp[i][k] + dp[k+1][j] + (li[i]*li[j+1]*li[k+1]))
print(dp[0][-1])

