# 초기 아기상어 : 2, 자기보다 큰 곳 못지나감, 같은 크기 못 먹지만 지나는 감 
# 최소 거리 우선 (위 -> 왼쪽 순)
# 자기 크기만큼 먹어야 크기 1 증가

# import sys
# from collections import defaultdict
# input = sys.stdin.readline

# def find_near(r,c):
#     global eat,result,dic
#     tmp = 0
#     eat.sort()
#     min_val,rr,rc,rsize = N+N+1,0,0,0
#     for tr,tc,ts in eat:
#         if min_val > abs(tr-r) + abs(tc-c):
#             min_val = abs(tr-r) + abs(tc-c)
#             rr, rc, rsize = tr,tc, ts
#         # 거리가 같으면 위, 위도 여러개면 아래 이걸 어떻게 표현하누..
#     result += min_val
#     dic[rsize].remove((rr,rc))
#     return rr, rc
    

# cur_size,eat_size,result,dic = 2,0,0,defaultdict(list)
# # 2<=N<=20
# N = int(input())
# # 0 : 빈 칸, 1~8 :물고기, 9:아기상어
# for i in range(N):
#     tmp = list(map(int,input().split()))
#     for j,val in enumerate(tmp):
#         if val == 0 :
#             continue
#         dic[val].append((i,j))
# cur_x,cur_y = dic[9].pop()
        
# eat,neat = [],[]
# while True:
#     if eat_size == cur_size :
#         eat_size, cur_size = 0, cur_size + 1
    
#     for i in range(1,cur_size):
#         for r,c in dic[i]:
#             eat.append((r,c,i))
#     if len(eat) == 0:
#         print(result)
#         exit(0)
#     for i in range(cur_size+1,9):
#         for r,c in dic[i]:
#             neat.append((r,c))

#     eat_size += 1
#     cur_x, cur_y = find_near(cur_x,cur_y)
        






import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
cur_x, cur_y, cur_size, eat_size, result = 0, 0, 2, 0, 0

for i in range(0,N*N):
    x,y = divmod(i,N)
    if matrix[x][y] == 9:
        cur_x, cur_y = x,y
        matrix[x][y] = 0
        break
px,py = [1,-1,0,0], [0,0,1,-1]

while True:
    if eat_size == cur_size:
        eat_size, cur_size = 0, cur_size+1

    queue = deque([(cur_x,cur_y,0)])
    visited = [[False]*N for _ in range(N)]
    visited[cur_x][cur_y] = True
    eat = []
    
    while queue:
        tx,ty,length = queue.popleft()
        for k in range(4):
            x,y = tx+px[k], ty+py[k]
            if 0<=x<N and 0<=y<N and not visited[x][y] and matrix[x][y] <= cur_size:
                if 0 < matrix[x][y] < cur_size :
                    eat.append((x,y,length+1))
                visited[x][y] = True
                queue.append((x,y,length+1))
        
    if len(eat) == 0:
        break
    eat.sort(key = lambda x : (x[2],x[0],x[1]))
    eat_size += 1
    result += eat[0][2]
    cur_x,cur_y = eat[0][0], eat[0][1]
    matrix[cur_x][cur_y] = 0
    
print(result)

