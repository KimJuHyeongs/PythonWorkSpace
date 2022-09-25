import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, k = map(int,input().split())

    coin, dp = list(), list(0 for _ in range(k+1))
    
    for _ in range(n) :
        coin.append(int(input()))
    
    dp[0] = 1
    for c in coin :
        for price in range(c,k+1):
            dp[price] += dp[price - c]
    
    print(dp[k])