# L<=인구차이<= R
# 연합 각 칸의 인구 수 = 연합 인구 수 / 연합의 칸 수 

# import sys
# from collections import deque
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# N, L, R = map(int,input().split())
# matrix = [list(map(int,input().split())) for _ in range(N)]
# px,py = [1,-1,0,0], [0,0,1,-1]

# result,ch_idx = 0, deque()
# while True :
#     visited, check = [[0]*N for _ in range(N)], False
#     for i in range(N):
#         for j in range(N):
#             if visited[i][j] == 0:
#                 tmp_check, visited[i][j] = False, 1
#                 for k in range(4):
#                     xx,yy = i+px[k], j+py[k]
#                     if 0<=xx<N and 0<=yy<N and not visited[xx][yy] and L<= abs(matrix[i][j] - matrix[xx][yy]) <= R :
#                         tmp_check = True
#                         break
                
#                 if tmp_check :
#                     ch_val, queue = matrix[i][j], deque([(i,j)])
#                     ch_idx.append((i,j))

#                     while queue:
#                         cx, cy = queue.popleft()
#                         cur_val = matrix[cx][cy]
#                         for k in range(4):
#                             tx,ty = cx+px[k], cy+py[k]
#                             if 0<=tx<N and 0<=ty<N and not visited[tx][ty] and L<= abs(cur_val - matrix[tx][ty]) <= R :
#                                 ch_val, visited[tx][ty] = ch_val + matrix[tx][ty], 1
#                                 queue.append((tx,ty))
#                                 ch_idx.append((tx,ty))

#                     num = ch_val // len(ch_idx)
#                     while ch_idx :
#                         cx,cy = ch_idx.pop()
#                         matrix[cx][cy] = num
#                     check = True
    
#     if not check : break
#     result += 1

# print(result)



# import sys
# from collections import deque
# input = sys.stdin.readline

# N, L, R = map(int,input().split())
# matrix = [list(map(int,input().split())) for _ in range(N)]
# px,py = [1,-1,0,0], [0,0,1,-1]

# result,ch_idx = 0, deque()
# while True :
#     visited, check = [[0]*N for _ in range(N)], False
#     for i in range(N):
#         for j in range(N):
#             if visited[i][j] == 0:
#                 visited[i][j] = 1
#                 ch_val, queue, cnt = matrix[i][j], deque([(i,j)]), 1
#                 ch_idx.clear()
#                 ch_idx.append((i,j))
#                 while queue:
#                     cx, cy = queue.popleft()
#                     cur_val = matrix[cx][cy]
#                     for k in range(4):
#                         tx,ty = cx+px[k], cy+py[k]
#                         if 0<=tx<N and 0<=ty<N and not visited[tx][ty] and L<= abs(cur_val - matrix[tx][ty]) <= R :
#                             ch_val, visited[tx][ty] = ch_val + matrix[tx][ty], 1
#                             cnt += 1
#                             queue.append((tx,ty))
#                             ch_idx.append((tx,ty))
#                 if cnt != 1:    
#                     num = ch_val // cnt
#                     for cx, cy in ch_idx:
#                         matrix[cx][cy] = num
#                     check = True
    
#     if not check : break
#     result += 1

# print(result)





import sys
from collections import deque

def bfs(i,j,visited,ans):
    q=deque()
    union=[(i,j)]
    q.appendleft((i,j))
    visited[i][j]=ans
    cnt=1
    population=country[i][j]

    while q:
        x,y=q.pop()

        for d in dir:
            nx,ny=x+d[0],y+d[1]
            if 0<= nx < N and 0<= ny <N:
                if visited[nx][ny] != ans and L <= abs(country[nx][ny] - country[x][y]) <= R:
                    visited[nx][ny]=ans
                    q.appendleft((nx,ny))
                    union.append((nx,ny))
                    cnt+=1
                    population+=country[nx][ny]

    # 인구 이동
    if cnt>1:
        pop_mean=population//cnt
        for x,y in union:
            country[x][y]=pop_mean
            search.appendleft((x,y))
        return True
    return False

N,L,R=map(int,sys.stdin.readline().split())
dir=[(1,0),(-1,0),(0,1),(0,-1)]
country=[]
for _ in range(N):
    country.append(list(map(int,sys.stdin.readline().split())))

search=deque()
for i in range(N):
    for j in range(N):
        search.appendleft((i,j))

visited=[[-1]*N for _ in range(N)]
def solution():
    ans=0
    while True:
        stop=True
        for _ in range(len(search)):
            i,j=search.pop()
            if visited[i][j]!=ans:
                if bfs(i,j,visited,ans):
                    stop =False
        if stop:
            break
        ans+=1
    print(ans)

solution()