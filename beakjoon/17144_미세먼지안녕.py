# A / 5 로 확산,  남은 양 = A - (A/5)*X(확산된 수)

# 공기청정기 -> 위 = 반시계, 아래 = 시계
# 바람의 방향으로 미세먼지 1칸 이동

# 미세먼지 확산 -> 공기청정기 작동

import sys
import copy
input = sys.stdin.readline

def move(tmp_matrix):
    global matrix

    for i in range(R):
        for j in range(0,2):
            if tmp_matrix[i][j] > 4:
                val, cnt = tmp_matrix[i][j]//5, 0
                for k in range(4):
                    cx, cy = i+px[k], j+py[k]
                    if 0<=cx<R and 0<=cy<C and tmp_matrix[cx][cy] != -1:
                        cnt += 1
                        matrix[cx][cy] += val
                matrix[i][j] -= val*cnt
        
        for j in range(2,C):
            if tmp_matrix[i][j] > 4:
                val, cnt = tmp_matrix[i][j]//5, 0
                for k in range(4):
                    cx, cy = i+px[k], j+py[k]
                    if 0<=cx<R and 0<=cy<C :
                        cnt += 1
                        matrix[cx][cy] += val
                matrix[i][j] -= val*cnt

def clean(position, plus):
    d, val = 0, 0
    cx, cy = position[0]+px[d], position[1]+py[d]
    while True:
        x, y = cx+px[d], cy+py[d]
        if x < 0 or x >= R or y < 0 or y >= C:
            d = (d+plus)%4
            continue
        if matrix[cx][cy] == -1:
            break
        matrix[cx][cy], val = val , matrix[cx][cy]
        cx, cy = x, y

if __name__ == '__main__':
    R,C,T = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(R)]
    air = []
    px, py = [0,-1,0,1], [1,0,-1,0]
    for i in range(R):
        if matrix[i][0] == -1:
           air.append((i,0))
           air.append((i+1,0))

    for _ in range(T) :
        tmp_matrix = copy.deepcopy(matrix)
        move(tmp_matrix)

        clean(air[0],1)
        clean(air[1],3)

    print(sum(map(sum,matrix)) + 2)
