import sys
input = sys.stdin.readline

floor,dp = [],[]
N = int(input())
for _ in range(N) :
    floor.append((int(input())))

if N == 1 :
    print(floor[0])
elif N==2 :
    print(max(floor[0]+floor[1], floor[1]))
else :
    dp.append(floor[0])
    dp.append(max(floor[0]+floor[1],floor[1]))
    dp.append(max(floor[0]+floor[2], floor[1]+floor[2]))
    for i in range(3,N) :
        dp.append(max( (dp[i-2]+floor[i]), (dp[i-3]+floor[i-1]+floor[i]) ))
    print(dp.pop(-1))