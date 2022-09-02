# 0 : 주사위 바닥 면 값 복사, 나머지 : 이동하는 칸의 숫자가 주사위 바닥 칸에 복사
# 주사위 벗어나는 명령 무시 & 출력 X
# 1 = 동, 2 = 서, 3 = 북, 4 = 남

import sys
import copy
input = sys.stdin.readline

n,m,x,y,k = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]

moves = list(map(int,input().split()))

xdice, ydice = [0,0,0,0],[0,0,0,0]
plus = [1,3,3,1]
px, py = [0,0,-1,1],[1,-1,0,0]

for move in moves:
    move -= 1
    tmp_x,tmp_y = x + px[move], y+py[move]
    # 범위 밖 전처리
    if tmp_x < 0 or tmp_x >= n or tmp_y < 0 or tmp_y >= m :
        continue

    #주사위 움직이기
    if move == 1 or move == 0 :
        tmp_ydice = copy.deepcopy(ydice)
        for i in range(4):
            ydice[(i+plus[move])%4] = tmp_ydice[i]
        xdice[1], xdice[3] = ydice[1], ydice[3]
    else :
        tmp_xdice = copy.deepcopy(xdice)
        for i in range(4):
            xdice[(i+plus[move])%4] = tmp_xdice[i]
        ydice[1],ydice[3] = xdice[1], xdice[3]
    # 값 설정
    if matrix[tmp_x][tmp_y] == 0:
        matrix[tmp_x][tmp_y] = xdice[3]
    else :
        xdice[3] = ydice[3] = matrix[tmp_x][tmp_y]
        matrix[tmp_x][tmp_y] = 0
    x,y = tmp_x,tmp_y
    print(xdice[1])