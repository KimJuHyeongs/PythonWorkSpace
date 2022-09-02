import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
matrix,queue = [],deque([[]])
for i in range(N):
    tmp = list(input().strip())
    matrix.append(tmp.copy())
    while 'o' in tmp:
        idx = tmp.index('o')
        queue[0] += [i,idx]
        tmp[idx] = ','
queue[0].append(0)

result = set()
px,py = [1,-1,0,0],[0,0,1,-1]
while queue:
    tx1,ty1, tx2, ty2, result_cnt = queue.popleft()
    if result_cnt >= 10 :
        continue
    for k in range(4):
        cnt = 0
        x1,y1,x2,y2= tx1+px[k], ty1+py[k], tx2+px[k],ty2+py[k]
        if (x1 < 0 or x1 >= N) or (y1 < 0 or y1 >= M) : cnt += 1
        if (x2 < 0 or x2 >= N) or (y2 < 0 or y2 >= M) : cnt += 1
        if cnt == 1 :
            print(result_cnt+1)
            exit(0)
        elif cnt == 0:
                tmp_cnt = 0
                if matrix[x1][y1] == '#':
                    x1,y1 = tx1,ty1
                    tmp_cnt += 1
                if matrix[x2][y2] == '#':
                    x2,y2 = tx2,ty2
                    tmp_cnt += 1
                if tmp_cnt != 2:
                    queue.append([x1,y1,x2,y2,result_cnt+1])

print(-1)