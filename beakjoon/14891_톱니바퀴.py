# # #극이 다르면 반대 방향 회전
# # # 같으면 회전 X
# # # 8개 -> 12시에서 시계방향으로 
# # # 0 = N, 1 = S
# # # K=회전횟수, (톱니바퀴 번호, 방향) -> 1= 시계, -1 = 반시계

# # # 왼쪽 공유 = 6, 오른쪽 공유 = 2

# # # 출력 -> 0번 index에 헤당-->
# # # 1번 : N = 0, S = 1
# # # 2번 : N = 0, S = 2
# # # 3번 : N = 0, S = 4
# # # 4번 : N = 0, S = 8

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def rotate(num, m, visited):
    global idx
    cur_val = [state[num][idx[num][0]], state[num][idx[num][1]]]
    visited[num] = True
    if m == -1:
        idx[num][0] = (idx[num][0] + 1)%8
        idx[num][1] = (idx[num][1] + 1)%8
    else :
        idx[num][0] = (idx[num][0] + 7)%8
        idx[num][1] = (idx[num][1] + 7)%8
    
    if 0<=num-1<4 and not visited[num-1] and state[num-1][idx[num-1][1]] != cur_val[0]:
        rotate(num-1,-m,visited)
    if 0<=num+1<4 and not visited[num+1] and state[num+1][idx[num+1][0]] != cur_val[1]:
        rotate(num+1,-m, visited)
    

state = [[] for _ in range(4)]
for i in range(4):
    state[i].extend(list(input().strip()))    
K = int(input())
idx = [[6,2],[6,2],[6,2],[6,2]]
ch_idx = [1,7]

for _ in range(K):
    num, move = map(int,input().split())
    visited = [False]*4
    rotate(num-1,move, visited)

result = 0
for i in range(4):
    cur = int(state[i][(idx[i][0]+2)%8])
    if cur == 0 : continue
    result += ((cur*2)**i)
print(result)