import sys
input = sys.stdin.readline

n,s,m = map(int,input().split(' '))
v = list(map(int,input().split(' ')))
li = [False for _ in range(m+1)]
li[s] = True

for i in v:
    val = []
    for j in range(m+1):
        if li[j] == True:
            li[j] = False
            val.append(j)           
    for k in val:
        if k + i <= m:
            li[k+i] = True
        if k - i >= 0:
            li[k-i] = True

for i in range(m,-1,-1):
    if li[i] == True:
        print(i)
        exit(0)
print(-1)

## 모범 답안
# n,s,m=map(int,input().split())
# l,d=[*map(int,input().split())],[s]
# for i in l:
#     d=[*set([j+i for j in d if j+i<=m]+[j-i for j in d if j-i>=0])]
# print(max(d) if d else -1)