import sys
input = sys.stdin.readline

if __name__ == '__main__' :
    s = int(input())
    cnt, val = 0, 1
    while s >= val :
        s -= val
        cnt += 1
        val += 1
    print(cnt)