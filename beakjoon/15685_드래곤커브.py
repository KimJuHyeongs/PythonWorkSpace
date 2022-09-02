# 0 = 우 , 1 = 위 , 2 = 좌, 3 = 아래
# [ 시작점, 시작점, 시작 방향, 세대]
#드래곤 커브 수
import sys
input = sys.stdin.readline

N = int(input())
matrix = [[False]*102 for _ in range(102)]
py,px = [0,-1,0,1],[1,0,-1,0]
total = set()
for _ in range(N):
    x,y,d,g = map(int,input().split())
    total.add((x,y))
    d_li = [d]
    cur_y,cur_x = y+py[d], x+px[d]
    matrix[y][x], matrix[cur_y][cur_x] = True, True
    total.add((cur_x,cur_y))
    for _ in range(g):
        for m in d_li[::-1]:
            m = (m+1)%4
            d_li.append(m)
            cur_y, cur_x = cur_y+py[m], cur_x+px[m]
            total.add((cur_x,cur_y))
            matrix[cur_y][cur_x] = True
result = 0
for cx, cy in total:
    if matrix[cy+1][cx+1] and matrix[cy+1][cx] and matrix[cy][cx+1] :
        result += 1
print(result)