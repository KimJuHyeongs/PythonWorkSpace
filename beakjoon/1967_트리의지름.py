# import sys
# input = sys.stdin.readline

# def dijkstra(start):
#     S,D = [False]*n, [-1]*n
#     for e, w in graph[start]:
#         D[i] = W[start][i]
#     S[start],D[start] = True, 0

#     for i in range(n-2):
#         max_val,max_idx = -1,-1
#         for j in range(n):
#             if j == start: continue
#             if max_val < D[j]:
#                 max_val, max_idx = D[j], j
#         S[max_idx] = True
#         for w in range(n):
#             if S[w] :
#                 continue
#             D[w] = max(D[w], D[max_idx] + W[max_idx][w])
#     return max(D)
        
# n=int(input())
# W = [[-1]*n for _ in range(n)]
# for _ in range(n-1):
#     parent, child, weight = map(int,input().split())
#     W[parent-1][child-1] = weight
#     W[child-1][parent-1] = weight

# result = -1
# for i in range(n):
#     result = max(result, dijkstra(i))
# print(result)


import sys
from collections import deque
input = sys.stdin.readline               

def BFS(start):
    queue = deque()
    D = [-1] * n
    queue.append(start)
    D[start] = 0
    max_val, max_idx = -1, -1

    while queue:
        node = queue.popleft()
        for e, w in graph[node]:
            if D[e] == -1 :
                D[e] = D[node] + w
                queue.append(e)
                if max_val < D[e]:
                    max_val,max_idx = D[e],e
    return max_val, max_idx

n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n-1):
    p, c, w = map(int,input().split())
    graph[p-1].append([c-1,w])
    graph[c-1].append([p-1,w])
if n == 1:
    print(0)
    exit(0)
_, tmp_idx = BFS(0)
result, _ = BFS(tmp_idx)
print(result)