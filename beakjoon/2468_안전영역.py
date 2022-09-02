import sys
input = sys.stdin.readline
from collections import deque

matrix = []
N = int(input())
for _ in range(N):
    matrix.append(list(map(int,input().split(' '))))

max_val,min_val = 1,101
for i in range(N):
    max_tmp,min_tmp = max(matrix[i]), min(matrix[i])
    if max_tmp > max_val:
        max_val = max_tmp
    if min_tmp < min_val:
        min_val = min_tmp

area = 0
px,py = [1,-1,0,0],[0,0,1,-1]
for h in range(0,max_val):
    if h < min_val:
        if area < 1:
            area = 1
        continue
    visited,tmp_area = [[False]*N for _ in range(N)],0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == True:
                continue
            visited[i][j] = True
            if matrix[i][j] <= h:
                continue
            stack = deque()
            stack.append([i,j])
            tmp_area += 1
            while stack:
                tx,ty = stack.pop()
                for k in range(4):
                    x,y = px[k] + tx, py[k] + ty
                    if (0<=x<N) and (0<=y<N) and (visited[x][y] == False) and (matrix[x][y] > h) :
                        stack.append([x,y])
                        visited[x][y] = True
    if tmp_area == 0:
        print(area)
        exit(0)
    elif area < tmp_area:
        area = tmp_area
print(area)