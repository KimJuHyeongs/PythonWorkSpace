import sys
input = sys.stdin.readline

if __name__ == "__main__" :
    n = int(input())

    val_tmp, val = set(), list()
    for _ in range(n):
        val_tmp.add(input().rstrip())

    for v in val_tmp :
        val.append([len(v),v])
    
    val.sort(key = lambda x : (x[0], x[1]))

    for _,v in val:
        print(v)