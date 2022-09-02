# N = int(input())
# li,dp = [],[]
# li += list(map(int,input().split(' ')))
# dp = [[0,0] for _ in range(len(li))]
# dp[0] = [li[0],1]
# for i in range(1,N):
#     max_num = 0
#     max_length = 0
#     for j in range(0,i):
#         if li[j] > li[i] and max_length <= dp[j][1]:
#             if max_num < dp[j][0]:
#                 max_num = dp[j][0]
#                 max_length = dp[j][1]
#     dp[i] = [li[i] + max_num,max_length+1]
# print(max(dp,key = lambda x : x[1])[1])


# N = int(input())
# li = list(map(int,input().split()))
# dp,idx = [li[0]],0

# for i in range(1,N):
#     if dp[idx] > li[i]:
#         dp.append(li[i])
#         idx += 1
#     else :
#         for j in range(idx+1):
#             # 같다가 없으면 더 작은 부분도 확인하게 되기 때문에 코드가 제대로 동작하지 않는다.
#             if dp[j] <= li[i]:
#                 dp[j] = li[i]
#                 break
# print(len(dp))




