import sys
input = sys.stdin.readline

if __name__ == '__main__' :
    num = int(input())
    dp, max_val = [0]*(num + 1), 0
    
    for idx in range(num) :
        d, p = map(int,input().split())

        max_val = max(dp[idx], max_val)
        if idx + d < num + 1 :
            dp[idx + d] = max(dp[idx + d], max_val + p)
        
    print(max(dp))
