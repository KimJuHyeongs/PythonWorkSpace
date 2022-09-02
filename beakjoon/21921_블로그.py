N,X = map(int,input().split(' '))
li = []
li += list(map(int,input().split(' ')))
dp = li[::]

if sum(li) == 0 :
    print('SAD')
else:
    if N == X:
        print(sum(li))
        print(1)
    else :
        for i in range(1,X):
            dp[i] += dp[i-1]
        for i in range(X,N):
            dp[i] = li[i] + dp[i-1] - li[i-X]
        max_num = max(dp)
        print(max_num)
        print(dp.count(max_num))
