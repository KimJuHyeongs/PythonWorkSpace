import sys
from collections import deque
input = sys.stdin.readline

def topology():
    global graph, indegree

    queue,result = deque(),[]
    for idx in range(n):
        if indegree[idx] == 0:
            queue.append(idx)
    
    for idx in range(n):
        if not queue:
            exit(0)
        stu_num = queue.popleft()
        result.append(stu_num+1)
        for _ in range(len(graph[stu_num])):
            tmp = graph[stu_num].pop()
            indegree[tmp] -= 1
            if indegree[tmp] == 0:
                queue.append(tmp)
    
    return result
            
if __name__ == "__main__":
    # n : 학생 수, m : 키 비교 횟수
    n,m = map(int,input().split())
    graph,indegree = [[] for _ in range(n)], [0]*n
    # a b --> a가 b 앞에 서야한다. --> a보다 b가 크다
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a-1].append(b-1)
        indegree[b-1] += 1
    
    result = topology()
    for r in result:
        print(r, end = ' ')