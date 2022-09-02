import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n,words = int(input()), []
    for _ in range(n):
        tmp = input().strip()
        words.append((len(tmp),tmp))
    words = list(set(words))
    words.sort(key = lambda x : (x[0],x[1]))
    for word in words:
        print(word[1])