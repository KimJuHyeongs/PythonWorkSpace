# import sys
# input = sys.stdin.readline

# if __name__ == '__main__' :
#     result = 0
#     for _ in range(int(input())) :
#         word = input()
#         if list(word) == sorted(word, key = word.find):
#             result += 1
#     print(result)


import sys
input = sys.stdin.readline

if __name__ == '__main__' :
    result = 0
    for _ in range(int(input())):
        word = input()
        before, now = word[0], ''
        check = set({word[0]})
        for idx,w in enumerate(word[1:],start=1) :
            if before == word[idx] :
                continue
            else:
                if w in check:
                    result -= 1
                    break
                else:
                    check.add(w)
                    before = w
        
        result += 1
    
    print(result)
    