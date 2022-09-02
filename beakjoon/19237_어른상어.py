# 냄새가 없는 칸 -> 자신의 냄새가 있는 칸(상어마다, 보는 방향 마다 차이)
# 이동 방향이 보는 방향
# 중복 -> 번호가 작은 1마리만 살아남음
# 1000초가 넘어가도 답이 안나오면 -1

import sys
import copy
input = sys.stdin.readline

def change_time(arr, total):
    remove_posi = set()
    for i,j in total:
        arr[i][j][2] -= 1
        if arr[i][j][2] == 0:
            arr[i][j] = [0,0,0]
            remove_posi.add((i,j))
    
    total -= remove_posi

if __name__ == '__main__':
    N,M,k = map(int,input().split())

    # [상어 번호, 냄새 주인, 남은 시간]
    matrix = [[[0,0,0]]*N for _ in range(N)]

    total_posi = set()
    cur_posi, cur_size, cur_time = [[] for _ in range(M+1)], M, 0 
    # 0 = 빈칸, 나머지 = 해당 번호의 상어
    for i in range(N):
        tmp = list(map(int,input().split()))
        for j,t in enumerate(tmp):
            if t != 0:
                total_posi.add((i,j))
                cur_posi[t].extend([i,j])
                matrix[i][j] = [t,t,k]

    # 1 = 위, 2 = 아래, 3 = 왼쪽, 4 = 오른쪽
    cur_d = [0]
    cur_d.extend(list(map(int,input().split())))

    # [상어 번호][현재 상어의 방향] = [우선 순위 4개]
    pri_d = [[] for _ in range(M+1)]
    px, py = [-1,1,0,0],[0,0,-1,1]
    for i in range(1,M+1):
        for j in range(4):
            pri_d[i].append(list(map(int,input().split())))

    while cur_time < 1000 and cur_size > 1:
        cur_time += 1
        
        # 이동
        tmp_matrix = copy.deepcopy(matrix)
        for idx in range(1,M+1):
            tx, ty = cur_posi[idx]
            if tx == -1: continue
            check = False
            # (냄새 없는 곳)
            for i in range(4):
                d = pri_d[idx][cur_d[idx]-1][i] - 1
                cx, cy = tx+px[d], ty+py[d]
                if 0<=cx<N and 0<=cy<N and tmp_matrix[cx][cy][1] == 0:
                    # 이동한 곳이 빈 공간
                    if matrix[cx][cy][0] == 0:
                        matrix[cx][cy], matrix[tx][ty][0] = [idx,idx,k+1], 0
                        cur_d[idx],cur_posi[idx] = d+1, [cx,cy]
                        total_posi.add((cx,cy))
                    # 이동한 곳에 다른 상어 존재
                    else:
                        # 나보다 숫자 큰 상어 -> 나로 바꿈
                        if matrix[cx][cy][0] > idx:
                            matrix[cx][cy], matrix[tx][ty][0] = [idx,idx,k+1], 0
                            cur_d[idx],cur_posi[idx] = d+1, [cx,cy]
                        # 나보다 숫자 작은 상어
                        else :
                            cur_size -= 1
                            matrix[tx][ty][0] = 0
                            cur_posi[idx] = [-1,-1]
                    check = True
                    break

            # 내 냄새, 상어 번호만 할당
            if check : continue
            for i in range(4):
                d = pri_d[idx][cur_d[idx]-1][i] - 1
                cx, cy = tx+px[d], ty+py[d]
                if 0<=cx<N and 0<=cy<N and matrix[cx][cy][1] == idx:
                    cur_d[idx],cur_posi[idx] = d+1, [cx,cy]
                    matrix[cx][cy][2], matrix[tx][ty][0] = k+1, 0
                    check = True
                    break

            if check : continue
            cur_size -= 1
            matrix[tx][ty][0] = 0
            cur_posi[idx] = [-1,-1]
        
        change_time(matrix,total_posi)
                            
    if cur_size != 1:
        print(-1)
        exit(0)
    print(cur_time)
