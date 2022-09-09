import sys
input = sys.stdin.readline

if __name__ == '__main__' :
    n = int(input())
    val = list(map(int,input().split(' ')))    

    dp = [1] * n
    for idx, v in enumerate(val) :
        for idx2 in range(idx+1, n) :
            if v > val[idx2] :
                dp[idx2] = max(dp[idx2], dp[idx] + 1)
    
    print(max(dp))