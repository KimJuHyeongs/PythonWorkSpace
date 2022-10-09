if __name__ == '__main__' :
    n = int(input())
    dp = [0] * (n+1)
    print_check = 0

    if n < 4 :
        print(n)
        print_check = 1
    else :
        dp[1], dp[2], dp[3] = 1, 2, 3
        
        for idx in range(4, n+1) :
            dp[idx], multi = dp[idx-1] + 1, 2

            for idx2 in range(idx-3, 0, -1) :
                dp[idx] = max(dp[idx], (dp[idx2]*multi))
                multi = multi + 1
            
    if print_check == 0:
        print(dp[n])
