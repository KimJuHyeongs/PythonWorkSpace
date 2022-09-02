# #     dp = [[0]*(k+1) for _ in range(n+1)]
# #     cal(n,k)
# #     print(dp[n][k])

# import sys
# input = sys.stdin.readline

# def cal(tn,tk):
#     if tn == 0 or tk == 0:
#         return 0
#     if tk < val[tn][0]:
#         return cal(tn-1,tk)
#     else :
#         return max((val[tn][1]+cal(tn-1,tk-val[tn][0])), cal(tn-1,tk))

# if __name__ == '__main__':
#     n,k = map(int,input().split())
#     # [무게, 가치]
#     val= [[0,0]]
#     val += [list(map(int,input().split())) for _ in range(n)]

#     print(cal(n,k))


# import sys
# input = sys.stdin.readline

# if __name__ == '__main__':
#     n,k = map(int,input().split())
#     # [무게, 가치]
#     val= [[0,0]]
#     val += [list(map(int,input().split())) for _ in range(n)]
#     dp = [[0]*(k+1) for _ in range(n+1)]

#     for i in range(1,n+1):
#         for j in range(1,k+1):
#             if j < val[i][0]:
#                 dp[i][j] = dp[i-1][j]
#             else :
#                 dp[i][j] = max(val[i][1]+dp[i-1][j-val[i][0]], dp[i-1][j])

#     print(dp[n][k])


import sys
input = sys.stdin.readline

def sol12865():
    n, k = map(int, input().split())
    dp = {0:0}
    for i in range(n):
        w, v = map(int, input().split())
        u = {}
        for value, weight in dp.items():
            nw, nv = w + weight, v + value
            if nw < dp.get(nv,k+1):
                u[nv] = nw
        dp.update(u)
    return max(dp.keys())

if __name__ == '__main__':
    print(sol12865())