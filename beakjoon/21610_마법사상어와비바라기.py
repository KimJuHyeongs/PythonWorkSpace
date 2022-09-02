# # # 좌표 -> 1~N, 행과 행 연결 ,열과 열 연결
# # # (N,1), (N,2), (N-1,1), (N-1,2) 비구름
# # # 명령 -> 방향(8개), 거리  (구름은 다 함께 이동)

# # # 구름 이동 -> 이동 위치 물 1 증가 -> 구름 제거 ->
# # # 이동 위치 물복사 (대각선 1에 물 바구니 수 만큼 물 증가) (격자 넘어가기 불가능)
# # #  물의 양 2 이상 -> 구름 생성 -> 물의 양 2 감소 (바로 전 구름이 사라진 칸은 불가능)

# # import sys
# # import copy
# # from collections import deque
# # input = sys.stdin.readline

# # def move_cloud(d,s,cloud):
# #     global matrix
    
# #     tmp_position = set()
# #     while cloud:
# #         # 구름 이동 & 물 증가
# #         tx, ty = cloud.pop()
# #         cx, cy = (tx+(px[d]*s))%N, (ty+(py[d]*s))%N
# #         matrix[cx][cy] += 1
# #         tmp_position.add((cx,cy))
# #     #대각선 탐색
# #     for cx, cy in tmp_position:
# #         tmp = 0
# #         for k in range(1,8,2):
# #             x, y = cx+px[k], cy+py[k]
# #             if 0<=x<N and 0<=y<N and matrix[x][y] != 0:
# #                 tmp += 1
# #         matrix[cx][cy] += tmp
# #     return tmp_position

# # def make_cloud(cloud):
# #     global matrix

# #     for i in range(N):
# #         for j in range(N):
# #             if (i,j) in tmp_cloud:
# #                 continue
# #             if matrix[i][j] >= 2:
# #                 cloud.append((i,j))
# #                 matrix[i][j] -= 2


# # if __name__ == '__main__':
# #     N,M = map(int,input().split())
# #     matrix = [list(map(int,input().split())) for _ in range(N)]
# #     move = [list(map(int,input().split())) for _ in range(M)]
# #     cloud = deque([(N-1,0),(N-1,1),(N-2,0),(N-2,1)])

# #     px, py = [0,-1,-1,-1,0,1,1,1], [-1,-1,0,1,1,1,0,-1]
# #     for d, s in move:
# #         # 구름 이동 -> 물 증가 -> 대각선 탐색 및 증가
        
# #         tmp_cloud = move_cloud(d-1,s,cloud)

# #         #새 구름 생성
# #         make_cloud(cloud)
    
# #     print(sum(map(sum,matrix)))


# 방향, 거리
import sys
import copy
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
move = [list(map(int,input().split())) for _ in range(M)]
px,py = [0,-1,-1,-1,0,1,1,1],[-1,-1,0,1,1,1,0,-1]
cloud = deque([(N-1,0),(N-1,1),(N-2,0),(N-2,1)])
for d,s in move:
    del_cloud = set()
    while cloud:
        cx,cy = cloud.pop()
        x,y = (cx+(px[d-1]*s))%N, (cy+(py[d-1]*s))%N
        del_cloud.add((x,y))
        matrix[x][y] += 1
    
    tmp_matrix = copy.deepcopy(matrix)
    for cx,cy in del_cloud:
        cnt = 0
        for k in range(1,8,2):
            x,y = cx+px[k], cy+py[k]
            if 0<=x<N and 0<=y<N and tmp_matrix[x][y] > 0:
                cnt += 1  
        matrix[cx][cy] += cnt
    
    for i in range(N):
        for j in range(N):
            if matrix[i][j] >= 2 and (i,j) not in del_cloud:
                matrix[i][j] -= 2
                cloud.append((i,j))

print(sum(map(sum,matrix)))

