import sys
import copy
input = sys.stdin.readline

if __name__ == '__main__' :
    n = int(input())
    a = list(map(int,input().split(' ')))
    dp = copy.deepcopy(a)

    for idx in range(len(a)-1) :
        for idx2 in range(idx+1, len(a)) :
            if a[idx] < a[idx2] :
                dp[idx2] = max((a[idx2] + dp[idx]), dp[idx2])
    
    print(max(dp))