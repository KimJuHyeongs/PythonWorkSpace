from operator import truediv
import sys
input = sys.stdin.readline

if __name__ == '__main__' :
    n = int(input())
    have = list(map(int,input().split(' ')))
    m = int(input())
    comp = list(map(int,input().split(' ')))

    have.sort()
    
    for c in comp:
        start, end = 0, len(have)-1

        while True:
            half = int((start + end)/2)

            if c == have[half] :
                print(1, end = ' ')
                break
            elif start >= end :
                print(0, end = ' ')
                break
            elif c < have[half] :
                end = half - 1
            else :
                start = half + 1
    print()
