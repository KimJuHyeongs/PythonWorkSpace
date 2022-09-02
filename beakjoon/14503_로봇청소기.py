# 왼쪽 청소 가능 -> 회전 -> 전진
# 왼쪽 청소 불가능 -> 회전 -> 다시 왼쪽 검사
# 이동가능 한 곳이 없으면 방향을 유지한 상태로 후진 -> 다시 왼쪽 검사
# 이동 가능한 곳이 없다 -> 후진도 벽이라 불가능 -> stop

# 0 : 북, 1 = 동, 2 = 남, 3 = 서
# import sys
# from collections import deque
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# def dfs(cx,cy,m_idx,check):
#     global result,visited

#     if check == 4 :
#         if matrix[cx-px[m_idx]][cy-py[m_idx]] == 1:
#             print(result)
#             exit(0)
#         else :
#             dfs(cx-px[m_idx],cy-py[m_idx],m_idx,-1)

#     elif check == 0 and matrix[cx][cy] == 0 and not visited[cx][cy] :
#         visited[cx][cy] = True
#         result += 1
#     check = max(0,check)
#     m_idx = (m_idx+3)%4
#     tx,ty = cx+px[m_idx], cy+py[m_idx]
#     if matrix[tx][ty] == 0 and not visited[tx][ty] :
#         cx,cy = dfs(tx,ty,m_idx,0)
#     else :
#         dfs(cx,cy,m_idx,check+1)
            
# N,M = map(int,input().split())
# cur_x, cur_y, move_idx = map(int,input().split())
# px, py = [-1,0,1,0], [0,1,0,-1]
# matrix = [list(map(int,input().split())) for _ in range(N)]
# result,visited = 0, [[False]*M for _ in range(N)]

# dfs(cur_x,cur_y,move_idx,0)



import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(cx,cy,m_idx,check):
    global result,visited

    if check and matrix[cx][cy] == 0 and not visited[cx][cy] :
        visited[cx][cy] = True
        result += 1
    
    for _ in range(4):
        m_idx = (m_idx+3)%4
        tx,ty = cx+px[m_idx], cy+py[m_idx]
        if matrix[tx][ty] == 0 and not visited[tx][ty] :
            dfs(tx,ty,m_idx,True)
            return

    if matrix[cx-px[m_idx]][cy-py[m_idx]] == 1:
        print(result)
        exit(0)
    else :
        dfs(cx-px[m_idx],cy-py[m_idx],m_idx,False)
            
N,M = map(int,input().split())
cur_x, cur_y, move_idx = map(int,input().split())
px, py = [-1,0,1,0], [0,1,0,-1]
matrix = [list(map(int,input().split())) for _ in range(N)]
result,visited = 0, [[False]*M for _ in range(N)]

dfs(cur_x,cur_y,move_idx,True)
