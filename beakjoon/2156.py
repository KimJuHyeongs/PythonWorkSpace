# import sys
# input = sys.stdin.readline

# if __name__ == '__main__' :
#     num = int(input())
#     val, dp = list(), [0]*num

#     for _ in range(num):
#         val.append(int(input()))

#     if num == 1 :
#         print(val[0])
#     elif num == 2:
#         print(val[0] + val[1])
#     else :
#         dp[0] = val[0]
#         dp[1] = val[0] + val[1]
#         dp[2] = max( (val[0] + val[2]), (val[1] + val[2]))

#         for idx in range(3,num):
#             dp[idx] = val[idx] + max( (max(dp[:idx-2]) + val[idx-1]), max(dp[:idx-1]) )
        
#         print(max(dp))

# 모범 답안
import sys
input = sys.stdin.readline

val = []
for _ in range(int(input())) :
   val.append(int(input())) 

dp = [0, val[0], 0]

for idx in val[1:] :
    dp = [max(dp), dp[0]+idx, dp[1]+idx]
print(max(dp))