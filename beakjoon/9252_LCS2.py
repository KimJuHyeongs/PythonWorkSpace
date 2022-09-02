import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()
    
#P -> 0: 대각, 1: 위, 2: 왼쪽
dp,P = [[0]*(len(b)+1) for _ in range(len(a)+1)], [[-1]*(len(b)) for _ in range(len(a))]

for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if (a[i-1] == b[j-1]):
            dp[i][j] = dp[i-1][j-1] + 1
            P[i-1][j-1] = 0
        else:
            if dp[i-1][j] >= dp[i][j-1] :
                dp[i][j], P[i-1][j-1] = dp[i-1][j], 1
            else:
                dp[i][j], P[i-1][j-1] = dp[i][j-1], 2
x, y, result = len(a)-1, len(b)-1, ''
while x > -1 and y > -1 :
    d = P[x][y]
    if d == 0:
        result += a[x]
        x, y = x-1, y-1
    elif d == 1 : x-=1
    else : y-=1

print(dp[-1][-1])
print(''.join(reversed(result)))
