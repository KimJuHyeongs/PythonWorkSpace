# #오른쪽 이동 시작
# import sys
# from collections import deque
# input = sys.stdin.readline

# def go(dir,c):
#     global tx,ty,visited,matrix

#     tx,ty = tx+px[dir],ty+py[dir]
#     if 0<=tx<N and 0<=ty<N and not((tx,ty) in visited):
#         if matrix[tx][ty] == 1:
#             matrix[tx][ty] = 0
#         else :
#             visited.popleft()
#         visited.append((tx,ty))
#     else :
#         print(c)
#         exit(0)

# #보드크기
# N = int(input())
# # 사과의 수
# li,change,matrix,visited = [],[],[[0]*N for _ in range(N)],deque([(0,0)])
# for _ in range(int(input())):
#     x,y = map(int,input().split())
#     matrix[x-1][y-1] =1

# px,py = [0,1,0,-1],[1,0,-1,0]
# tx,ty,move_idx,result = 0,0,0,0
# #방향 변환 수
# for _ in range(int(input())):
#     X,C = input().split()
#     change.append((int(X),C))

# for X,C in change:
#     # C : 왼쪽 'L', 오른쪽 'D' -> 90도
#     # X는 오름차순 정렬 
#     for i in range(X-result):
#         go(move_idx,result+i+1)
#     result += (X-result)
#     if C == 'D':
#         move_idx = (move_idx+1)%4
#     else :
#         move_idx -= 1
#         if move_idx == -1:
#             move_idx = 3

# while True:
#     result += 1
#     go(move_idx,result)