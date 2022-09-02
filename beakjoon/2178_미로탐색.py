from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split(' '))
matrix,queue = [],deque()
for _ in range(N):
    matrix.append(list(input().rstrip()))
dx = [1,-1,0,0]
dy = [0,0,1,-1]
queue.append([0,0,1])
matrix[0][0] = '0'
while queue :
    px,py,count = queue.popleft()
    for i in range(4):
        x,y = px+dx[i], py+dy[i]
        if x == N-1 and y == M-1 :
            print(count+1)
            exit(0)
        elif 0 <= x < N and 0 <= y < M and matrix[x][y] == '1':
            queue.append([x,y,count+1])
            matrix[x][y] = '0'