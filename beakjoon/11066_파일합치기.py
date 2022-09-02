import sys
import math
input = sys.stdin.readline

for _ in range(int(input())):
    K = int(input())
    li = list(map(int,input().split()))
    dp = [[0]*K for _ in range(K)]
    for t in range(1,K):
        for i in range(K-t):
            j=i+t
            small = math.inf
            for k in range(i,j):
                small = min(small, dp[i][k] + dp[k+1][j])
            dp[i][j] = small + sum(li[i:j+1])
    print(dp[0][K-1])