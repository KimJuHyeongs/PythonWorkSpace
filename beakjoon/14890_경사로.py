import sys
import copy
input = sys.stdin.readline

def check_road(matrix):
    global result

    for i in range(N):
        rvisit,check  = [False]*N, 1
        for j in range(N-1):
            if abs(matrix[i][j] - matrix[i][j+1]) == 0:
                continue
            elif abs(matrix[i][j] - matrix[i][j+1]) > 1 :
                check = 0
                break
            else :
                #뒤가 더 작다
                if matrix[i][j] > matrix[i][j+1] :
                    if N-(j+1) < L:
                        check = 0
                        break
                    elif rvisit[j+1:j+1+L].count(True) != 0 or L != matrix[i][j+1:j+1+L].count(matrix[i][j+1]):
                        check = 0
                        break
                    rvisit[j+1:j+1+L] = [True]*L
                # 앞이 더 작다
                else :
                    if j+1 < L:
                        check = 0
                        break
                    elif rvisit[j+1-L:j+1].count(True) != 0 or L != matrix[i][j+1-L:j+1].count(matrix[i][j]):
                        check = 0
                        break
                    rvisit[j+1-L:j+1] = [True]*L
        result += check

        
N,L = map(int,input().split())
m = [list(map(int,input().split())) for _ in range(N)]
t_m = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        t_m[i].append(m[j][i])
result = 0

check_road(m)
check_road(t_m)

print(result)
