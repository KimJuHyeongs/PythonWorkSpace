# 1<= r,c <= N
# 0 = 빈칸, 1 = 집, 2 = 치킨집
# 1<= 집의 수<=2N
# M<=치킨 집 수<=13

import sys
input = sys.stdin.readline

def cal_dis(cur):
    total = 0
    for hx,hy in house:
        tmp = (2*N)+1
        for cx,cy in cur:
            tmp = min(tmp,abs(hx-cx) + abs(hy-cy))
        total += tmp
    return total

def make_chi(cur, idx):
    global result
    if idx == len(chi)+1:
        return
    
    if len(cur) == M:
        tmp_result = cal_dis(cur)
        result = min(tmp_result, result)
    
    else :
        for i in range(idx,len(chi)):
            cur.append(chi[i])
            make_chi(cur,i+1)
            cur.remove(chi[i])
            

N,M = map(int,input().split())
house, chi, matrix = [], [], []
for i in range(N):
    tmp = list(map(int,input().split()))
    for j,t in enumerate(tmp):
        if t == 1:
            house.append((i+1,j+1))
        elif t==2:
            chi.append((i+1,j+1))
result = (2*len(house)*N)+1

make_chi([],0)
print(result)


# import sys
# from itertools import combinations as cb
# input = sys.stdin.readline

# N,M = map(int,input().split())
# house, chi = [], []
# for i in range(N):
#     tmp = list(map(int,input().split()))
#     for j,t in enumerate(tmp):
#         if t == 1:
#             house.append((i+1,j+1))
#         elif t == 2:
#             chi.append((i+1,j+1))

# cb_comb = list(cb(chi,M))
# result = (2*N*len(house))+1
# for cb in cb_comb:
#     total = 0
#     for hx, hy in house:
#         tmp = (2*N)+1
#         for cx, cy in cb:
#             tmp = min(tmp,abs(hx-cx) + abs(hy-cy))
#         total += tmp
#     result = min(result, total)
# print(result)
