N = int(input())
dp = [0 for _ in range(N)]
if N <= 3:
    print(N)
    exit(0)
dp[0],dp[1],dp[2] = 1,2,3
for i in range(3,N):
    max_val,multi = dp[i-1] + 1,2
    for j in range(i-3,-1,-1):
        if max_val < dp[j] * multi:
            max_val = dp[j] * multi
        multi += 1
    dp[i] = max_val
print(dp[N-1])