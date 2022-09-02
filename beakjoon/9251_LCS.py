import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()
dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]

for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        #추가된 문자가 동일
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else :
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])
print(dp[-1][-1])