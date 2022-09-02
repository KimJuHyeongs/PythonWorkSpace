import sys
from collections import deque
input = sys.stdin.readline

if __name__ == '__main__':
    n, k = map(int,input().split())
    if k < n:
        print(n-k)
        print(1)
        exit(0)
    queue = deque([n])
    # 걸린 시간, 갯수
    visited = [[-1,0] for _ in range(1000001)]
    visited[n][0], visited[n][1] = 0,1
    
    while queue:
        v = queue.popleft()
        for tmp in (v+1,v-1,2*v):
            if 0<=tmp<1000001:
                if visited[tmp][0] == -1:
                    visited[tmp][0] = visited[v][0]+1
                    visited[tmp][1] = visited[v][1]
                    queue.append(tmp)
                elif visited[tmp][0] == visited[v][0]+1:
                    visited[tmp][1] += visited[v][1]
    
    print(visited[k][0])
    print(visited[k][1])