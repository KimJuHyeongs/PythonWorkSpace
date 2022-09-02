import sys
from collections import deque
input = sys.stdin.readline

def is_correct(c,num):
    tmp_result = 0
    if len(pre) <= 0:
        print(0)
        exit(0)
    tmp = pre.pop()
    while type(tmp) == int:
        if len(pre) <= 0:
            print(0)
            exit(0)
        tmp_result += tmp
        tmp = pre.pop()
    if tmp == c:
        if tmp_result == 0:
            return num
        else :
            return tmp_result*num
    else :
        print(0)
        exit(0)

a=deque(input().rstrip())
a.reverse()
ch,pre,result = ['(',')','[',']'],deque(),0
while a:
    cur = a.pop()
    tmp_result = 0
    if cur == ch[1]:
        pre.append(is_correct(ch[0],2))
    elif cur == ch[3]:
        pre.append(is_correct(ch[2],3))
    else :
        pre.append(cur)
for i in pre:
    if type(i) != int:
        print(0)
        exit(0)
    result += i
print(result)
