import sys
input = sys.stdin.readline

if __name__ == '__main__':
    # 3<= n <= 100 , 0<=숫자범위 <= 20
    n = int(input())
    nums = list(map(int,input().split()))
    dp = [0]*21
    dp[nums[0]] = 1
    for num in nums[1:-1]:
        tmp = [0]*21
        for idx in range(len(dp)):
            if dp[idx] > 0:
                if 0<=idx+num<=20:
                    tmp[idx+num] += dp[idx]
                if 0<=idx-num<=20:
                    tmp[idx-num] += dp[idx]
        dp = tmp
    print(dp[nums[-1]])
    