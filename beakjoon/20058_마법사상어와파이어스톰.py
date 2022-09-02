# 시계방향 90도 회전 -> 인접 중 2개 이상이 얼음 X = 해당 칸의 얼음 양 -1

# 1. 남아있는 얼음의 합, 2. 남아있는 것 중 가장 큰 덩어리 (인접하면 덩이리가 됨)

import sys
import copy
input = sys.stdin.readline


if __name__ == '__main__':
    N,Q = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(2**N)]
    L = list(map(int,input().split()))
    px,py = [0,0,1,-1], [1,-1,0,0]

    for l in L:
        k = 2**l
        #회전
        for i in range(0,2**N,k):
            for j in range(0,2**N,k):
                fx, fy = i+k, j+k
                tmp_matrix = [matrix[idx][j:fy] for idx in range(i,fx)]
                for x in range(k):
                    for y in range(k):
                        matrix[i+y][j+k-x-1] = tmp_matrix[x][y]
        
        # 얼음 제거
        tmp_matrix = copy.deepcopy(matrix)
        for i in range(2**N):
            for j in range(2**N):
                if tmp_matrix[i][j] > 0 :
                    cnt = 0
                    for u in range(4):
                        cx,cy = i+px[u], j+py[u]
                        if 0<=cx<2**N and 0<=cy<2**N and tmp_matrix[cx][cy]:
                            cnt += 1
                    if cnt < 3:
                        matrix[i][j] -= 1
    
    # 남아 있는 얼음의 합
    print(sum(map(sum,matrix)))
    
    result = 0
    for i in range(2**N):
        for j in range(2**N):
            if matrix[i][j] > 0:
                tmp_result, matrix[i][j] = 1,-1
                stack = [(i,j)]
                while stack:
                    tx,ty = stack.pop()
                    for u in range(4):
                        cx,cy = tx+px[u], ty+py[u]
                        if 0<=cx<2**N and 0<=cy<2**N and matrix[cx][cy] > 0:
                            matrix[cx][cy], tmp_result = -1, tmp_result+1
                            stack.append((cx,cy))
                result = max(result,tmp_result)
    
    print(result)