import sys
input = sys.stdin.readline

N,M = map(int,input().split(' '))
num_li = list(map(int,input().split(' ')))

num_li.insert(0,0)
for i in range(2,len(num_li)):
    num_li[i] += num_li[i-1]
for _ in range(M):
    i,j = map(int,input().split(' '))
    print(num_li[j] - num_li[i-1])
