import sys
input = sys.stdin.readline

t=int(input())
number = []
for _ in range(t):
    number.append(int(input()))
DP = [1,1,2]
for i in range(3,max(number)+1):
    DP.append(0)
    DP[i] = (DP[i-1] + DP[i-2] + DP[i-3]) % 1000000009

for i in number :
    print(DP[i])


##  모범답안
# from sys import stdin, stdout


# def sum123(N):
#     dp = [1,2,4]
#     if N <= 3:
#         return dp[N-1]
#     else:
#         for i in range(N-3):
#             dp.append((dp[-3]+dp[-2]+dp[-1]) % 1000000009)
#         return dp


# T = int(stdin.readline())
# N = []

# for t in range(1, T+1):
#     N.append(int(stdin.readline()))

# memo = sum123(max(N))

# for n in N:
#     stdout.write(str(memo[n-1]) + '\n')