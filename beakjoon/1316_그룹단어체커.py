import sys
input = sys.stdin.readline

if __name__ == '__main__' :
    n = int(input())
    result, word = 0, list()
    for _ in range(n):
        word.append(input())
    
    