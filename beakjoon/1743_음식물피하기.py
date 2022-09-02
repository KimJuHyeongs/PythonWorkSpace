import sys
from collections import deque
input = sys.stdin.readline

N,M,K = map(int,input().split(' '))
li = [[0]*M for _ in range(N)]
for _ in range(K):
    r,c = map(int,input().split(' '))
    li[r-1][c-1] = 1
px,py = [1,-1,0,0],[0,0,1,-1]
result = 0
visited,stack = [[False]*M for _ in range(N)],deque()
for i in range(N):
    for j in range(M):
        if li[i][j] == 1 and visited[i][j] == False:
            stack.append([i,j])
            visited[i][j] = True
            tmp_size = 0
            while stack:
                x,y = stack.pop()
                tmp_size += 1
                for j in range(4):
                    if 0 <= x+px[j] < N and 0 <= y+py[j] < M  and li[x+px[j]][y+py[j]] == 1 and visited[x+px[j]][y+py[j]] == False:
                        stack.append([x+px[j],y+py[j]])
                        visited[x+px[j]][y+py[j]] = True
            if tmp_size > result :
                result = tmp_size
print(result)