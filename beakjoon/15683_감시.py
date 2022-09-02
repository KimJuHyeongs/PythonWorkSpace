# # 대각선 감시 불가능
# # 0 = 빈칸, 6 = 벽, 1~5 = CCTV
# # CCTV는 8대 이하

# import sys
# from collections import deque
# import copy
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# def move(tx,ty,sd,tmp_matrix):
#     while True:
#         cx,cy = tx+px[sd],ty+py[sd]
#         if cx < 0 or cx >= N or cy < 0 or cy >= M or tmp_matrix[cx][cy] == 6:
#             break
#         elif tmp_matrix[cx][cy] == 0:
#             tmp_matrix[cx][cy] = -1
#         tx, ty = cx,cy

# def select(d):
#     global result

#     if len(d) == len(cctv):
#         tmp_matrix = copy.deepcopy(matrix)
#         for idx,(tx, ty, cctv_num) in enumerate(cctv):
#             if cctv_num == 1:
#                 move(tx,ty,d[idx],tmp_matrix)
#             elif cctv_num == 2:
#                 move(tx,ty,d[idx],tmp_matrix)
#                 move(tx,ty,(d[idx]+2)%4,tmp_matrix)
#             elif cctv_num == 3:
#                 move(tx,ty,d[idx],tmp_matrix)
#                 move(tx,ty,(d[idx]+1)%4,tmp_matrix)
#             else:
#                 move(tx,ty,d[idx],tmp_matrix)
#                 move(tx,ty,(d[idx]+1)%4,tmp_matrix)
#                 move(tx,ty,(d[idx]+2)%4,tmp_matrix)
#         result = min(result,sum(_.count(0) for _ in tmp_matrix))
#         if result == 0:
#             print(0)
#             exit(0)

#     else :
#         for i in range(4):
#             d.append(i)
#             select(d)
#             d.pop()

# if __name__ == '__main__':
#     # 1 <= N,M<=8
#     N,M = map(int,input().split())
#     # 1 = 한 방향, 2 = 2개(서로 반대), 3 = 직각
#     matrix,cctv,five = [], deque(), deque()
#     for i in range(N):
#         tmp = list(map(int,input().split()))
#         matrix.append(tmp)
#         for j,t in enumerate(tmp):
#             if 1<=t<=4:
#                 cctv.append((i,j,t))
#             elif t == 5:
#                 five.append((i,j))
#     px,py = [0,-1,0,1], [-1,0,1,0]
#     num, direction = [4,2,4,4], [[],[2],[1],[1,2]]
    
#     #CCTV 5 처리
#     while five:
#         x,y = five.pop()
#         for k in range(4):
#             tx,ty = x,y
#             while True:
#                 cx,cy = tx+px[k],ty+py[k]
#                 if cx < 0 or cx >= N or cy < 0 or cy >= M or matrix[cx][cy] == 6:
#                     break
#                 elif matrix[cx][cy] == 0:
#                     matrix[cx][cy] = -1
#                 tx, ty = cx,cy
#     #나머지 CCTV 처리
#     result = N*M+1
#     d = deque()
#     select(d)    
#     print(result)


import sys
input = sys.stdin.readline

def move(cx,cy,sdir):
    tmp = set()
    for sd in sdir:
        x,y=cx+px[sd],cy+py[sd]
        while 0<=x<N and 0<=y<M :
            if matrix[x][y] == 6: break
            elif matrix[x][y] == 0: tmp.add((x,y))
            x,y = x+px[sd],y+py[sd]
    return tmp

def check(cnt, cur_set):
    global max_check

    if cnt == cctv:
        max_check = max(max_check, len(cur_set))
    else:
        for p in position[cnt]:
            check(cnt+1, cur_set|p)
          
N,M = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
px,py = [0,-1,0,1],[-1,0,1,0]
position,blank,cctv = [],0,0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            blank += 1
        elif matrix[i][j] == 1:
            position.append([move(i,j,[k]) for k in range(4)])
            cctv += 1
        elif matrix[i][j] == 2:
            position.append([move(i,j,[k,k+2]) for k in range(2)])
            cctv += 1
        elif matrix[i][j] == 3:
            position.append([move(i,j,[k,(k+1)%4]) for k in range(4)])
            cctv += 1
        elif matrix[i][j] == 4:
            position.append([move(i,j,[k,(k+1)%4,(k+2)%4]) for k in range(4)])
            cctv += 1
        elif matrix[i][j] == 5:
            position.append([move(i,j,[0,1,2,3])])
            cctv += 1
max_check = 0

check(0,set())
print(blank-max_check)