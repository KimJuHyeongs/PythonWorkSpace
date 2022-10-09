if __name__ == '__main__' :
    n, s, m = map(int,input().split())
    v = list(map(int,input().split()))
    
    dp = [0]*(m+1)
    dp[s] = 1

    for val in v :
        cur_v = list()
        for idx in range(m+1) :
            if dp[idx] == 1 :
                dp[idx] = 0
                cur_v.append(idx)
        
        for cv in cur_v :
            if 0 <= (cv + val) <= m :
                dp[cv + val] = 1
            if 0 <= (cv - val) <= m :
                dp[cv - val] = 1
        
    for idx in range(m,-1,-1) :
        if dp[idx] == 1:
            print(idx)
            exit(0)
    
    print(-1)
