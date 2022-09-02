import sys
input = sys.stdin.readline

N,K,Q,M = map(int,input().split(' '))
K_li = list(map(int,input().split(' ')))
Q_li = list(map(int,input().split(' ')))
M_li = []
N += 2
check = [False]* (N+1)

for _ in range(M):
    M_li.append(list(map(int,input().split(' '))))

for i in Q_li :
    if (i in K_li) == True :
        continue
    count = N//i
    tmp = [i*k for k in range(1,count+1)]
    for j in K_li :
        if (j in tmp) == True :
            tmp.remove(j)
    for j in tmp :
        check[j] = True
            
result = [0] * (N+1)
for i in range(3,N+1) :
    result[i] = result[i-1] + int(check[i])

for i,j in M_li :
    print((j-i+1) - (result[j] - result[i-1]))



import sys
input = sys.stdin.readline

N,K,Q,M = map(int,input().split(' '))
K_li = list(map(int,input().split(' ')))
Q_li = list(map(int,input().split(' ')))
M_li = []
N += 2
sleep = [False]* (N+1)
check = [False]* (N+1)

for _ in range(M):
    M_li.append(list(map(int,input().split(' '))))

for i in K_li :
    sleep[i] = True

for i in Q_li :
    if sleep[i] :
        continue
    count = N//i
    for j in range(1,count+1) :
        if sleep[i*j] :
            continue
        check[i*j] = True
result = [0]*(N+1)
for i in range(3,N+1) :
    c = 0
    if check[i] == 0:
        c =1
    result[i] = result[i-1] + c

for i,j in M_li:
    print(result[j] - result[i - 1])