# 1 : 벽, 
# 2 : 비활성 바이러스,
# 3 : 활성 바이러스, 
# 빈칸 : 퍼지는 시간

import sys
import copy
import math
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def bfs(tmp_matrix,virus_li):
    queue = deque(virus_li)
    visited = [[False]*N for _ in range(N)]
    last = 0
    while queue:
        ppx, ppy, depth = queue.popleft()
        for k in range(4):
            r,c = ppx + tx[k], ppy + ty[k]
            if 0<=r<N and 0<=c<N and not visited[r][c] and tmp_matrix[r][c] != 1:
                visited[r][c]= True
                if tmp_matrix[r][c] == 0:
                    last = depth + 1
                    tmp_matrix[r][c] = 2
                queue.append((r,c,depth+1))
    return last

def run_virus(start,virus_li):
    global matrix,result
    
    if len(virus_li) == M:
        tmp_matrix = copy.deepcopy(matrix)
        tmp_result = bfs(tmp_matrix,virus_li)
        one_matrix = sum(tmp_matrix,[])
        # 바이러스가 퍼지지 않은 곳이 없다
        if not 0 in one_matrix:
            result = min(result,tmp_result)

    else :
        for i in range(start,N*N):
            x,y = divmod(i,N)
            if matrix[x][y] == 2:
                matrix[x][y] = 3
                virus_li.append((x,y,0))
                run_virus(i,virus_li)
                virus_li.remove((x,y,0))
                matrix[x][y] = 2

# 4<=N<=50, 1 <=M<=10
N, M =map(int,input().split())
tx,ty,result = [1,-1,0,0],[0,0,1,-1], math.inf

matrix = [list(map(int,input().split())) for _ in range(N)]
virus_li = []
run_virus(0,virus_li)
if result == math.inf:
    print(-1)
else :
    print(result)