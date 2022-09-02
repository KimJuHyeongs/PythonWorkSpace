import sys
input = sys.stdin.readline

number = 10000
li = [0] * (number+1)

for i in range(2,number+1):
    li[i] = i

for i in range(2,number+1):
    if li[i] == 0 :
        continue
    for j in range(i+i,number+1,i):
        li[j] = 0

for _ in range(int(input())):
    N = int(input())
    for i in range(int(N/2),N+1):
        if li[i] and li[N-i]:
            print(N-i,i)
            break