# # 3개
# # 0 : 빈칸, 1: 벽, 2: 바이러스

# # import sys
# # import copy
# # from itertools import combinations as cb
# # input = sys.stdin.readline

# # def DFS(tx,ty,cm):
# #     for k in range(4):
# #         x,y = tx+px[k], ty+py[k]
# #         if 0<=x<N and 0<=y<M and cm[x][y] == 0:
# #             cm[x][y] = 2
# #             BFS(x,y,cm)
            

# # N,M = map(int,input().split())
# # matrix = [list(map(int,input().split())) for _ in range(N)]
# # zero = []
# # px,py = [1,-1,0,0],[0,0,1,-1]
# # result = -1

# # for i in range(N):
# #     for j in range(M):
# #         if matrix[i][j] == 0:
# #             zero.append((i,j))

# # cb_zero = list(cb(zero,3))

# # for cz in cb_zero:
# #     cp_matrix = copy.deepcopy(matrix)
# #     for x,y in cz:
# #         cp_matrix[x][y] = 1
# #     for i in range(N):
# #         for j in range(M):
# #             if cp_matrix[i][j] == 2:
# #                 DFS(i,j,cp_matrix)
# #     result = max(sum(i.count(0) for i in cp_matrix), result)
# # print(result)



import sys
import copy
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)] # 그래프 생성
dx, dy = [-1,1,0,0], [0,0,-1,1] # 상하좌우 이동

safe_region = 0 # 최대 안전 영역

# dfs
def dfs(x,y,sel_wall):
    sel_wall[x][y] = 2 # 바이러스로 변경

    # 상하좌우 탐색
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if sel_wall[nx][ny] == 0: # 바이러스가 퍼질 수 있는 곳
                dfs(nx,ny,sel_wall) # 바이러스 퍼뜨리기

# 벽 선택하기
def select_wall(start, count):
    global safe_region

    if count == 3: # 벽이 3개 선택된 경우 실행
        sel_wall = copy.deepcopy(graph) # 벽이 선택된 그래프 복사
        # dfs로 바이러스 퍼뜨리기
        for i in range(N):
            for j in range(M):
                if sel_wall[i][j] == 2: # 바이러스 발견시에 dfs
                    dfs(i,j,sel_wall)
        safe_count = sum(i.count(0) for i in sel_wall) # 안전 영역 개수 계산
        safe_region = max(safe_region,safe_count) # 최대 안전 영역 개수 갱신
        return

    else: # 벽이 3개 선택되지 않은 경우
        for i in range(start, N*M): # 브루트-포스로 벽 선택
            r = i // M # M으로 나눈 몫는 행
            c = i % M # M으로 나눈 나머지는 열
            if graph[r][c] == 0: # 해당 구역이 0인 경우에
                graph[r][c] = 1 # 벽으로 선택
                select_wall(i,count+1) # 다음 벽 선택
                graph[r][c] = 0 # 되돌리기

select_wall(0,0)
print(safe_region)