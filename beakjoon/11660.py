from os import lseek
import sys
input = sys.stdin.readline

if __name__ == '__main__' :
    n,m = map(int, input().split(' '))
    val = [list(map(int,input().split(' '))) for _ in range(n)]
    
    dp = [[0]*(n+1) for _ in range(n+1)]
    
    for idx in range(1,n+1) :
        for idx2 in range(1,n+1) :
            dp[idx][idx2] = dp[idx][idx2 - 1] + val[idx-1][idx2-1]

    for idx in range(1,n+1) :
        for idx2 in range(1,n+1) :
            dp[idx2][idx] += dp[idx2-1][idx]

    for result_cnt in range(m) :
        x1, y1, x2, y2 = map(int,input().split(' '))
        
        print((dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]))