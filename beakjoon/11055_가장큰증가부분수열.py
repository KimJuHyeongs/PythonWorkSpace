N = int(input())
li = []
li += list(map(int,input().split(' ')))
dp = [0 for _ in range(len(li))]
dp[0] = li[0]
for i in range(1,len(li)) :
    max_num = 0
    for j in range(0,i):
        if li[j] < li[i] and max_num < dp[j]:
            max_num = dp[j]
    dp[i] = li[i] + max_num
print(max(dp))

# N = int(input())
# li = []
# li += list(map(int,input().split(' ')))
# dp = [0 for _ in range(len(li))]
# dp[0] = li[0]
# for i in range(1,len(li)) :
#     ## 아래 코드가 없으면 안되는데 왜 ...?
#     # dp[i] = li[i]
#     for j in range(0,i):
#         if li[j] < li[i] :
#             dp[i] = max(dp[i],li[i]+dp[j])
# print(max(dp))