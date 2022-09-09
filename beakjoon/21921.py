import sys
input = sys.stdin.readline

if __name__ == '__main__' :
    start, length = map(int,input().split(' '))
    val = list(map(int,input().split(' ')))

    dp = [0] * len(val)
    dp[0] = val[0]
    for idx in range(1,length) :
        dp[idx] = dp[idx-1] + val[idx]

    for idx in range(length,len(val)) :
        dp[idx] = dp[idx-1] + val[idx] - val[idx-length]
    
    max_val, cnt = max(dp), 0
    if max_val == 0:
        print('SAD')
    else :    
        for v in dp :
            if v == max_val :
                cnt += 1

        print(max_val)
        print(cnt)
