# 산성 : 양수, 알칼리성 : 음수
import sys
import math
input = sys.stdin.readline

def BS(s,e):
    result,result_val = math.inf,[0,0]
    while s < e:
        tmp = li[s] + li[e]
        if result > abs(tmp):
            result = abs(tmp)
            result_val = [li[s],li[e]]
        
        if tmp < 0 :
            s += 1
        elif tmp == 0:
            break
        else :
            e -= 1
    
    return result_val

N = int(input())
li = list(map(int,input().split()))
li.sort()
answer = BS(0,len(li)-1)
print(answer[0], answer[1])