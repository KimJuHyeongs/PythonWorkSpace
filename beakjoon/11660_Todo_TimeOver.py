from os import lseek
import sys
input = sys.stdin.readline

if __name__ == '__main__' :
    n,m = map(int, input().split(' '))
    val = [list(map(int,input().split(' '))) for _ in range(n)]
    
    dp = [[0]*n for _ in range(n)]
    
    for idx in range(n) :
        dp[idx][0] = val[idx][0]

    for idx in range(n) :
        for idx2 in range(1,n) :
            dp[idx][idx2] = dp[idx][idx2 - 1] + val[idx][idx2]

    for result_cnt in range(m) :
        x1, y1, x2, y2 = map(int,input().split(' '))
        result = 0

        for idx in range(x1-1, x2) :
            if y1 == 1:
                result += dp[idx][y2 - 1]
            else :
                result += dp[idx][y2 - 1] - dp[idx][y1 - 2]
        
        print(result)