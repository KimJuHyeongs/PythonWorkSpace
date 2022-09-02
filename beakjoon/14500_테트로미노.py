# # import sys
# # input = sys.stdin.readline

# # N,M = map(int,input().split())
# # matrix = [list(map(int,input().split())) for _ in range(N)]

# # shapes = [
# #     [(0, 0), (0, 1), (1, 0), (1, 1)], [(0, 0), (0, 1), (0, 2), (0, 3)],
# #     [(0, 0), (1, 0), (2, 0), (3, 0)], [(0, 0), (1, 0), (1, 1), (2, 1)],
# #     [(0, 0), (1, 0), (1, -1), (2, -1)], [(0, 0), (0, 1), (1, 1), (1, 2)],
# #     [(0, 0), (0, 1), (-1, 1), (-1, 2)], [(0, 0), (0, 1), (0, 2), (1, 2)],
# #     [(0, 0), (1, 0), (2, 0), (2, -1)], [(0, 0), (1, 0), (1, 1), (1, 2)],
# #     [(0, 0), (0, -1), (1, -1), (2, -1)], [(0, 0), (-1, 0), (-1, 1), (-1, 2)],
# #     [(0, 0), (1, 0), (2, 0), (2, 1)], [(0, 0), (0, 1), (0, 2), (-1, 2)],
# #     [(0, 0), (0, 1), (1, 1), (2, 1)], [(0, 0), (0, 1), (-1, 1), (0, 2)],
# #     [(0, 0), (1, 0), (1, 1), (2, 0)], [(0, 0), (0, 1), (1, 1), (0, 2)],
# #     [(0, 0), (1, 0), (1, -1), (2, 0)]
# # ]
# # max_val = -1
# # for i in range(N):
# #     for j in range(M):
# #         for k in shapes:
# #             tmp_val = 0
# #             for px,py in k:
# #                 x,y = i+px, j+py
# #                 if 0<=x<N and 0<=y<M :
# #                     tmp_val += matrix[x][y]
# #                 else :
# #                     break
# #             if max_val < tmp_val:
# #                 max_val = tmp_val

# # print(max_val)


import sys
input = sys.stdin.readline

def dfs(tx,ty,cnt,total,visited):
    global result
    if cnt==3:
        result = max(result,total)
        return

    if total+((3-cnt)*max_val) <= result:
        return

    for k in range(4):
        cx, cy = tx+px[k], ty+py[k]
        if 0<=cx<N and 0<=cy<M and not visited[cx][cy]:
            if cnt==1:
                visited[cx][cy] = True
                dfs(tx,ty,cnt+1,total+matrix[cx][cy],visited)
                visited[cx][cy] = False
            visited[cx][cy] = True
            dfs(cx,cy,cnt+1,total+matrix[cx][cy],visited)
            visited[cx][cy] = False

N,M = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
max_val = max(map(max,matrix))
px,py,result = [1,-1,0,0],[0,0,1,-1],0
visited = [[False]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i,j,0,matrix[i][j],visited)
        visited[i][j] = False
print(result)