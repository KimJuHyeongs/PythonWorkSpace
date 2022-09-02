import sys
input = sys.stdin.readline

if __name__ == '__main__' :
    result = 0
    for _ in range(int(input())) :
        word = input()
        if list(word) == sorted(word, key = word.find):
            result += 1
    print(result)