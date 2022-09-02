import sys
import math
from heapq import heappop, heappush, heapify
input = sys.stdin.readline

def dijkstra(src):
    dist = [math.inf]*(v+1)
    pq = [(0,src)]
    dist[src] = 0
    
    while pq:
        cw, cn = heappop(pq)
        if cw > dist[cn]:
            continue
        
        for tw, tn in graph[cn]:
            if cw+tw < dist[tn]:
                dist[tn] = cw+tw
                heappush(pq, (cw+tw, tn))    
    
    for val in dist[1:]:
        if val == math.inf : 
            print('INF')
            continue
        print(val)
        

if __name__ == '__main__':
    #정점 수 = v, 간선 수 = e
    v,e = map(int,input().split())
    # 시작정점 = k
    k = int(input())
    graph = [[] for _ in range(v+1)]
    # u -> v , w 가중치
    for _ in range(e):
        tu,tv,tw = map(int,input().split())
        graph[tu].append((tw,tv))
    dijkstra(k)
