import sys
input = sys.stdin.readline

def del_node(g):
    global rm_set
    if len(g) == 0:
        return
    for node in g:
        rm_set.add(node)
        del_node(graph[node])

N = int(input())
graph = [set() for _ in range(N)]
parents = list(map(int,input().split()))
rm = int(input())
for node,p in enumerate(parents) :
    if p==-1: continue
    graph[p].add(node)
result,rm_set = set(), set({rm})
del_node(graph[rm])
for idx,g in enumerate(graph):
    g = g-rm_set
    if len(g) == 0:
        result.add(idx)
print(len(result - rm_set))