# N : 1 ~ 20 , S : -1,000,000 ~ 1,000,000
import sys
input = sys.stdin.readline

def BT(idx,sum):
    global count
    if idx >= N:
        return
    sum += li[idx]
    if sum == S:
        count += 1
    BT(idx+1,sum)
    BT(idx+1,sum-li[idx])

N,S = map(int,input().split())
li = list(map(int,input().split()))
count = 0
BT(0,0)
print(count)
