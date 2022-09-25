import sys
input = sys.stdin.readline

if __name__ == '__main__' :
    n = int(input())

    matrix, dp = list(), [[0]*n for _ in range(n)]
    dp[0][0] = 1
    px, py = [1, 0], [0,1]

    for _ in range(n) :
        matrix.append(list(map(int,input().split())))

    for row in range(n) :
        for col in range(n) :
            if dp[row][col] == 0 or matrix[row][col] == 0 :
                continue

            val = matrix[row][col]
            
            for idx in range(2) :
                tx, ty = (row + (px[idx]*val)), (col + (py[idx]*val)) 
                
                if (0 <= tx < n) and (0 <= ty < n) :
                    dp[tx][ty] += dp[row][col]
    
    print(dp[-1][-1])