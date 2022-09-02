# 번호, 방향 --> 1<=번호<=16(중복X) ,  (0,0) 물고기 방향과 동일 (8가지 방향)
# 45도 반시계 회전 -> 빈칸이면 이동, 물고기 있으면 교환
# (크기 작은 물고기부터 이동) 

# 상어 (0,0)에 배치 -> 물고기 이동 -> 상어 이동

#상어 -> 물고기 있는 칸으로 이동 , 한 뱡향으로 여러 칸 이동 가능
# 물고기 먹으면 물고기 방향을 가짐

# 상어가 먹는 물고기 번호의 합 중 최댓값

# import sys
# import copy
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# def BT(arr, cx, cy, r):
#     global result

#     tmp_arr = copy.deepcopy(arr)
#     r += tmp_arr[cx][cy][0]
#     tmp_arr[cx][cy][0] = -1

#     result = max(r,result)

#     fish_move(tmp_arr)

#     d, tmp_arr[cx][cy][0] = tmp_arr[cx][cy][1], 0
#     for i in range(1,4):
#         if (0<=cx+(px[d] * i)<4 and 0<=cy+(py[d] * i)<4 and tmp_arr[cx+(px[d] * i)][cy+(py[d] * i)][0] > 0) :
#             BT(tmp_arr, cx+(px[d] * i), cy+(py[d] * i), r) 

# def fish_position(arr,num):
#     for i in range(4):
#         for j in range(4):
#             if arr[i][j][0] == num:
#                 return i,j
#     return -1,-1

# def fish_move(arr):
#     for i in range(1,17):
#         fx,fy = fish_position(arr,i)
#         if fx == -1 : continue
        
#         for _ in range(8):
#             xx, yy = fx+px[arr[fx][fy][1]], fy+py[arr[fx][fy][1]]
#             if 0<=xx<4 and 0<=yy<4 and arr[xx][yy][0] != -1:
#                 arr[xx][yy][0], arr[fx][fy][0] = arr[fx][fy][0], arr[xx][yy][0]
#                 arr[xx][yy][1], arr[fx][fy][1] = arr[fx][fy][1], arr[xx][yy][1]
#                 break
#             else :
#                 # 마지막에 원래 방향으로 돌아가는 게 맞을까..?
#                 arr[fx][fy][1] = (arr[fx][fy][1]+1)%8
        

# tmp = [list(map(int,input().split())) for _ in range(4)]
# matrix = [[]*4 for _ in range(4)]
# px,py = [-1,-1,0,1,1,1,0,-1], [0,-1,-1,-1,0,1,1,1]
# for idx,t in enumerate(tmp):
#     for i in range(0,len(t),2):
#         matrix[idx].append([t[i],t[i+1]-1])

# #초기 상어 위치
# result = -1

# BT(matrix,0,0,0)
# print(result)

#45도 반시계
import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def fish_position(target,tmp_matrix):
    for i in range(4):
        for j in range(4):
            if tmp_matrix[i][j][0] == target:
                return i,j
    return -1,-1

def eat_fish(tx,ty,cnt,arr):
    global result

    tmp_matrix = copy.deepcopy(arr)
    #물고기 먹기
    cnt += tmp_matrix[tx][ty][0]
    tmp_matrix[tx][ty][0] = -1
    result = max(result,cnt)

    #물고기 이동
    for fish in range(1,17):
        fx,fy = fish_position(fish,tmp_matrix)
        if fx == -1: continue

        fdir = tmp_matrix[fx][fy][1]
        for k in range(8):
            cx,cy = fx+px[fdir],fy+py[fdir]
            if cx < 0 or cx >= 4 or cy < 0 or cy >=4 or tmp_matrix[cx][cy][0] == -1:
                fdir = (fdir+1)%8
                continue
            else :
                tmp_matrix[fx][fy][1] = fdir
                tmp_matrix[cx][cy], tmp_matrix[fx][fy] = tmp_matrix[fx][fy], tmp_matrix[cx][cy]
                break

    sdir = tmp_matrix[tx][ty][1]
    for k in range(1,4):
        sx, sy = tx+(px[sdir]*k), ty+(py[sdir]*k)
        if 0<=sx<4 and 0<=sy<4 and tmp_matrix[sx][sy][0] > 0:
            tmp_matrix[tx][ty][0] = 0
            eat_fish(sx,sy,cnt,tmp_matrix)
    
    return

matrix = [[] for _ in range(4)]
for i in range(4):
    tmp = list(map(int,input().split()))
    for j in range(0,len(tmp),2):
        matrix[i].append([tmp[j],tmp[j+1]-1])
px,py,result = [-1,-1,0,1,1,1,0,-1],[0,-1,-1,-1,0,1,1,1],0
eat_fish(0,0,0,matrix)

print(result)