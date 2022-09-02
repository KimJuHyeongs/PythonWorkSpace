# 2 <= N <= 10,000
# N : 섬의 수, M : 다리의 수

import sys
from collections import deque
input = sys.stdin.readline

def BS():
    global start, end
    result = 1
    while start <= end :
        mid = (start+end)//2
        if BFS(mid):
            result,start = mid, mid + 1
        else :
            end = mid - 1
    return result

def BFS(t):
    queue = deque([src-1])
    visited = [False]*N
    visited[src-1] = True
    while queue:
        tmp = queue.popleft()
        if tmp == dst-1 :
            return True
        for d, w in graph[tmp]:
            if w >= t and not(visited[d]):
                queue.append(d)
                visited[d] = True
    return False

N,M = map(int,input().split())
graph = [[] for _ in range(N)]
start, end = int(1e10),0
for _ in range(M):
    s, d, w = map(int,input().split())
    graph[s-1].append([d-1,w])
    graph[d-1].append([s-1,w])
    start, end = min(start,w), max(end,w)
src, dst = map(int,input().split())
print(BS())
