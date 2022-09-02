import sys
input = sys.stdin.readline

def BT(idx,v,st):
    global result
    tmp_v,length = v,len(st)
    if idx >= C :
        return
    cur = li[idx]
    if cur in vowel :
        tmp_v += 1
    if length+1 == L and tmp_v >= 1 and (length+1) - tmp_v >= 2:
        result.append(st+cur)
    BT(idx+1,tmp_v,st+cur)
    BT(idx+1,v,st)

L,C = map(int,input().split())
li = list(input().split())
li.sort()
vowel = ['a','e','i','o','u']
result = []
BT(0,0,'')
for i in result:
    print(i)