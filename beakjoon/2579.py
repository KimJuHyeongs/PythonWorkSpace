import sys
input = sys.stdin.readline

if __name__ == '__main__' :
    num = int(input())
    val,dp = list(), [0]*num

    for _ in range(num) :
        val.append(int(input()))

    if num == 1 :
        print(val[0])
    elif num == 2:
        print(val[0] + val[1])
    else :
        dp[0] = val[0]
        dp[1] = val[0] + val[1]
        dp[2] = max( (val[0] + val[2]), (val[1] + val[2]) )
        
        for idx in range(3,num):
            dp[idx] = max( (dp[idx-3] + val[idx-1] + val[idx]), (dp[idx-2] + val[idx]))

        print(dp[-1])    
    