N=int(input())
li = list(map(int,input().split(' ')))
M=int(input())
li2 = list(map(int,input().split(' ')))
li.sort()
for i in li2:
    start,end = 0,len(li)-1
    while True:
        half = int((start + end)/2)

        if i == li[half]:
            print(1, end = ' ')
            break
        if start >= end :
            print(0, end = ' ')
            break
        elif i > li[half]:
            start = half + 1
        else :
            end = half - 1




