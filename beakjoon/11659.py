import sys
from collections import deque
input = sys.stdin.readline


if __name__ == "__main__" :
    n, m = map(int,input().split(' '))
    q = deque(map(int,input().split(' ')))
    q.appendleft(0)

    for idx in range(n):
        q[idx+1] += q[idx] 

    for _ in range(m) :
        i, j = map(int,input().split(' '))
        
        print(q[j] - q[i-1])
