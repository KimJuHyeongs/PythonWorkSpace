# 길이 N(짝수), 높이 H
# 첫 장애물 = 석순 -> 종유석 -> 석순 (번갈아)
# 석순 : 아래에서 나오는 것
import sys
input = sys.stdin.readline

n,h = map(int,input().split())
down, up = [0]*h,[0]*h
for i in range(n):
    height = int(input())
    # 석순
    if i%2 == 0:
        down[height-1] += 1
    # 종유석
    else :
        up[height-1] += 1

for i in range(h-2,-1,-1):
    down[i] += down[i+1]
    up[i] += up[i+1]

min_val,count = n+1,0
for i in range(h):
    if min_val > (down[i] + up[h-i-1]):
        min_val,count = (down[i] + up[h-i-1]),1
    elif min_val == (down[i] + up[h-i-1]):
        count += 1
print(min_val,count)
