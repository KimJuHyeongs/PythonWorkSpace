import sys
input = sys.stdin.readline

N=int(input())
T,P,dp = [],[],[0]*(N+1)
pre_max = 0
for i in range(N):
    t,p = map(int,input().split())
    pre_max = max(pre_max,dp[i])
    if i+t < N+1:
        dp[i+t] = max(dp[i+t],pre_max+p)
    
print(max(dp))